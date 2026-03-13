"""Doc runtime hooks for regulatory_filing."""

class DocRuntime:
    doc_key = "regulatory_filing"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'confirm', 'archive']
