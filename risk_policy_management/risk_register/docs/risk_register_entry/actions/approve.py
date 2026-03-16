"""Action handler seed for risk_register_entry:approve."""

from __future__ import annotations


DOC_ID = "risk_register_entry"
ACTION_ID = "approve"
ACTION_RULE = {'allowed_in_states': ['open', 'mitigated'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'record risks, monitor treatment actions, and maintain policy updates in response to control needs', 'actors': ['risk owner', 'policy owner', 'reviewer'], 'start_condition': 'a risk or policy issue is identified', 'ordered_steps': ['Record the identified risk or policy trigger.'], 'primary_actions': ['create', 'review'], 'primary_transitions': ['risk_register_entry: draft -> active'], 'downstream_effects': ['supports compliance, audit, and business-law controls'], 'action_actors': {'create': ['risk owner'], 'review': ['reviewer'], 'approve': ['reviewer'], 'close': ['risk owner'], 'archive': ['risk owner']}}

def handle_approve(payload: dict, context: dict | None = None) -> dict:
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
