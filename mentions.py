import re

SLIMEBOT_ALIASES = {
    "slimebot",
    "slime bot",
    "@slimebot",
    "slime-bot",
    "slime_bot",
    "slimeboi",
    "slimeb0t",
    "slime-b0t",
    "SLIMEBOT",
    "SliMeBot",
    "slimeyslimeyslime",
    "@slimeyslimeyslime",
}

_ALIAS_PATTERNS = [
    re.compile(rf"\b{re.escape(a)}\b", re.IGNORECASE)
    for a in SLIMEBOT_ALIASES
]

def mentions_slimebot(text: str) -> bool:
    if not text:
        return False
    return any(p.search(text) for p in _ALIAS_PATTERNS)
