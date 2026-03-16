"""Action handler seed for regulatory_obligation:create."""

from __future__ import annotations


DOC_ID = "regulatory_obligation"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'track obligations, prepare filings, submit them, and retain submission evidence', 'actors': ['compliance officer', 'preparer', 'approver', 'regulator-facing submitter'], 'start_condition': 'a regulatory obligation or due date becomes actionable', 'ordered_steps': ['Identify the applicable obligation and due date.'], 'primary_actions': ['create', 'update', 'record'], 'primary_transitions': [], 'downstream_effects': ['compliance history becomes available to audit, legal, risk, and reporting flows'], 'action_actors': {'create': ['compliance officer'], 'update': ['compliance officer'], 'archive': ['compliance officer']}}

def handle_create(payload: dict, context: dict | None = None) -> dict:
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
