"""Action handler seed for regulatory_filing:submit."""

from __future__ import annotations


DOC_ID = "regulatory_filing"
ACTION_ID = "submit"
ACTION_RULE = {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': 'submitted'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Track required submissions against live regulatory obligations and their reporting periods.', 'actors': ['compliance officer', 'report owner'], 'primary_transitions': ['regulatory_filing: draft -> submitted -> confirmed -> archived']}

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
