"""Doc runtime hooks for policy_document."""

class DocRuntime:
    doc_key = "policy_document"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'approve', 'publish', 'archive']
