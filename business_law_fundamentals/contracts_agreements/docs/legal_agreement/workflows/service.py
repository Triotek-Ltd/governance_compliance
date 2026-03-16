"""Workflow service seed for legal_agreement."""

from __future__ import annotations


DOC_ID = "legal_agreement"
ARCHETYPE = "transaction"
INITIAL_STATE = 'draft'
STATES = ['draft', 'approved', 'executed', 'expired', 'renewed', 'archived']
TERMINAL_STATES = ['archived']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': 'approved'}, 'approve': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': 'approved'}, 'issue': {'allowed_in_states': ['approved'], 'transitions_to': 'executed'}, 'renew': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': 'renewed'}, 'archive': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': 'archived'}, 'route': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': None}, 'request_revision': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': None}, 'execute': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': None}, 'expire': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': None}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'draft and review legal agreements, then track the obligations they create', 'actors': ['legal reviewer', 'business owner', 'approver'], 'start_condition': 'a contract or legal obligation requires review', 'ordered_steps': ['Draft the agreement and key terms.', 'Execute the agreement and register obligations.', 'Monitor renewal, expiry, or breach conditions.'], 'primary_actions': ['create', 'update', 'execute', 'record', 'track', 'review', 'renew', 'close'], 'primary_transitions': ['legal_agreement: draft', 'legal_agreement: draft -> approved -> executed -> active'], 'downstream_effects': ['supports legal compliance and obligation management'], 'action_actors': {'create': ['legal reviewer'], 'review': ['legal reviewer'], 'submit': ['legal reviewer'], 'approve': ['approver'], 'issue': ['business owner'], 'archive': ['business owner'], 'execute': ['approver']}}

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
