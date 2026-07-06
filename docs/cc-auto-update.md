# Auto-update Claude Code tooling on launch

A shell wrapper that keeps Claude Code and its ecosystem current — so you're not running a stale or known-broken version — without slowing down every launch.

It replaces a plain `alias cc='claude'` with two functions:

- **`cc`** — launches Claude Code, but first runs an update **at most once per 24h** (throttled via a timestamp file, so day-to-day launches stay instant).
- **`ccupdate`** — run manually anytime to force-update everything now.

## What gets updated

- **Claude Code** — via Homebrew cask (`brew upgrade --cask claude-code`), falling back to `claude update`.
- **ccusage** and **claude-code-router** — npm globals.
- **All global skills** — via `npx skills update -g -y`.

## Setup

Add this to your `~/.zshrc` (or `~/.bashrc`), removing any existing `alias cc='claude'`:

```bash
# Update Claude Code + ccusage + router + all global skills to latest
ccupdate() {
  echo "⟳ Updating Claude Code, ccusage, claude-code-router, and skills…"
  brew upgrade --cask claude-code 2>/dev/null || claude update
  npm install -g ccusage@latest @musistudio/claude-code-router@latest
  npx -y skills update -g -y
  echo "✓ All Claude tooling up to date."
}

# Launch Claude Code; auto-update at most once per 24h before launching
cc() {
  local stamp="$HOME/.cache/cc-last-update"
  mkdir -p "$HOME/.cache"
  if [ ! -f "$stamp" ] || [ -n "$(find "$stamp" -mmin +1440 2>/dev/null)" ]; then
    ccupdate && touch "$stamp"
  fi
  claude "$@"
}
```

Then reload your shell:

```bash
source ~/.zshrc
```

## How the throttle works

`cc` checks `~/.cache/cc-last-update`. If that file is missing or older than 1440 minutes (24h), it runs `ccupdate` and re-stamps the file. Otherwise it launches Claude immediately. So you get at most one update per day, on the first `cc` of the day.

- First `cc` of the day: 10–30s update, then launch.
- Every later `cc` that day: instant.
- Want to skip the update for a quick launch? Just run `claude` directly instead of `cc`.
- Force an update right now: `ccupdate`.

## Customizing

- **Different interval** — change `-mmin +1440` (1440 min = 24h). E.g. `+10080` for weekly.
- **Not on Homebrew** — the `|| claude update` fallback handles npm/native installs.
- **Adjust which tools update** — edit the commands inside `ccupdate`.

## Caveat

Auto-updating protects against running an *old or known-broken* version, which is the realistic risk. It is not a guarantee against a freshly compromised release — a bad new version would also be pulled in. Pin versions manually if you need stricter supply-chain control.
