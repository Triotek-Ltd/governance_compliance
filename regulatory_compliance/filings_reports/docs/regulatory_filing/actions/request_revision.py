"""Action handler seed for regulatory_filing:request_revision."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "regulatory_filing"
ACTION_ID = "request_revision"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'submitted', 'confirmed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'track obligations, prepare filings, submit them, and retain submission evidence', 'actors': ['compliance officer', 'preparer', 'approver', 'regulator-facing submitter'], 'start_condition': 'a regulatory obligation or due date becomes actionable', 'ordered_steps': ['Create the filing record for the reporting period or event.', 'Prepare submission content and supporting documents.', 'Submit and confirm the filing.', 'Mark lateness, issues, or revisions if necessary.', 'Archive the completed regulatory record set.'], 'primary_actions': ['create', 'assign', 'review', 'record', 'request_revision', 'submit', 'confirm', 'mark_late', 'archive'], 'primary_transitions': ['regulatory_filing: draft', 'regulatory_filing: draft -> submitted -> confirmed'], 'downstream_effects': ['compliance history becomes available to audit, legal, risk, and reporting flows'], 'action_actors': {'create': ['compliance officer'], 'review': ['preparer'], 'submit': ['compliance officer'], 'confirm': ['approver'], 'archive': ['compliance officer'], 'assign': ['compliance officer'], 'record': ['compliance officer']}}

def handle_request_revision(payload: dict, context: dict | None = None) -> dict:
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
