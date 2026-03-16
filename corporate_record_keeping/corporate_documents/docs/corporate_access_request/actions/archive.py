"""Action handler seed for corporate_access_request:archive."""

from __future__ import annotations


DOC_ID = "corporate_access_request"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['open', 'approved'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'preserve formal corporate records, track them in registers, and govern access and retention', 'actors': ['governance officer', 'custodian', 'approver'], 'start_condition': 'a corporate legal or governance document must be retained', 'ordered_steps': ['Control document access requests.'], 'primary_actions': ['create', 'submit', 'approve', 'close'], 'primary_transitions': ['corporate_access_request: draft -> in_review -> approved -> closed'], 'downstream_effects': ['supports legal, audit, and regulatory controls'], 'action_actors': {'create': ['governance officer'], 'approve': ['approver'], 'close': ['governance officer'], 'archive': ['governance officer']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
