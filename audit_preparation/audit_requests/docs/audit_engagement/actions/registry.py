"""Action registry seed for audit_engagement."""

from __future__ import annotations


DOC_ID = "audit_engagement"
ALLOWED_ACTIONS = ['create', 'assign', 'review', 'close', 'archive', 'accept', 'refer', 'request_clarification', 'escalate']
ACTION_RULES = {'create': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': 'in_progress'}, 'review': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': None}, 'close': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': 'archived'}, 'accept': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': None}, 'refer': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': None}, 'request_clarification': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': None}, 'escalate': {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': None}}

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
