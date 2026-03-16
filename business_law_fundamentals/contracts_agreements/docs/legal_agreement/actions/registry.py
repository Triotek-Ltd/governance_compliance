"""Action registry seed for legal_agreement."""

from __future__ import annotations


DOC_ID = "legal_agreement"
ALLOWED_ACTIONS = ['create', 'review', 'submit', 'approve', 'issue', 'renew', 'archive', 'route', 'request_revision', 'execute', 'expire']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': 'approved'}, 'approve': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': 'approved'}, 'issue': {'allowed_in_states': ['approved'], 'transitions_to': 'executed'}, 'renew': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': 'renewed'}, 'archive': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': 'archived'}, 'route': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': None}, 'request_revision': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': None}, 'execute': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': None}, 'expire': {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': None}}

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
