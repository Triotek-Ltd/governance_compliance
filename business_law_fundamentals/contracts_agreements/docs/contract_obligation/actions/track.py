"""Action handler seed for contract_obligation:track."""

from __future__ import annotations


DOC_ID = "contract_obligation"
ACTION_ID = "track"
ACTION_RULE = {'allowed_in_states': ['open', 'in_progress', 'fulfilled'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['legal_agreement'], 'borrowed_fields': ['dates', 'parties', 'agreement type from legal_agreement'], 'inferred_roles': ['compliance officer']}, 'actors': ['compliance officer'], 'action_actors': {'create': ['compliance officer'], 'assign': ['compliance officer'], 'track': ['compliance officer'], 'close': ['compliance officer'], 'archive': ['compliance officer']}}

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
