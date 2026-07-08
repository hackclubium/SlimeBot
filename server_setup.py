import datetime

from economy_shared import state, save_state


def setup_root():
    return state.setdefault("server_setup_v2", {})


def workspace_setup_data():
    root = setup_root()
    key = "workspace"
    if key not in root:
        root[key] = {
            "onboarding_channel_id": None,
            "tips_enabled": True,
            "last_posted_at": None,
            "created_at": datetime.datetime.utcnow().isoformat(),
        }
        save_state()
    return root[key]


def onboarding_text(config: dict) -> str:
    tips_section = ""
    if config.get("tips_enabled", True):
        tips_section = "\n\n*Starter Tip:* new people should try `/slime_profile`, `/slime_daily`, `/slime_work`, and `/slime_help adventure` first"
    return (
        ":wave: *welcome to slimebot*\n"
        "this bot does a lot, so here's the clean starting point before you mash `/` and get lost\n\n"
        "*Start Here:*\n"
        "`/slime_help start` for the beginner guide\n"
        "`/slime_profile` to see your account\n"
        "`/slime_balance` to check money\n"
        "`/slime_daily` and `/slime_work` to start earning\n\n"
        "*Best Starter Routes:*\n"
        "*money* — `/slime_daily` → `/slime_work` → `/slime_shop` or `/slime_stocks`\n"
        "*creatures* — `/slime_hunt` or `/slime_fish` → `/slime_team list` → `/slime_battle`\n"
        "*deep modes* — `/slime_dungeon` or `/slime_voidmaze` or `/slime_arena`\n"
        "*ai* — `/slime_roast` or `/code_list` → `/slime_hack`\n\n"
        "*Need More Help?*\n"
        "`/slime_help economy` `/slime_help adventure` `/slime_help deep` `/slime_help ai` `/slime_help fun`"
        + tips_section
    )


def setup_view_text(config: dict) -> str:
    channel_text = f"<#{config['onboarding_channel_id']}>" if config.get("onboarding_channel_id") else "not set"
    return (
        ":wrench: *slimebot Workspace Setup*\n\n"
        f"onboarding channel: {channel_text}\n"
        f"tips enabled: `{'yes' if config.get('tips_enabled', True) else 'no'}`\n"
        f"last onboarding post: `{config.get('last_posted_at') or 'never'}`\n\n"
        "*Recommended Flow:*\n"
        "1. run `/slime_setup channel <channel_id>`\n"
        "2. run `/slime_setup post`\n"
        "3. test `/slime_help start`\n"
        "4. optionally configure automod\n\n"
        "*Useful Admin Commands:*\n"
        "`/slime_setup view` `/slime_setup channel` `/slime_setup tips` `/slime_setup post` `/slime_setup reset`"
    )


async def setup(app):

    @app.command("/slime_setup")
    async def setup_cmd(ack, command, client):
        await ack()
        uid = command["user_id"]; channel = command["channel_id"]
        parts = (command.get("text") or "").strip().split(None, 1)
        action = parts[0].lower() if parts else "view"
        arg = parts[1].strip() if len(parts) > 1 else ""

        if action in ("view", ""):
            config = workspace_setup_data()
            await client.chat_postEphemeral(channel=channel, user=uid, text=setup_view_text(config))

        elif action == "channel":
            if not arg:
                await client.chat_postEphemeral(channel=channel, user=uid, text="usage: `/slime_setup channel <channel_id>`"); return
            import re as re_mod
            m = re_mod.search(r"<#([A-Z0-9]+)>", arg)
            channel_id = m.group(1) if m else arg.strip()
            config = workspace_setup_data(); config["onboarding_channel_id"] = channel_id; save_state()
            await client.chat_postEphemeral(channel=channel, user=uid, text=f"onboarding channel set to <#{channel_id}>")

        elif action == "tips":
            val = arg.lower()
            if val not in ("on", "off", "true", "false", "1", "0", "yes", "no"):
                await client.chat_postEphemeral(channel=channel, user=uid, text="usage: `/slime_setup tips on` or `/slime_setup tips off`"); return
            enabled = val in ("on", "true", "1", "yes")
            config = workspace_setup_data(); config["tips_enabled"] = enabled; save_state()
            await client.chat_postEphemeral(channel=channel, user=uid, text=f"onboarding tips are now `{'on' if enabled else 'off'}`")

        elif action == "post":
            config = workspace_setup_data()
            target_channel = config.get("onboarding_channel_id") or channel
            text = onboarding_text(config)
            await client.chat_postMessage(channel=target_channel, text=text)
            config["last_posted_at"] = datetime.datetime.utcnow().isoformat(); save_state()
            notice = "posted the onboarding guide here" if target_channel == channel else f"posted the onboarding guide in <#{target_channel}>"
            await client.chat_postEphemeral(channel=channel, user=uid, text=notice)

        elif action == "reset":
            root = setup_root(); root.pop("workspace", None); save_state()
            await client.chat_postEphemeral(channel=channel, user=uid, text="workspace setup data reset")

        else:
            await client.chat_postEphemeral(channel=channel, user=uid, text="actions: `view` | `channel <id>` | `tips on|off` | `post` | `reset`")
