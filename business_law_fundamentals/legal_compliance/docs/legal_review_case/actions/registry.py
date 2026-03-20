"""Action registry seed for legal_review_case."""

from __future__ import annotations

from typing import Any


DOC_ID = "legal_review_case"
ALLOWED_ACTIONS = ['create', 'assign', 'review', 'close']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['open', 'in_review'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['open', 'in_review'], 'transitions_to': 'in_review'}, 'review': {'allowed_in_states': ['open', 'in_review'], 'transitions_to': 'in_review'}, 'close': {'allowed_in_states': ['open', 'in_review'], 'transitions_to': 'closed'}}

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
