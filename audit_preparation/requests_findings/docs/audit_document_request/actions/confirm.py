"""Action handler seed for audit_document_request:confirm."""

from __future__ import annotations


DOC_ID = "audit_document_request"
ACTION_ID = "confirm"
ACTION_RULE = {'allowed_in_states': ['open', 'requested', 'provided'], 'transitions_to': 'closed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Track evidence and document requests issued as part of audit preparation.', 'actors': ['audit coordinator', 'request owner', 'responder'], 'primary_transitions': ['audit_document_request: open -> requested -> provided -> closed']}

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
