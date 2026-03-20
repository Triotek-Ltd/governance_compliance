"""Action registry seed for policy_document."""

from __future__ import annotations

from typing import Any


DOC_ID = "policy_document"
ALLOWED_ACTIONS = ['create', 'submit', 'approve', 'publish', 'archive']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'approved'}, 'approve': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'approved'}, 'publish': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'published'}, 'archive': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'archived'}}

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
