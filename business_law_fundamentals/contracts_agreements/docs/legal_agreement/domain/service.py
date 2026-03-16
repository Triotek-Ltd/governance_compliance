"""Business-domain service seed for Legal Agreement."""

from __future__ import annotations


ARCHETYPE_PROFILE = {'workflow_profile': {'mode': 'transaction_flow', 'supports_submission': True}, 'reporting_profile': {'supports_snapshots': True, 'supports_outputs': True}, 'integration_profile': {'external_sync_enabled': True, 'tracks_external_refs': True}, 'lifecycle_states': ['draft', 'approved', 'executed', 'expired', 'renewed', 'archived'], 'is_transactional': True}

CONTRACT = {'title_field': 'title', 'status_field': 'workflow_state', 'reference_field': 'reference_no', 'required_fields': ['title', 'workflow_state', 'transaction_date'], 'field_purposes': {'workflow_state': 'lifecycle_state', 'transaction_date': 'transaction_date', 'party': 'primary_party', 'currency': 'currency_code', 'total_amount': 'total_amount', 'counterparty': 'party_reference', 'effective_date': 'schedule_marker', 'expiration_date': 'schedule_marker', 'routing_status': 'status_flag', 'related_legal_review_case': 'relation_collection', 'related_contract_obligation': 'relation_collection'}, 'search_fields': ['title', 'reference_no', 'description', 'agreement_number', 'agreement_type', 'counterparty'], 'list_columns': ['title', 'reference_no', 'transaction_date', 'party', 'total_amount', 'workflow_state'], 'initial_state': 'draft', 'lifecycle_states': ['draft', 'approved', 'executed', 'expired', 'renewed', 'archived'], 'terminal_states': ['archived'], 'action_targets': {'create': None, 'review': None, 'submit': 'approved', 'approve': 'approved', 'issue': 'executed', 'renew': 'renewed', 'archive': 'archived', 'route': None, 'request_revision': None, 'execute': None, 'expire': None}}

WORKFLOW_HINTS = {'business_objective': 'draft and review legal agreements, then track the obligations they create', 'actors': ['legal reviewer', 'business owner', 'approver'], 'start_condition': 'a contract or legal obligation requires review', 'ordered_steps': ['Draft the agreement and key terms.', 'Execute the agreement and register obligations.', 'Monitor renewal, expiry, or breach conditions.'], 'primary_actions': ['create', 'update', 'execute', 'record', 'track', 'review', 'renew', 'close'], 'primary_transitions': ['legal_agreement: draft', 'legal_agreement: draft -> approved -> executed -> active'], 'downstream_effects': ['supports legal compliance and obligation management'], 'action_actors': {'create': ['legal reviewer'], 'review': ['legal reviewer'], 'submit': ['legal reviewer'], 'approve': ['approver'], 'issue': ['business owner'], 'archive': ['business owner'], 'execute': ['approver']}}

SIDE_EFFECT_HINTS = {'downstream_effects': ['supports legal compliance and obligation management'], 'related_docs': ['legal_review_case', 'contract_obligation'], 'action_targets': {'create': None, 'review': None, 'submit': 'approved', 'approve': 'approved', 'issue': 'executed', 'renew': 'renewed', 'archive': 'archived', 'route': None, 'request_revision': None, 'execute': None, 'expire': None}, 'action_side_effects_file': 'side_effects.json'}

class DomainService:
    doc_id = "legal_agreement"
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
