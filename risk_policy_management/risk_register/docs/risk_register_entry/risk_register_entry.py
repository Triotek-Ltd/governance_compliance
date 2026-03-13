"""Doc runtime hooks for risk_register_entry."""

class DocRuntime:
    doc_key = "risk_register_entry"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
