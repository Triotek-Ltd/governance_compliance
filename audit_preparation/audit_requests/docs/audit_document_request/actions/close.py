"""Action handler seed for audit_document_request:close."""

from __future__ import annotations


DOC_ID = "audit_document_request"
ACTION_ID = "close"
ACTION_RULE = {'allowed_in_states': ['open', 'requested', 'provided'], 'transitions_to': 'closed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['audit_engagement'], 'borrowed_fields': ['engagement title', 'business area', 'requester from audit_engagement'], 'inferred_roles': ['auditor']}, 'actors': ['auditor'], 'action_actors': {'create': ['auditor'], 'assign': ['auditor'], 'confirm': ['auditor'], 'close': ['auditor']}}

def handle_close(payload: dict, context: dict | None = None) -> dict:
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
