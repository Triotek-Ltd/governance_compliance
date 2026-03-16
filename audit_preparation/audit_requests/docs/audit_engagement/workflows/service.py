"""Workflow service seed for audit_engagement."""

from __future__ import annotations


DOC_ID = "audit_engagement"
ARCHETYPE = "workflow_case"
INITIAL_STATE = 'open'
STATES = ['open', 'in_progress', 'closed', 'archived']
TERMINAL_STATES = ['closed', 'archived']
ACTION_RULES = {'create': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': 'in_progress'}, 'review': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': None}, 'close': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': 'archived'}, 'accept': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': None}, 'refer': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': None}, 'request_clarification': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': None}, 'escalate': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': None}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'prepare evidence and responses for audit activity, then track findings to remediation closure', 'actors': ['audit coordinator', 'requester', 'finding owner', 'reviewer'], 'start_condition': 'an internal or external audit cycle begins', 'ordered_steps': ['Open the audit engagement and confirm scope.'], 'primary_actions': ['create', 'review', 'approve'], 'primary_transitions': ['audit_engagement: draft -> approved -> active'], 'downstream_effects': ['supports governance assurance and remediation tracking', 'consulting explanations', 'implementation planning', 'user guides', 'demo narratives'], 'action_actors': {'create': ['audit coordinator'], 'assign': ['audit coordinator'], 'review': ['reviewer'], 'close': ['finding owner'], 'archive': ['finding owner']}}

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
