"""DevTools Webhook CICD Utilities"""

__version__ = "1.6.0"

class WebhookHandler:
    """Handle webhook events from CI/CD pipelines."""
    def __init__(self, secret=None, verify_ssl=True):
        self.secret = secret
        self.verify_ssl = verify_ssl

    def validate(self, payload, signature=None):
        """Validate webhook payload signature."""
        if not self.secret:
            return True
        import hmac, hashlib
        expected = hmac.new(
            self.secret.encode(), payload.encode(), hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(expected, signature or "")

    def parse_event(self, payload):
        """Parse webhook event payload."""
        import json
        if isinstance(payload, str):
            payload = json.loads(payload)
        return {"event": payload.get("action", "unknown"),
                "repo": payload.get("repository", {}).get("full_name", ""),
                "sender": payload.get("sender", {}).get("login", "")}
