"""Doc runtime hooks for corporate_register_entry."""

class DocRuntime:
    doc_key = "corporate_register_entry"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
