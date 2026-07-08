import json
import os

import requests


def _redis_command(*parts):
    url = os.getenv("UPSTASH_REDIS_REST_URL")
    token = os.getenv("UPSTASH_REDIS_REST_TOKEN")
    if not url or not token:
        return None
    # ponytail: blocking call — matches the sync save_state() call sites it replaces
    # (they already blocked on disk I/O). Switch to aiohttp if this becomes a bottleneck.
    r = requests.post(url.rstrip("/"), headers={"Authorization": f"Bearer {token}"}, json=list(parts), timeout=5)
    r.raise_for_status()
    return r.json().get("result")


def redis_get_json(key, default):
    try:
        raw = _redis_command("GET", key)
        return json.loads(raw) if raw else default
    except Exception:
        return default


def redis_set_json(key, value):
    try:
        _redis_command("SET", key, json.dumps(value))
    except Exception:
        pass
