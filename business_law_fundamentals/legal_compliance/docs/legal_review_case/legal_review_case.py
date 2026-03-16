"""Doc runtime hooks for legal_review_case."""

class DocRuntime:
    doc_key = "legal_review_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'close']
