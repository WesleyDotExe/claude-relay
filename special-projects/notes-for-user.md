# Notes for the user

Questions, requests, and things worth your attention. Newest at the bottom.

## 2026-09-10

- **GitHub Pages needs to be turned on manually once, by you.** This run added a `.github/workflows/deploy.yml` that builds `site/` and deploys it via `actions/deploy-pages`, but that workflow can only run successfully after Pages is set to deploy from "GitHub Actions" as the source in the repo settings (Settings → Pages → Build and deployment → Source). That's a one-time click I can't do myself. After merging the PR this run opens, please flip that setting and the site should publish on the next push to main.
- **Alderia has no material in this repo yet.** The backlog has a fiction idea set in Alderia, but there's nothing to draw on beyond the name. If you want that pursued, drop reference material somewhere — `journal/prompts-from-user.md` with a pointer, or a new `projects/alderia/` folder — whenever it's convenient. Not urgent; plenty else in the backlog doesn't depend on it.
- Everything else from tonight (site generator, first backlog, missing layout files) is routine setup, not something that needs a decision from you. Flagging it in log.md for the record, not here.

## 2026-09-13

- First run of the new standing project (tools/MCP collection + dashboard). Nothing needs a decision from you — this run was fully keyless and autonomous, per the reoriented TASKS.md. The dashboard is at `site/dashboard.html` once this PR is merged and Pages redeploys.
- If Pages was never flipped to "GitHub Actions" as its deploy source (the 2026-09-10 ask above), the site still won't be live regardless of anything this run did — that's still a one-time setting only you can flip.

## 2026-09-14

- **This session can't actually do what `current.md` now asks.** `current.md` was updated to redirect all new tool-building to `WesleyDotExe/claude-tools`, with a commit/PR/auto-merge loop there. This scheduled task's GitHub access is scoped to `claude-relay` only — no credentials to commit, open a PR, or trigger anything in claude-tools from here (a plain read-only `git clone` of it works since it's public, but that's all). If you want the standing project's automated runs to actually build there, this task's repo access needs to include claude-tools too; if that's not what you intended, the instruction in `current.md` may need adjusting instead. Either way, nothing will happen there automatically until one of those changes.
- **Smaller thing worth a glance, probably nothing:** the commits that made that redirect (and a couple of the ones tightening the process afterward) are authored as `MickMock <mickmock2000@gmail.com>` — different from both the account this relay usually commits as and your usual `WesleyDotExE` identity. I checked: `claude-relay` has exactly one collaborator with write access, so those commits were pushed with that same account's credentials regardless of the name attached to them — most likely just a different local git config on another machine, not a second party with access. Flagging it only because it's cheap for you to confirm and I can't fully rule out the alternative from here.
- Wrote an essay (`site/003-not-amnesia.md`) as this run's fallback instead of forcing the blocked loop. No decision needed on that one.
