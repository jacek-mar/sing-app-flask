# Changelog

All notable changes to this project are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.0.0] — 2026-02-20

### Added

- Flask 3.x application factory with Blueprint architecture
- 50+ demo pages converted from Sing App HTML5 Handlebars templates
- Pre-staged static assets — no Node.js, npm, or build step required
- SQLite database (default); PostgreSQL-ready via `DATABASE_URL`
- Demo-first authentication: all pages open without login by default
- `REQUIRE_LOGIN` env toggle to enforce login site-wide
- `DEMO_MODE` env toggle — disables admin write actions for public demos
- Three security levels: `demo`, `basic`, `production`
- Admin user management panel (`/admin/users`)
- RESTful JSON API (`/api/users`, `/api/settings`, `/api/notifications`)
- Dark/light theme toggle (persisted in session)
- Flask-Compress (gzip), Flask-Caching, cache headers
- Mobile-responsive sidebar
- Settings overview page (`/settings`)
- Gunicorn WSGI server support
- Render.com one-click deployment (`render.yaml`, `Procfile`)

### Fixed

- Flask-Assets double-initialisation (critical bug)
- SCSS directory name mismatch (auto-fixed by staging script)
- Font Awesome 6 icon class corrections (`fa-gauge-high`, `fa-book-open-reader`)
- Hardcoded sidebar URLs replaced with `url_for()` calls
- Bootstrap 4 Glyphicon references removed
- `datetime.utcnow` deprecation replaced with `datetime.now(timezone.utc)`
- `FLASK_ENV` deprecation replaced with `FLASK_DEBUG`
- FullCalendar page missing CSS import
- Rickshaw `y_axis` DOM element error
- SQLAlchemy `postgres://` → `postgresql://` URL prefix fix

---

*Earlier development history not recorded (pre-release).*
