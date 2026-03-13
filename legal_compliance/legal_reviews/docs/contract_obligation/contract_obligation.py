"""Doc runtime hooks for contract_obligation."""

class DocRuntime:
    doc_key = "contract_obligation"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'track', 'close', 'archive']
