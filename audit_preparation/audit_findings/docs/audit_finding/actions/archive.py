"""Action handler seed for audit_finding:archive."""

from __future__ import annotations


DOC_ID = "audit_finding"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['open', 'confirmed', 'resolved'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'prepare evidence and responses for audit activity, then track findings to remediation closure', 'actors': ['audit coordinator', 'requester', 'finding owner', 'reviewer'], 'start_condition': 'an internal or external audit cycle begins', 'ordered_steps': ['Record findings and remediate them through action items.'], 'primary_actions': ['create', 'assign', 'track', 'verify', 'close'], 'primary_transitions': ['audit_finding: opened -> in_review -> resolved -> closed'], 'downstream_effects': ['supports governance assurance and remediation tracking', 'consulting explanations', 'implementation planning', 'user guides', 'demo narratives'], 'action_actors': {'create': ['audit coordinator'], 'review': ['reviewer'], 'confirm': ['reviewer'], 'close': ['finding owner'], 'archive': ['finding owner']}}

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
