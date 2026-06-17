import datetime
from slack_utils import header_block, section_block, divider_block, context_block

TOPIC_ALIASES = {
    "start": "start", "beginner": "start", "new": "start", "getting started": "start", "getting-started": "start",
    "economy": "economy", "money": "economy", "cash": "economy",
    "adventure": "adventure", "games": "adventure", "combat": "adventure", "grind": "adventure",
    "deep": "deep", "systems": "deep",
    "ai": "ai", "roast": "ai", "code": "ai", "hack": "ai",
    "admin": "admin", "setup": "admin", "mod": "admin", "moderation": "admin",
    "fun": "fun", "misc": "fun", "extras": "fun",
    "all": "all",
}


def normalize_topic(topic: str | None) -> str:
    text = (topic or "start").strip().lower()
    return TOPIC_ALIASES.get(text, "start")


def make_blocks(topic: str, user_id: str) -> list[dict]:
    topic = normalize_topic(topic)

    if topic == "economy":
        return [
            header_block("help • economy"),
            section_block("money, items, stocks, trading, and progression basics"),
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Core Money*\n`/fus_balance` see your horsenncy\n`/fus_daily` claim free money\n`/fus_recommend` get your best next move\n`/fus_work` do jobs\n`/fus_give` send money to someone\n`/fus_pray` gain prayer points\n`/fus_leaderboard` richest players"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Risk and Gambling*\n`/fus_blackjack`\n`/fus_coinflip`\n`/fus_crime`\n`/fus_slots`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Items, Market, and Player Trading*\n`/fus_shop`\n`/fus_buy`\n`/fus_inventory`\n`/fus_use`\n`/fus_stocks` — `/fus_stocks buy SYMBOL amount` or `/fus_stocks sell SYMBOL amount`\n`/fus_auction browse`\n`/fus_auction sell`\n`/fus_auction buy`"}},
            context_block("easy starter route: /fus_daily → /fus_work → /fus_shop or /fus_stocks"),
        ]

    if topic == "adventure":
        return [
            header_block("help • adventure"),
            section_block("creatures, teams, combat, and your core grinding routes"),
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Creature Loop*\n`/fus_hunt` get creatures\n`/fus_fish` get fish and sea monsters\n`/fus_team list` see your team\n`/fus_team add` add a creature\n`/fus_team remove` remove one\n`/fus_battle` fight monsters"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Big Progression Modes*\n`/fus_dungeon` evolving dungeon run\n`/fus_voidmaze` cosmic roguelite\n`/fus_arena` auto-battler ladder\n`/fus_lab` research lab"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Account and Progress Tracking*\n`/fus_profile`\n`/fus_profile achievements`\n`/fus_profile collections`\n`/fus_recommend`\n`/fus_quests`\n`/fus_titles`"}},
            context_block("easy starter route: /fus_hunt or /fus_fish → /fus_team list → /fus_battle → /fus_dungeon"),
        ]

    if topic == "deep":
        return [
            header_block("help • deep systems"),
            section_block("the heavier systems once you want more than quick commands"),
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Account Layer*\n`/fus_profile` overview\n`/fus_profile achievements` unlock board\n`/fus_quests` daily goals\n`/fus_quests claim <slot>` claim rewards\n`/fus_titles` unlocked titles\n`/fus_titles equip <title>` equip a title\n`/fus_profile collections` account-wide collection progress"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Social Layer*\n`/fus_guild create`\n`/fus_guild join`\n`/fus_guild leave`\n`/fus_guild info`\n`/fus_guild deposit`\n`/fus_guild upgrade`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*High-Depth Modes*\n`/fus_dungeon`\n`/fus_voidmaze`\n`/fus_arena`\n`/fus_lab`\n`/fus_hack`"}},
            context_block("this is the layer that ties the rest of the bot together"),
        ]

    if topic == "ai":
        return [
            header_block("help • ai and utility"),
            section_block("roast ai, codepad, hacking, images, and lichess"),
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Roast AI*\n`/fus_roast`\n`/fus_data`\n`/fus_autor`\n`/fus_roastmode fast|deep|adjustable|off`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Codepad and Hacking*\n`/fus_code new <file>`\n`/fus_code edit <file>`\n`/fus_code view <file>`\n`/fus_code list`\n`/fus_code delete <file>`\n`/fus_code run <file>`\n`/fus_hack <target>`\n`/fus_hack chaos <target>`\n`/fus_hack profile`\n`/fus_hack targets`\n`/fus_hack state`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Other AI*\n`/fus_img <prompt>`"}},
            context_block("good starter route: /fus_roast or /fus_code list"),
        ]

    if topic == "admin":
        return [
            header_block("help • admin"),
            section_block("server onboarding and moderation tools"),
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Server Setup*\n`/fus_setup view`\n`/fus_setup channel`\n`/fus_setup tips`\n`/fus_setup post`\n`/fus_setup reset`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*AutoMod*\n`/fus_automod` — view settings\n`/fus_automod on|off`\n`/fus_automod reset @user`\n`/fus_automod punishment`\n`/fus_automod slurs`\n`/fus_automod spam`\n`/fus_automod filters`\n`/fus_automod settings`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Recommended Order*\n1. run `/fus_setup channel`\n2. run `/fus_setup post`\n3. run `/fus_help start` yourself and check the flow\n4. turn on automod only if you want it"}},
            context_block("admins should start with /fus_setup view"),
        ]

    if topic == "fun":
        return [
            header_block("help • fun and extras"),
            section_block("side commands, casual stuff, and social commands"),
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Casual Commands*\n`/fus_afk`\n`/fus_animal`\n`/fus_badge`\n`/fus_emojimixup`\n`/fus_aki`\n`/fus_img`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Interactive Games*\n`/fus_battleship` — start a game\n`/fus_bs place|fire|status|forfeit|resume|stats|leaderboard`\n`/fus_monopoly start|stop|resume`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Extra Builders*\n`/fus_rave`\n`/fus_rave bg <key>`"}},
            context_block("these are the side dishes, not the main grind"),
        ]

    if topic == "all":
        return [
            header_block("help • topic map"),
            section_block("use `/fus_help <topic>` with one of these categories"),
            {"type": "section", "fields": [
                {"type": "mrkdwn", "text": "*Topics*\n`start`\n`economy`\n`adventure`\n`deep`\n`ai`\n`admin`\n`fun`\n`all`"},
                {"type": "mrkdwn", "text": "*Fast Examples*\n`/fus_help start`\n`/fus_help economy`\n`/fus_help adventure`\n`/fus_help deep`\n`/fus_help ai`\n`/fus_help admin`\n`/fus_help fun`"},
            ]},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Best New User Route*\n`/fus_profile` → `/fus_recommend` → `/fus_daily` → `/fus_work` → `/fus_help economy` → `/fus_help adventure`"}},
            context_block("start with /fus_help start if you're new"),
        ]

    return [
        header_block("help • getting started"),
        section_block(f"hey <@{user_id}>, this bot does a lot — here's the clean way to start without staring at the slash menu."),
        {"type": "section", "text": {"type": "mrkdwn", "text": "*First Commands to Try*\n`/fus_profile` see your account\n`/fus_balance` check your money\n`/fus_recommend` or `/fus_recommend` get your best next move\n`/fus_daily` claim free horsenncy\n`/fus_work` earn more\n`/fus_help economy` or `/fus_help adventure`"}},
        {"type": "section", "text": {"type": "mrkdwn", "text": "*Popular Routes*\n*money route* — `/fus_daily` → `/fus_work` → `/fus_shop` or `/fus_stocks`\n*creature route* — `/fus_hunt` or `/fus_fish` → `/fus_team list` → `/fus_battle`\n*deep route* — `/fus_dungeon` or `/fus_voidmaze` or `/fus_arena`\n*ai route* — `/fus_roast` or `/fus_code list` → `/fus_hack`\n*stuck?* — `/fus_recommend` or `/fus_recommend`"}},
        {"type": "section", "text": {"type": "mrkdwn", "text": "*Help Topics*\n`/fus_help economy`\n`/fus_help adventure`\n`/fus_help deep`\n`/fus_help ai`\n`/fus_help admin`\n`/fus_help fun`"}},
    ]


