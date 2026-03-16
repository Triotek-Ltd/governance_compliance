"""Action handler seed for submission_confirmation:record."""

from __future__ import annotations


DOC_ID = "submission_confirmation"
ACTION_ID = "record"
ACTION_RULE = {'allowed_in_states': ['active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['regulatory_filing'], 'borrowed_fields': ['filing type', 'authority', 'submission date from regulatory_filing'], 'inferred_roles': ['compliance officer']}, 'actors': ['compliance officer'], 'action_actors': {'record': ['compliance officer'], 'archive': ['compliance officer']}}

def handle_record(payload: dict, context: dict | None = None) -> dict:
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
