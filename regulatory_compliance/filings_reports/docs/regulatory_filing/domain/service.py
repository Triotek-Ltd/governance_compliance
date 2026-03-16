"""Business-domain service seed for Regulatory Filing."""

from __future__ import annotations


ARCHETYPE_PROFILE = {'workflow_profile': {'mode': 'transaction_flow', 'supports_submission': True}, 'reporting_profile': {'supports_snapshots': True, 'supports_outputs': True}, 'integration_profile': {'external_sync_enabled': True, 'tracks_external_refs': True}, 'lifecycle_states': ['draft', 'submitted', 'confirmed', 'archived'], 'is_transactional': True}

CONTRACT = {'title_field': 'title', 'status_field': 'workflow_state', 'reference_field': 'reference_no', 'required_fields': ['title', 'workflow_state', 'transaction_date'], 'field_purposes': {'workflow_state': 'lifecycle_state', 'transaction_date': 'transaction_date', 'party': 'primary_party', 'currency': 'currency_code', 'total_amount': 'total_amount', 'due_date': 'schedule_marker', 'submission_date': 'schedule_marker', 'related_submission_confirmation': 'relation_collection', 'related_compliance_record': 'relation_collection'}, 'search_fields': ['title', 'reference_no', 'description', 'filing_number', 'obligation', 'filing_type'], 'list_columns': ['title', 'reference_no', 'transaction_date', 'party', 'total_amount', 'workflow_state'], 'initial_state': 'draft', 'lifecycle_states': ['draft', 'submitted', 'confirmed', 'archived'], 'terminal_states': ['archived'], 'action_targets': {'create': None, 'review': None, 'submit': 'submitted', 'confirm': 'confirmed', 'archive': 'archived', 'assign': None, 'mark_late': None, 'request_revision': None, 'record': None}}

WORKFLOW_HINTS = {'business_objective': 'track obligations, prepare filings, submit them, and retain submission evidence', 'actors': ['compliance officer', 'preparer', 'approver', 'regulator-facing submitter'], 'start_condition': 'a regulatory obligation or due date becomes actionable', 'ordered_steps': ['Create the filing record for the reporting period or event.', 'Prepare submission content and supporting documents.', 'Submit and confirm the filing.', 'Mark lateness, issues, or revisions if necessary.', 'Archive the completed regulatory record set.'], 'primary_actions': ['create', 'assign', 'review', 'record', 'request_revision', 'submit', 'confirm', 'mark_late', 'archive'], 'primary_transitions': ['regulatory_filing: draft', 'regulatory_filing: draft -> submitted -> confirmed'], 'downstream_effects': ['compliance history becomes available to audit, legal, risk, and reporting flows'], 'action_actors': {'create': ['compliance officer'], 'review': ['preparer'], 'submit': ['compliance officer'], 'confirm': ['approver'], 'archive': ['compliance officer'], 'assign': ['compliance officer'], 'record': ['compliance officer']}}

SIDE_EFFECT_HINTS = {'downstream_effects': ['compliance history becomes available to audit, legal, risk, and reporting flows'], 'related_docs': ['regulatory_obligation', 'submission_confirmation', 'compliance_record'], 'action_targets': {'create': None, 'review': None, 'submit': 'submitted', 'confirm': 'confirmed', 'archive': 'archived', 'assign': None, 'mark_late': None, 'request_revision': None, 'record': None}, 'action_side_effects_file': 'side_effects.json'}

class DomainService:
    doc_id = "regulatory_filing"
    archetype = "transaction"
    doc_kind = "transaction"

    def required_fields(self) -> list[str]:
        return CONTRACT.get("required_fields", [])

    def state_field(self) -> str | None:
        return CONTRACT.get("status_field")

    def default_state(self) -> str | None:
        return CONTRACT.get("initial_state")

    def list_columns(self) -> list[str]:
        return CONTRACT.get("list_columns", [])

    def validate_invariants(self, payload: dict, *, partial: bool = False) -> dict:
        if partial:
            required_scope = [field for field in self.required_fields() if field in payload]
        else:
            required_scope = self.required_fields()
        missing_fields = [field for field in required_scope if not payload.get(field)]
        if missing_fields:
            raise ValueError(f"Missing required business fields: {', '.join(missing_fields)}")
        state_field = self.state_field()
        allowed_states = set(CONTRACT.get("lifecycle_states", []))
        if state_field and payload.get(state_field) and allowed_states and payload[state_field] not in allowed_states:
            raise ValueError(f"Invalid state '{payload[state_field]}' for {state_field}")
        return payload

    def prepare_create_payload(self, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        state_field = self.state_field()
        if state_field and not payload.get(state_field) and self.default_state():
            payload[state_field] = self.default_state()
        title_field = CONTRACT.get("title_field")
        reference_field = CONTRACT.get("reference_field")
        if title_field and not payload.get(title_field) and reference_field and payload.get(reference_field):
            payload[title_field] = str(payload[reference_field])
        payload = self.validate_invariants(payload)
        return payload

    def after_create(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def prepare_update_payload(self, instance, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        payload = self.validate_invariants(payload, partial=True)
        return payload

    def after_update(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def after_action(
        self,
        instance,
        action_id: str,
        payload: dict,
        action_result: dict,
        context: dict | None = None,
    ) -> dict:
        return {
            "updates": {},
            "side_effects": [],
        }

    def shape_retrieve_data(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        serialized_data.setdefault("_business_capabilities", self.business_capabilities())
        return serialized_data

    def workflow_objective(self) -> str | None:
        return WORKFLOW_HINTS.get("business_objective")

    def side_effect_hints(self) -> dict:
        return SIDE_EFFECT_HINTS

    def business_capabilities(self) -> dict:
        return {
            **ARCHETYPE_PROFILE,
            "required_fields": self.required_fields(),
            "state_field": self.state_field(),
            "default_state": self.default_state(),
        }
