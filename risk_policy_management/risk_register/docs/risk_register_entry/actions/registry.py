"""Action registry seed for risk_register_entry."""

from __future__ import annotations


DOC_ID = "risk_register_entry"
ALLOWED_ACTIONS = ['create', 'review', 'approve', 'close', 'archive', 'score', 'mitigate', 'escalate', 'reopen']
ACTION_RULES = {'create': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': None}, 'review': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': None}, 'approve': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': None}, 'close': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': 'archived'}, 'score': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': None}, 'mitigate': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': None}, 'escalate': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': None}, 'reopen': {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': None}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
