"""Doc runtime hooks for legal_agreement."""

class DocRuntime:
    doc_key = "legal_agreement"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'submit', 'approve', 'issue', 'renew', 'archive', 'route', 'request_revision', 'execute', 'expire']
