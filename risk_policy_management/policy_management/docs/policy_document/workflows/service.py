"""Workflow service seed for policy_document."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "policy_document"
ARCHETYPE = "configuration"
INITIAL_STATE = 'draft'
STATES = ['draft', 'approved', 'published', 'archived']
TERMINAL_STATES = ['archived']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'approved'}, 'approve': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'approved'}, 'publish': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'published'}, 'archive': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'draft and review legal agreements, then track the obligations they create', 'actors': ['legal reviewer', 'business owner', 'approver'], 'start_condition': 'a contract or legal obligation requires review', 'ordered_steps': [], 'primary_actions': [], 'primary_transitions': [], 'downstream_effects': ['supports legal compliance and obligation management'], 'action_actors': {'create': ['legal reviewer'], 'submit': ['legal reviewer'], 'approve': ['approver'], 'publish': ['business owner'], 'archive': ['business owner']}}

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
        return cast(str | None, rule.get("transitions_to"))

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
        return {'mode': 'configuration_control', 'case_management': False}
