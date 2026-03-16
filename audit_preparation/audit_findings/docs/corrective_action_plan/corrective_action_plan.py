"""Doc runtime hooks for corrective_action_plan."""

class DocRuntime:
    doc_key = "corrective_action_plan"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'track', 'close']
