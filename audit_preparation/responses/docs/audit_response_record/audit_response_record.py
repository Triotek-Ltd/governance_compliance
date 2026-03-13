"""Doc runtime hooks for audit_response_record."""

class DocRuntime:
    doc_key = "audit_response_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'view', 'archive']
