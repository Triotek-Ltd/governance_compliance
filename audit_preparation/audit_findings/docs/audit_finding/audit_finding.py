"""Doc runtime hooks for audit_finding."""

class DocRuntime:
    doc_key = "audit_finding"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'confirm', 'close', 'archive']