STARTER_ROUTES = {
    "money": {
        "title": "money route",
        "desc": "fast start for economy and progression",
        "steps": ["/fus_profile", "/fus_recommend", "/fus_daily", "/fus_work", "/fus_recommend", "/fus_shop", "/fus_help economy"],
    },
    "battle": {
        "title": "battle route",
        "desc": "build a team and start fighting things",
        "steps": ["/fus_profile", "/fus_recommend", "/fus_hunt", "/fus_team list", "/fus_battle", "/fus_recommend", "/fus_help adventure"],
    },
    "ai": {
        "title": "ai route",
        "desc": "jump into the bot's ai side first",
        "steps": ["/fus_recommend", "/fus_roast", "/fus_roastmode", "/fus_code list", "/fus_hack", "/fus_recommend", "/fus_help ai"],
    },
}


def make_start_blocks(route_key: str, user_id: str) -> list[dict]:
    if route_key == "home":
        return [
            header_block("start here"),
            section_block(f"hey <@{user_id}> — pick the path you want and i'll give you the fastest route"),
            {"type": "section", "text": {"type": "mrkdwn", "text": "*available paths*\n:moneybag: money\n:crossed_swords: battle\n:robot_face: ai"}},
            {"type": "actions", "block_id": "start_route", "elements": [
                {"type": "button", "text": {"type": "plain_text", "text": "money", "emoji": True}, "action_id": "start_money", "value": "money"},
                {"type": "button", "text": {"type": "plain_text", "text": "battle", "emoji": True}, "action_id": "start_battle", "value": "battle", "style": "danger"},
                {"type": "button", "text": {"type": "plain_text", "text": "ai", "emoji": True}, "action_id": "start_ai", "value": "ai", "style": "primary"},
            ]},
        ]
    data = STARTER_ROUTES[route_key]
    steps = "\n".join(f"{i+1}. `{step}`" for i, step in enumerate(data["steps"]))
    return [
        header_block(data["title"]),
        section_block(data["desc"]),
        {"type": "section", "text": {"type": "mrkdwn", "text": f"*do these in order*\n{steps}"}},
        context_block("finish this path first, then branch out"),
    ]


async def setup(app):
    @app.command("/fus_help")
    async def help_cmd(ack, command, respond):
        await ack()
        uid = command["user_id"]
        text = (command.get("text") or "").strip()
        if text.lower() == "start":
            blocks = make_start_blocks("home", uid)
            await respond(blocks=blocks, text="Start here")
        else:
            topic = text or None
            blocks = make_blocks(topic, uid)
            await respond(blocks=blocks, text="Help")

    async def _handle_start_route(ack, body, respond):
        await ack()
        uid = body["user"]["id"]
        route = body["actions"][0]["value"]
        if route not in STARTER_ROUTES:
            return
        blocks = make_start_blocks(route, uid)
        await respond(replace_original=True, blocks=blocks, text=STARTER_ROUTES[route]["title"])

    app.action("start_money")(_handle_start_route)
    app.action("start_battle")(_handle_start_route)
    app.action("start_ai")(_handle_start_route)
