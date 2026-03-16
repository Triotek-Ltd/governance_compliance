"""Workflow service seed for risk_register_entry."""

from __future__ import annotations


DOC_ID = "risk_register_entry"
ARCHETYPE = "workflow_case"
INITIAL_STATE = 'open'
STATES = ['open', 'mitigated', 'closed', 'archived']
TERMINAL_STATES = ['closed', 'archived']
ACTION_RULES = {'create': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': None}, 'review': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': None}, 'approve': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': None}, 'close': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': 'archived'}, 'score': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': None}, 'mitigate': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': None}, 'escalate': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': None}, 'reopen': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': None}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'record risks, monitor treatment actions, and maintain policy updates in response to control needs', 'actors': ['risk owner', 'policy owner', 'reviewer'], 'start_condition': 'a risk or policy issue is identified', 'ordered_steps': ['Record the identified risk or policy trigger.'], 'primary_actions': ['create', 'review'], 'primary_transitions': ['risk_register_entry: draft -> active'], 'downstream_effects': ['supports compliance, audit, and business-law controls'], 'action_actors': {'create': ['risk owner'], 'review': ['reviewer'], 'approve': ['reviewer'], 'close': ['risk owner'], 'archive': ['risk owner']}}

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
        return {'mode': 'case_flow', 'supports_assignment': True, 'supports_escalation': True}
