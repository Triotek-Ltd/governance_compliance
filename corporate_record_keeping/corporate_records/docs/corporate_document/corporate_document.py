"""Doc runtime hooks for corporate_document."""

class DocRuntime:
    doc_key = "corporate_document"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'archive']
