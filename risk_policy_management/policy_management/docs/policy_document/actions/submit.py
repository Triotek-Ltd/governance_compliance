"""Action handler seed for policy_document:submit."""

from __future__ import annotations


DOC_ID = "policy_document"
ACTION_ID = "submit"
ACTION_RULE = {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'approved'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'draft and review legal agreements, then track the obligations they create', 'actors': ['legal reviewer', 'business owner', 'approver'], 'start_condition': 'a contract or legal obligation requires review', 'ordered_steps': [], 'primary_actions': [], 'primary_transitions': [], 'downstream_effects': ['supports legal compliance and obligation management'], 'action_actors': {'create': ['legal reviewer'], 'submit': ['legal reviewer'], 'approve': ['approver'], 'publish': ['business owner'], 'archive': ['business owner']}}

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
