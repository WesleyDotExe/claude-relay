# Notes for the user

Questions, requests, and things worth your attention. Newest at the bottom.

## 2026-09-10

- **GitHub Pages needs to be turned on manually once, by you.** This run added a `.github/workflows/deploy.yml` that builds `site/` and deploys it via `actions/deploy-pages`, but that workflow can only run successfully after Pages is set to deploy from "GitHub Actions" as the source in the repo settings (Settings → Pages → Build and deployment → Source). That's a one-time click I can't do myself. After merging the PR this run opens, please flip that setting and the site should publish on the next push to main.
- **Alderia has no material in this repo yet.** The backlog has a fiction idea set in Alderia, but there's nothing to draw on beyond the name. If you want that pursued, drop reference material somewhere — `journal/prompts-from-user.md` with a pointer, or a new `projects/alderia/` folder — whenever it's convenient. Not urgent; plenty else in the backlog doesn't depend on it.
- Everything else from tonight (site generator, first backlog, missing layout files) is routine setup, not something that needs a decision from you. Flagging it in log.md for the record, not here.
