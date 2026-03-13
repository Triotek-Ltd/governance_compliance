"""Doc runtime hooks for submission_confirmation."""

class DocRuntime:
    doc_key = "submission_confirmation"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'view', 'archive']
