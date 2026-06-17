import re
from dataclasses import dataclass


_MENTION_RE = re.compile(r"<@([A-Z0-9]+)>")


@dataclass(frozen=True)
class RoastRequest:
    target_user_ids: list[str]
    prompt: str


def parse_slack_mentions(text: str) -> list[str]:
    return _MENTION_RE.findall(text or "")


def strip_slack_mentions(text: str) -> str:
    text = _MENTION_RE.sub("", text or "")
    return re.sub(r"\s+", " ", text).strip()


def build_roast_request(text: str, teller_user_id: str, bot_user_id: str = "") -> RoastRequest:
    target_ids = [
        uid for uid in parse_slack_mentions(text)
        if uid and uid != bot_user_id
    ]
    if not target_ids:
        target_ids = [teller_user_id]

    clean_prompt = strip_slack_mentions(text)
    if bot_user_id:
        clean_prompt = re.sub(r"\bfusbot\b", "", clean_prompt, flags=re.IGNORECASE)
        clean_prompt = re.sub(r"\s+", " ", clean_prompt).strip()

    target_list = ", ".join(f"<@{uid}>" for uid in target_ids)
    target_is_teller = target_ids == [teller_user_id]
    target_guard = (
        "The requester is the target."
        if target_is_teller
        else "Do not roast the requester; roast only the listed target user(s)."
    )
    if clean_prompt:
        prompt = f"Roast the target user(s): {target_list}. {target_guard} Request context: {clean_prompt}"
    else:
        prompt = f"Roast the target user(s): {target_list}. {target_guard}"
    return RoastRequest(target_user_ids=target_ids, prompt=prompt)


def allowed_in_workspace_channel(
    team_id: str,
    enterprise_id: str,
    channel_id: str,
    allowed_workspace_id: str,
    allowed_channel_id: str,
) -> bool:
    if not allowed_workspace_id or not allowed_channel_id:
        return True
    in_workspace = enterprise_id == allowed_workspace_id or team_id == allowed_workspace_id
    return not in_workspace or channel_id == allowed_channel_id
