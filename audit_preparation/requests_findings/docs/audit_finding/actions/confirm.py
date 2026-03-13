"""Action handler seed for audit_finding:confirm."""

from __future__ import annotations


DOC_ID = "audit_finding"
ACTION_ID = "confirm"
ACTION_RULE = {'allowed_in_states': ['open', 'confirmed', 'resolved'], 'transitions_to': 'confirmed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Track issues identified during audit work until confirmation and resolution.', 'actors': ['audit coordinator', 'reviewer', 'owner'], 'primary_transitions': ['audit_finding: open -> confirmed -> resolved -> closed -> archived']}

def handle_confirm(payload: dict, context: dict | None = None) -> dict:
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
