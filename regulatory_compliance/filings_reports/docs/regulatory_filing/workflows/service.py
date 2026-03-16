"""Workflow service seed for regulatory_filing."""

from __future__ import annotations


DOC_ID = "regulatory_filing"
ARCHETYPE = "transaction"
INITIAL_STATE = 'draft'
STATES = ['draft', 'submitted', 'confirmed', 'archived']
TERMINAL_STATES = ['archived']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': 'submitted'}, 'confirm': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': 'confirmed'}, 'archive': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': 'archived'}, 'assign': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': None}, 'mark_late': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': None}, 'request_revision': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': None}, 'record': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': None}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'track obligations, prepare filings, submit them, and retain submission evidence', 'actors': ['compliance officer', 'preparer', 'approver', 'regulator-facing submitter'], 'start_condition': 'a regulatory obligation or due date becomes actionable', 'ordered_steps': ['Create the filing record for the reporting period or event.', 'Prepare submission content and supporting documents.', 'Submit and confirm the filing.', 'Mark lateness, issues, or revisions if necessary.', 'Archive the completed regulatory record set.'], 'primary_actions': ['create', 'assign', 'review', 'record', 'request_revision', 'submit', 'confirm', 'mark_late', 'archive'], 'primary_transitions': ['regulatory_filing: draft', 'regulatory_filing: draft -> submitted -> confirmed'], 'downstream_effects': ['compliance history becomes available to audit, legal, risk, and reporting flows'], 'action_actors': {'create': ['compliance officer'], 'review': ['preparer'], 'submit': ['compliance officer'], 'confirm': ['approver'], 'archive': ['compliance officer'], 'assign': ['compliance officer'], 'record': ['compliance officer']}}

class WorkflowService:
    def allowed_actions_for_state(self, state: str | None) -> list[str]:
        if not state:
            return list(ACTION_RULES.keys())
        allowed = []
        for action_id, rule in ACTION_RULES.items():
            states = rule.get("allowed_in_states") or []
            if not states or state in states:
                allowed.append(action_id)
        return allowed

    def is_action_allowed(self, action_id: str, state: str | None) -> bool:
        return action_id in self.allowed_actions_for_state(state)

    def next_state_for(self, action_id: str) -> str | None:
        rule = ACTION_RULES.get(action_id, {})
        return rule.get("transitions_to")

    def apply_action(self, action_id: str, state: str | None) -> dict:
        if not self.is_action_allowed(action_id, state):
            raise ValueError(f"Action '{action_id}' is not allowed in state '{state}'")
        next_state = self.next_state_for(action_id)
        updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
        return {
            "action_id": action_id,
            "current_state": state,
            "next_state": next_state,
            "updates": updates,
        }

    def is_terminal(self, state: str | None) -> bool:
        return bool(state and state in TERMINAL_STATES)

    def workflow_summary(self) -> dict:
        return {
            "initial_state": INITIAL_STATE,
            "states": STATES,
            "terminal_states": TERMINAL_STATES,
            "business_objective": WORKFLOW_HINTS.get("business_objective"),
            "ordered_steps": WORKFLOW_HINTS.get("ordered_steps", []),
        }

    def workflow_profile(self) -> dict:
        return {'mode': 'transaction_flow', 'supports_submission': True}
