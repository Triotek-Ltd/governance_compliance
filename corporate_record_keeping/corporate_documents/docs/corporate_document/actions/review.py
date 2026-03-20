"""Action handler seed for corporate_document:review."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "corporate_document"
ACTION_ID = "review"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'preserve formal corporate records, track them in registers, and govern access and retention', 'actors': ['governance officer', 'custodian', 'approver'], 'start_condition': 'a corporate legal or governance document must be retained', 'ordered_steps': ['Capture the corporate document and classify it.', 'Apply retention and retention-hold controls.'], 'primary_actions': ['create', 'classify', 'review', 'update', 'archive'], 'primary_transitions': ['corporate_document: draft -> active'], 'downstream_effects': ['supports legal, audit, and regulatory controls'], 'action_actors': {'create': ['governance officer'], 'review': ['custodian'], 'archive': ['governance officer']}}

def handle_review(payload: dict, context: dict | None = None) -> dict:
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
