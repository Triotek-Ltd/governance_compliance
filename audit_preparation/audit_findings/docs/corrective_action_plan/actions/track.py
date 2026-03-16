"""Action handler seed for corrective_action_plan:track."""

from __future__ import annotations


DOC_ID = "corrective_action_plan"
ACTION_ID = "track"
ACTION_RULE = {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['audit_finding'], 'borrowed_fields': ['severity', 'recommendation from audit_finding'], 'inferred_roles': ['auditor']}, 'actors': ['auditor'], 'action_actors': {'create': ['auditor'], 'assign': ['auditor'], 'track': ['auditor'], 'close': ['auditor']}}

def handle_track(payload: dict, context: dict | None = None) -> dict:
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
