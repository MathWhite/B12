import json
import hmac
import hashlib
import os
from datetime import datetime, timezone

import requests

SIGNING_SECRET = "hello-there-from-b12"

payload = {
    "action_run_link": os.environ["ACTION_RUN_LINK"],
    "email": "matheusfgc99@gmail.com",
    "name": "Matheus Francisco Garcia de Carvalho",
    "repository_link": "https://github.com/MathWhite/B12",
    "resume_link": "https://mc-dev.tech/",
    "timestamp": datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z"),
}

# Canonical JSON:
# - compact separators
# - sorted keys
# - UTF-8 encoded
body = json.dumps(
    payload,
    separators=(",", ":"),
    sort_keys=True,
    ensure_ascii=False,
).encode("utf-8")

signature = hmac.new(
    SIGNING_SECRET.encode("utf-8"),
    body,
    hashlib.sha256,
).hexdigest()

headers = {
    "Content-Type": "application/json",
    "X-Signature-256": f"sha256={signature}",
}

response = requests.post(
    "https://b12.io/apply/submission",
    data=body,
    headers=headers,
    timeout=30,
)

response.raise_for_status()

data = response.json()

print("Submission successful!")
print("Receipt:", data["receipt"])
