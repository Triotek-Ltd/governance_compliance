"""Doc runtime hooks for corporate_access_request."""

class DocRuntime:
    doc_key = "corporate_access_request"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'approve', 'close', 'archive']
