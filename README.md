# devtools-webhook-cicd-utils

[![PyPI version](https://img.shields.io/pypi/v/devtools-webhook-cicd-utils.svg)](https://pypi.org/project/devtools-webhook-cicd-utils/)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Lightweight webhook integration utilities for modern CI/CD pipelines. Provides async event dispatching, payload validation, and retry logic for GitHub Actions, GitLab CI, and Jenkins.

## Installation

```bash
pip install devtools-webhook-cicd-utils
```

Or install from source:

```bash
pip install git+https://github.com/inowocil11-rgb/devtools-webhook-cicd-utils.git
```

## Quick Start

```python
from devtools_webhook import WebhookHandler

handler = WebhookHandler(secret="your-webhook-secret")

# Validate incoming webhook
is_valid = handler.validate(payload, signature=request.headers.get("X-Hub-Signature-256"))

# Parse event
event = handler.parse_event(payload)
print(f"Event: {event['event']} from {event['repo']}")
```

## Features

- **Webhook Validation** — HMAC-SHA256 signature verification for GitHub, GitLab, Bitbucket
- **Event Parsing** — Unified event model across CI/CD platforms
- **Retry Logic** — Configurable exponential backoff for webhook delivery
- **TLS Helpers** — Certificate pinning and custom CA support
- **Async Support** — Native asyncio integration for high-throughput pipelines

## Supported Platforms

| Platform | Webhooks | Status Checks | Deployment Events |
|----------|----------|---------------|-------------------|
| GitHub Actions | ✅ | ✅ | ✅ |
| GitLab CI | ✅ | ✅ | ✅ |
| Jenkins | ✅ | ✅ | ⬚ |
| Bitbucket Pipelines | ✅ | ⬚ | ⬚ |

## Configuration

```python
from devtools_webhook import WebhookHandler

handler = WebhookHandler(
    secret="your-secret",
    verify_ssl=True,
)
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
