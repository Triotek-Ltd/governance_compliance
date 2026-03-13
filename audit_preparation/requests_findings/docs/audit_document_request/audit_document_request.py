"""Doc runtime hooks for audit_document_request."""

class DocRuntime:
    doc_key = "audit_document_request"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'confirm', 'close']
