"""Action handler seed for corporate_document:review."""

from __future__ import annotations


DOC_ID = "corporate_document"
ACTION_ID = "review"
ACTION_RULE = {'allowed_in_states': ['draft', 'active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Maintain the master record for legal and corporate governance documents.', 'actors': ['corporate secretary', 'compliance officer'], 'primary_transitions': ['corporate_document: draft -> active -> archived']}

def handle_review(payload: dict, context: dict | None = None) -> dict:
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
