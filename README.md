# slimebot

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Slack](https://img.shields.io/badge/Slack-Bolt-4A154B?logo=slack&logoColor=white)
![Socket Mode](https://img.shields.io/badge/Socket%20Mode-enabled-4A154B?logo=slack&logoColor=white)
![AI](https://img.shields.io/badge/AI-GitHub%20Models-181717?logo=github&logoColor=white)
![Deploy](https://img.shields.io/badge/Deploy-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)
![Status](https://img.shields.io/badge/status-active-brightgreen)

> **Full Server Bot** — roast AI, economy, RPG systems, auto-battler, stock market, hacking sim, and more. All slash commands.

---

## Features

| Category | Systems |
|---|---|
| 🔥 Roast AI | Multi-model roasting, memory profiles, auto-roast, spice scoring |
| 💰 Economy | Balance, daily, work, give, pray, leaderboard |
| 🎲 Gambling | Blackjack, slots, coinflip, crime |
| 🦌 Hunting & Fishing | 130+ creatures, weighted rarities, prayer buffs |
| ⚔️ Battle & Team | Monster fights, team management, evolutions |
| 📈 Stocks | Live simulated market, buy/sell, portfolio |
| 🏰 Dungeon | Floor crawler, sanity, relics, raid boss, rift dives |
| 🌀 Voidmaze | Roguelite, artifacts, anomalies, clarity system |
| 🏟️ Arena | Auto-battler, elements, ultimates, seasons, ELO ladder |
| 🧪 Lab | Research, experiments, breakthroughs, instability |
| 💻 Hack | 4-phase hacking RPG using your own code files |
| 📁 Codepad | Per-user code snippets, run in sandbox |
| 🚢 Battleship | Full game with AI (easy → god), ELO ranking |
| 🎩 Monopoly | Full game, AI opponent, SQLite persistence |
| 🏛️ Guilds | Create, join, deposit, upgrade |
| 🛒 Auction House | List, browse, buy, cancel |
| 🗺️ Quests | Daily quest board, claim rewards |
| 🏆 Achievements | 33 tracked milestones, mastery grades |
| 🎖️ Titles & Badges | Unlock and equip cosmetic titles |
| 🛡️ AutoMod | Spam detection, slur filter, escalation ladder |
| 🎉 Fun | Akinator, animal facts, emoji mixup, rave, image gen |

---

## Setup

### 1. Slack App

Create an app at [api.slack.com/apps](https://api.slack.com/apps):

- **Socket Mode** → enable → copy `SLACK_APP_TOKEN` (`xapp-…`)
- **OAuth & Permissions** → add scopes → install to workspace → copy `SLACK_BOT_TOKEN` (`xoxb-…`)
- **Event Subscriptions** → subscribe: `message.channels`, `message.groups`, `message.im`, `message.mpim`, `reaction_added`

Required bot scopes:
```
chat:write  chat:write.public  commands
channels:history  groups:history  im:history  mpim:history
reactions:read  files:write
```

### 2. Register all slash commands

Add `SLACK_APP_ID` and `SLACK_CONFIG_TOKEN` (App-Level Token with `app_configurations:write`) to your secrets, then run once:

```bash
python register_slack_app.py
```

### 3. GitHub Secrets

Go to **Settings → Secrets → Actions** and add:

| Secret | Description |
|---|---|
| `SLACK_BOT_TOKEN` | `xoxb-…` bot token |
| `SLACK_APP_TOKEN` | `xapp-…` socket mode token |
| `HACKCLUB_AI_KEY` | Hack Club AI proxy key — primary chat/roast provider |
| `UPSTASH_REDIS_REST_URL` | Upstash Redis REST URL — bot state storage |
| `UPSTASH_REDIS_REST_TOKEN` | Upstash Redis REST token — bot state storage |
| `GITHUB` | GitHub PAT for AI models *(fallback, optional)* |
| `GROQ` | Groq API key *(fallback, optional)* |
| `GEMINI_API_KEY` | Gemini API key *(fallback, optional)* |
| `OPENROUTER_KEY` | OpenRouter key *(fallback, optional)* |

### 4. Run

The bot runs automatically via GitHub Actions every 6 hours. To start manually:

**Actions → Run Slack Bot → Run workflow**

Or locally:
```bash
pip install -r requirements.txt
python app.py
```

---

## How it works

The bot runs on GitHub Actions on a 6-hour cron. All state (economy, roast memory, automod config, etc.) persists to Upstash Redis, so nothing is lost between runs — no committing state files back to the repo. Monopoly still uses a local SQLite DB, which resets each run.

---

## Command Reference

<details>
<summary><b>🔥 Roast</b></summary>

| Command | Description |
|---|---|
| `/slime_roast @user` | AI-roast someone using memory + multi-model scoring |
| `/slime_roastmode fast\|deep\|adjustable\|off` | Set roast style — `off` exits roast mode |
| `/slime_autor on\|off` | Auto-roast anyone who mentions the bot in this channel |
| `/slime_data [@user]` | View stored memory profile |

</details>

<details>
<summary><b>💰 Economy</b></summary>

| Command | Description |
|---|---|
| `/slime_balance [@user]` | Check balance |
| `/slime_daily` | Claim daily reward |
| `/slime_work` | Work a job for horsenncy |
| `/slime_give @user amount` | Transfer horsenncy |
| `/slime_pray` | Gain a prayer boost |
| `/slime_leaderboard` | Top 10 richest |
| `/slime_coinflip amount [heads\|tails]` | 50/50 gamble |
| `/slime_blackjack amount` | Full blackjack game |
| `/slime_slots amount` | 3×3 slot machine |
| `/slime_crime` | High-risk heist |

</details>

<details>
<summary><b>🛍️ Shop & Items</b></summary>

| Command | Description |
|---|---|
| `/slime_shop` | Browse all items |
| `/slime_buy item [amount]` | Purchase an item |
| `/slime_inventory [@user]` | View items |
| `/slime_use item` | Use an item |

</details>

<details>
<summary><b>📈 Stocks</b></summary>

| Command | Description |
|---|---|
| `/slime_stocks` | View market prices and your portfolio |
| `/slime_stocks buy SYMBOL amount` | Buy shares |
| `/slime_stocks sell SYMBOL amount` | Sell shares |

</details>

<details>
<summary><b>🦌 Hunting, Fishing & Battle</b></summary>

| Command | Description |
|---|---|
| `/slime_hunt` | Hunt one of 130+ creatures |
| `/slime_fish` | Fish for aquatic creatures |
| `/slime_battle [@user]` | Fight a monster or player |
| `/slime_team list\|add\|remove` | Manage your battle team |

</details>

<details>
<summary><b>🏰 Deep Modes</b></summary>

**Complicated to use!**

| Command | Description |
|---|---|
| `/slime_dungeon` | Enter the dungeon RPG |
| `/slime_voidmaze` | Enter the void maze roguelite |
| `/slime_arena` | Enter the auto-battler arena |
| `/slime_arena buy might\|haste\|ward\|luck` | Buy an arena upgrade with crowns |
| `/slime_arena setteam name1, name2, …` | Set your arena team (up to 5) |
| `/slime_lab` | Enter the research lab |

</details>

<details>
<summary><b>💻 Hack & Codepad</b></summary>

**Complicated to use!**

| Command | Description |
|---|---|
| `/slime_hack <target>` | Run a 4-phase hacking sim |
| `/slime_hack profile [@user]` | View hack stats |
| `/slime_hack targets` | List available targets |
| `/slime_hack chaos <target>` | Trigger chaos hack (max difficulty) |
| `/slime_hack state` | View current chaos resonance |
| `/slime_code new <file>` | Create a code file |
| `/slime_code edit <file>` | Edit a file via modal |
| `/slime_code view <file>` | View a file |
| `/slime_code list` | List your files |
| `/slime_code delete <file>` | Delete a file |
| `/slime_code run <file>` | Run a file |

</details>

<details>
<summary><b>🚢 Battleship</b></summary>

| Command | Description |
|---|---|
| `/slime_battleship [@user \| ai diff]` | Start a game |
| `/slime_bs place A0 r\|d` | Place your next ship |
| `/slime_bs fire B5` | Fire at a coordinate |
| `/slime_bs status` | View your boards |
| `/slime_bs forfeit` | Forfeit |
| `/slime_bs resume` | Resume a saved game |
| `/slime_bs stats [@user]` | Win/loss/ELO stats |
| `/slime_bs leaderboard` | ELO leaderboard |

</details>

<details>
<summary><b>🎩 Monopoly</b></summary>

| Command | Description |
|---|---|
| `/slime_monopoly start [@opponent]` | Start a game (vs player or AI) |
| `/slime_monopoly stop` | End the current game |
| `/slime_monopoly resume` | Resume a saved game |

</details>

<details>
<summary><b>🏛️ Guilds & Auction</b></summary>

| Command | Description |
|---|---|
| `/slime_guild create name` | Create a guild |
| `/slime_guild join id` | Join a guild |
| `/slime_guild leave` | Leave your guild |
| `/slime_guild info [id]` | View guild info |
| `/slime_guild deposit amount` | Deposit to guild bank |
| `/slime_guild upgrade` | Upgrade guild level |
| `/slime_auction sell item amount price` | List an item |
| `/slime_auction browse` | Browse listings |
| `/slime_auction buy id` | Buy a listing |
| `/slime_auction cancel id` | Cancel your listing |

</details>

<details>
<summary><b>🗺️ Quests, Profile & Titles</b></summary>

| Command | Description |
|---|---|
| `/slime_quests [@user]` | View daily quest board |
| `/slime_quests claim slot` | Claim a completed quest |
| `/slime_profile [@user]` | View full profile |
| `/slime_profile achievements [@user]` | View achievement progress |
| `/slime_profile collections [@user]` | View collector stats |
| `/slime_titles [@user]` | View unlocked titles |
| `/slime_titles equip title` | Equip a title |
| `/slime_badge [@user]` | View badges |

</details>

<details>
<summary><b>🛡️ AutoMod</b></summary>

**Complicated to use!**

| Command | Description |
|---|---|
| `/slime_automod` | View current settings |
| `/slime_automod on\|off` | Enable or disable automod |
| `/slime_automod reset @user` | Reset a user's offence count |
| `/slime_automod punishment level action` | Set punishment for a level |
| `/slime_automod slurs list\|add\|remove` | Manage slur filter |
| `/slime_automod spam setting value` | Configure spam thresholds |
| `/slime_automod filters name on\|off` | Toggle a filter |
| `/slime_automod settings key value` | Adjust misc settings |

</details>

<details>
<summary><b>🎉 Fun & Misc</b></summary>

| Command | Description |
|---|---|
| `/slime_aki` | Play Akinator |
| `/slime_animal` | Random animal fact |
| `/slime_emojimixup` | Mix up emoji meanings |
| `/slime_rave` | Start a rave |
| `/slime_rave bg <key>` | Set rave background video |
| `/slime_img prompt` | Generate an image |
| `/slime_afk [message]` | Set AFK status |
| `/slime_recommend` | Get a personalised activity suggestion |
| `/slime_help [topic\|start]` | Help guide — use `start` for the beginner guide |
| `/slime_setup view\|channel\|tips\|post\|reset` | Workspace setup |

</details>

---

*slimebot — Full (Fu) Server (S) Bot*
