"""Action registry seed for regulatory_filing."""

from __future__ import annotations


DOC_ID = "regulatory_filing"
ALLOWED_ACTIONS = ['create', 'submit', 'confirm', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': 'submitted'}, 'confirm': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': 'confirmed'}, 'archive': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': 'archived'}}

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
