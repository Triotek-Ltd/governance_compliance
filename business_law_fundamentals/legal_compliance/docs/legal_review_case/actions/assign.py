"""Action handler seed for legal_review_case:assign."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "legal_review_case"
ACTION_ID = "assign"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['open', 'in_review'], 'transitions_to': 'in_review'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['legal_agreement'], 'borrowed_fields': ['agreement type', 'counterparty', 'routing status from legal_agreement'], 'inferred_roles': ['compliance officer', 'case owner']}, 'actors': ['compliance officer', 'case owner'], 'action_actors': {'create': ['compliance officer'], 'assign': ['compliance officer'], 'review': ['case owner'], 'close': ['case owner']}}

def handle_assign(payload: dict, context: dict | None = None) -> dict:
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
