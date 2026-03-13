"""Action handler seed for corrective_action_plan:assign."""

from __future__ import annotations


DOC_ID = "corrective_action_plan"
ACTION_ID = "assign"
ACTION_RULE = {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': 'in_progress'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Track planned remediation work for audit findings until closure.', 'actors': ['action owner', 'audit coordinator'], 'primary_transitions': ['corrective_action_plan: open -> in_progress -> closed -> archived']}

def handle_assign(payload: dict, context: dict | None = None) -> dict:
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
