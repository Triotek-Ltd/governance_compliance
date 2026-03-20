"""Action handler seed for audit_response_record:view."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "audit_response_record"
ACTION_ID = "view"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['audit_engagement'], 'borrowed_fields': ['engagement number', 'scope from audit_engagement'], 'inferred_roles': ['auditor']}, 'actors': ['auditor'], 'action_actors': {'record': ['auditor'], 'archive': ['auditor']}}

def handle_view(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
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
