"""Doc runtime hooks for compliance_record."""

class DocRuntime:
    doc_key = "compliance_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
