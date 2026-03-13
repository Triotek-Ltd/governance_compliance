"""Doc runtime hooks for mitigation_plan."""

class DocRuntime:
    doc_key = "mitigation_plan"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'track', 'close']
