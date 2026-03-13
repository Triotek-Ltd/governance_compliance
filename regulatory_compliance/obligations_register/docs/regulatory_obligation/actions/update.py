"""Action handler seed for regulatory_obligation:update."""

from __future__ import annotations


DOC_ID = "regulatory_obligation"
ACTION_ID = "update"
ACTION_RULE = {'allowed_in_states': 'active', 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Define the active regulatory duties that the institution must satisfy and monitor.', 'actors': ['compliance officer', 'owner'], 'primary_transitions': ['regulatory_obligation: active -> archived']}

def handle_update(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
