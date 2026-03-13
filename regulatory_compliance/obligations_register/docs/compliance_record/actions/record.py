"""Action handler seed for compliance_record:record."""

from __future__ import annotations


DOC_ID = "compliance_record"
ACTION_ID = "record"
ACTION_RULE = {'allowed_in_states': 'active', 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Maintain the evidence trail for ongoing compliance against defined obligations.', 'actors': ['compliance officer', 'owner'], 'primary_transitions': ['compliance_record: active -> archived']}

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
