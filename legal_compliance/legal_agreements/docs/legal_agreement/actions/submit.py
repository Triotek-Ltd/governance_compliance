"""Action handler seed for legal_agreement:submit."""

from __future__ import annotations


DOC_ID = "legal_agreement"
ACTION_ID = "submit"
ACTION_RULE = {'allowed_in_states': ['draft', 'approved', 'executed', 'expired', 'renewed'], 'transitions_to': 'approved'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Track legal agreements through drafting, approval, execution, and renewal or closure.', 'actors': ['legal officer', 'approver', 'business owner'], 'primary_transitions': ['legal_agreement: draft -> approved -> executed', 'legal_agreement: executed -> renewed or expired -> archived']}

def handle_submit(payload: dict, context: dict | None = None) -> dict:
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
