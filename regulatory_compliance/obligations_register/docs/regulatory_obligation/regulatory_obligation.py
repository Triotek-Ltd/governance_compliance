"""Doc runtime hooks for regulatory_obligation."""

class DocRuntime:
    doc_key = "regulatory_obligation"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'archive']
