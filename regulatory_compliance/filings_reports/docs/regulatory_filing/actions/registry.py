"""Action registry seed for regulatory_filing."""

from __future__ import annotations

from typing import Any


DOC_ID = "regulatory_filing"
ALLOWED_ACTIONS = ['create', 'review', 'submit', 'confirm', 'archive', 'assign', 'mark_late', 'request_revision', 'record']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': 'submitted'}, 'confirm': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': 'confirmed'}, 'archive': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': 'archived'}, 'assign': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': None}, 'mark_late': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': None}, 'request_revision': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': None}, 'record': {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': None}}

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
