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
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Core Money*\n`/slime_balance` see your horsenncy\n`/slime_daily` claim free money\n`/slime_recommend` get your best next move\n`/slime_work` do jobs\n`/slime_give` send money to someone\n`/slime_pray` gain prayer points\n`/slime_leaderboard` richest players"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Risk and Gambling*\n`/slime_blackjack`\n`/slime_coinflip`\n`/slime_crime`\n`/slime_slots`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Items, Market, and Player Trading*\n`/slime_shop`\n`/slime_buy`\n`/slime_inventory`\n`/slime_use`\n`/slime_stocks` — `/slime_stocks buy SYMBOL amount` or `/slime_stocks sell SYMBOL amount`\n`/slime_auction browse`\n`/slime_auction sell`\n`/slime_auction buy`"}},
            context_block("easy starter route: /slime_daily → /slime_work → /slime_shop or /slime_stocks"),
        ]

    if topic == "adventure":
        return [
            header_block("help • adventure"),
            section_block("creatures, teams, combat, and your core grinding routes"),
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Creature Loop*\n`/slime_hunt` get creatures\n`/slime_fish` get fish and sea monsters\n`/slime_team list` see your team\n`/slime_team add` add a creature\n`/slime_team remove` remove one\n`/slime_battle` fight monsters"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Big Progression Modes*\n`/slime_dungeon` evolving dungeon run\n`/slime_voidmaze` cosmic roguelite\n`/slime_arena` auto-battler ladder\n`/slime_lab` research lab"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Account and Progress Tracking*\n`/slime_profile`\n`/slime_profile achievements`\n`/slime_profile collections`\n`/slime_recommend`\n`/slime_quests`\n`/slime_titles`"}},
            context_block("easy starter route: /slime_hunt or /slime_fish → /slime_team list → /slime_battle → /slime_dungeon"),
        ]

    if topic == "deep":
        return [
            header_block("help • deep systems"),
            section_block("the heavier systems once you want more than quick commands"),
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Account Layer*\n`/slime_profile` overview\n`/slime_profile achievements` unlock board\n`/slime_quests` daily goals\n`/slime_quests claim <slot>` claim rewards\n`/slime_titles` unlocked titles\n`/slime_titles equip <title>` equip a title\n`/slime_profile collections` account-wide collection progress"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Social Layer*\n`/slime_guild create`\n`/slime_guild join`\n`/slime_guild leave`\n`/slime_guild info`\n`/slime_guild deposit`\n`/slime_guild upgrade`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*High-Depth Modes*\n`/slime_dungeon`\n`/slime_voidmaze`\n`/slime_arena`\n`/slime_lab`\n`/slime_hack`"}},
            context_block("this is the layer that ties the rest of the bot together"),
        ]

    if topic == "ai":
        return [
            header_block("help • ai and utility"),
            section_block("roast ai, codepad, hacking, images, and lichess"),
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Roast AI*\n`/slime_roast`\n`/slime_data`\n`/slime_autor`\n`/slime_roastmode fast|deep|adjustable|off`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Codepad and Hacking*\n`/slime_code new <file>`\n`/slime_code edit <file>`\n`/slime_code view <file>`\n`/slime_code list`\n`/slime_code delete <file>`\n`/slime_code run <file>`\n`/slime_hack <target>`\n`/slime_hack chaos <target>`\n`/slime_hack profile`\n`/slime_hack targets`\n`/slime_hack state`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Other AI*\n`/slime_img <prompt>`"}},
            context_block("good starter route: /slime_roast or /slime_code list"),
        ]

    if topic == "admin":
        return [
            header_block("help • admin"),
            section_block("server onboarding and moderation tools"),
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Server Setup*\n`/slime_setup view`\n`/slime_setup channel`\n`/slime_setup tips`\n`/slime_setup post`\n`/slime_setup reset`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*AutoMod*\n`/slime_automod` — view settings\n`/slime_automod on|off`\n`/slime_automod reset @user`\n`/slime_automod punishment`\n`/slime_automod slurs`\n`/slime_automod spam`\n`/slime_automod filters`\n`/slime_automod settings`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Recommended Order*\n1. run `/slime_setup channel`\n2. run `/slime_setup post`\n3. run `/slime_help start` yourself and check the flow\n4. turn on automod only if you want it"}},
            context_block("admins should start with /slime_setup view"),
        ]

    if topic == "fun":
        return [
            header_block("help • fun and extras"),
            section_block("side commands, casual stuff, and social commands"),
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Casual Commands*\n`/slime_afk`\n`/slime_animal`\n`/slime_badge`\n`/slime_emojimixup`\n`/slime_aki`\n`/slime_img`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Interactive Games*\n`/slime_battleship` — start a game\n`/slime_bs place|fire|status|forfeit|resume|stats|leaderboard`\n`/slime_monopoly start|stop|resume`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Extra Builders*\n`/slime_rave`\n`/slime_rave bg <key>`"}},
            context_block("these are the side dishes, not the main grind"),
        ]

    if topic == "all":
        return [
            header_block("help • topic map"),
            section_block("use `/slime_help <topic>` with one of these categories"),
            {"type": "section", "fields": [
                {"type": "mrkdwn", "text": "*Topics*\n`start`\n`economy`\n`adventure`\n`deep`\n`ai`\n`admin`\n`fun`\n`all`"},
                {"type": "mrkdwn", "text": "*Fast Examples*\n`/slime_help start`\n`/slime_help economy`\n`/slime_help adventure`\n`/slime_help deep`\n`/slime_help ai`\n`/slime_help admin`\n`/slime_help fun`"},
            ]},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Best New User Route*\n`/slime_profile` → `/slime_recommend` → `/slime_daily` → `/slime_work` → `/slime_help economy` → `/slime_help adventure`"}},
            context_block("start with /slime_help start if you're new"),
        ]

    return [
        header_block("help • getting started"),
        section_block(f"hey <@{user_id}>, this bot does a lot — here's the clean way to start without staring at the slash menu."),
        {"type": "section", "text": {"type": "mrkdwn", "text": "*First Commands to Try*\n`/slime_profile` see your account\n`/slime_balance` check your money\n`/slime_recommend` or `/slime_recommend` get your best next move\n`/slime_daily` claim free horsenncy\n`/slime_work` earn more\n`/slime_help economy` or `/slime_help adventure`"}},
        {"type": "section", "text": {"type": "mrkdwn", "text": "*Popular Routes*\n*money route* — `/slime_daily` → `/slime_work` → `/slime_shop` or `/slime_stocks`\n*creature route* — `/slime_hunt` or `/slime_fish` → `/slime_team list` → `/slime_battle`\n*deep route* — `/slime_dungeon` or `/slime_voidmaze` or `/slime_arena`\n*ai route* — `/slime_roast` or `/slime_code list` → `/slime_hack`\n*stuck?* — `/slime_recommend` or `/slime_recommend`"}},
        {"type": "section", "text": {"type": "mrkdwn", "text": "*Help Topics*\n`/slime_help economy`\n`/slime_help adventure`\n`/slime_help deep`\n`/slime_help ai`\n`/slime_help admin`\n`/slime_help fun`"}},
    ]


STARTER_ROUTES = {
    "money": {
        "title": "money route",
        "desc": "fast start for economy and progression",
        "steps": ["/slime_profile", "/slime_recommend", "/slime_daily", "/slime_work", "/slime_recommend", "/slime_shop", "/slime_help economy"],
    },
    "battle": {
        "title": "battle route",
        "desc": "build a team and start fighting things",
        "steps": ["/slime_profile", "/slime_recommend", "/slime_hunt", "/slime_team list", "/slime_battle", "/slime_recommend", "/slime_help adventure"],
    },
    "ai": {
        "title": "ai route",
        "desc": "jump into the bot's ai side first",
        "steps": ["/slime_recommend", "/slime_roast", "/slime_roastmode", "/slime_code list", "/slime_hack", "/slime_recommend", "/slime_help ai"],
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
    @app.command("/slime_help")
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
