# Track Claude Code usage with ccusage

[`ccusage`](https://github.com/ryoppippi/ccusage) is a popular (16k+ ⭐) CLI that reads Claude Code's local logs and shows how much you've used — right in your status line. This is what powers the usage display in my Claude Code setup.

## What it shows

Added to the status line at the bottom of Claude Code, it looks like:

```
🤖 Opus 4.8 | 💰 $0.42 session / $2.37 today / $2.37 block (3h 16m left) | 🔥 $3.04/hr 🟢 (Normal) | 🧠 42%
```

- **session** — cost of the current session
- **today** — total for the day (rolls over at midnight in your timezone)
- **block (Xh Ym left)** — the active rolling 5-hour window and time until it resets
- **🔥 burn rate** — spend per hour, with a color indicator
- **🧠** — context-window usage

## Setup

### 1. Install

```bash
npm install -g ccusage
```

(Or run it on demand with `npx ccusage` — but a global install makes the status line render faster.)

### 2. Add it to Claude Code

Edit `~/.claude/settings.json` and add a `statusLine` block:

```json
{
  "statusLine": {
    "type": "command",
    "command": "ccusage statusline --timezone Asia/Kolkata --visual-burn-rate emoji-text",
    "padding": 0
  }
}
```

Set `--timezone` to your IANA timezone (e.g. `Asia/Kolkata`, `America/New_York`, `Europe/London`) so the daily total rolls over at your local midnight. Drop `--visual-burn-rate` if you don't want the colored burn indicator.

Restart Claude Code (or start a new session) and the status line appears.

### 3. Check history anytime

```bash
ccusage            # summary
ccusage daily      # per-day breakdown
ccusage monthly    # per-month breakdown
```

## Notes for subscription (Pro/Max) users

- The `$` figures are **estimated token cost**, not your subscription bill (which is a flat fee). Treat them as a relative "how heavily am I using it" gauge.
- The **`(Xh Ym left)` block reset is the real rolling window**.
- For exact plan **quota %** and reset times, use Claude Code's built-in **`/usage`** command — it's official and precise. `ccusage` gives the always-on burn view; `/usage` gives the exact numbers on demand.

## Keeping it current

To reduce exposure to broken/outdated versions, update periodically:

```bash
npm install -g ccusage@latest
```
