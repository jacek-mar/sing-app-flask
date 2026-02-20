# Flask Sing App

A reusable Flask admin dashboard built on the
[Sing App HTML5](https://github.com/flatlogic/sing-app-html5) template
(Bootstrap 4, MIT licence). Zero Node.js required — assets are pre-staged.

---

## Live Demo

*Link will be added after Render.com deployment — see [Session 13](../_revision_and_changes/session_13_render_deployment.md).*

---

## Features

- Flask 3.x application factory + Blueprint architecture
- 50+ demo pages (charts, tables, forms, maps, UI components)
- Pre-built CSS — no npm, gulp, or webpack required
- SQLite by default; swap to PostgreSQL via `DATABASE_URL`
- Demo-first: all pages accessible without login by default
- Optional login enforcement: set `REQUIRE_LOGIN=true` in `.env`
- `DEMO_MODE` toggle — disables admin write actions for public demos
- Dark/light theme toggle
- Admin user management panel
- RESTful JSON API (`/api/users`, `/api/settings`, `/api/notifications`)

---

## Quick Start

### 1. Clone

    git clone <repository-url>
    cd sing-app-flask-admin/sing-app-flask

### 2. Create virtual environment

    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # macOS / Linux:
    source .venv/bin/activate

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Create environment file

    cp .env.example .env
    # Open .env and set a unique SECRET_KEY

### 5. Initialise the database

    flask init-db
    flask seed-db

### 6. Run

    python run.py

Open **http://localhost:49251** — no login required in the default demo mode.

Default admin credentials (after `flask seed-db`): `admin` / `admin`

---

## Key Configuration

| Variable | Default | Effect |
|----------|---------|--------|
| `REQUIRE_LOGIN` | `false` | `true` = login required on all pages |
| `DEMO_MODE` | `true` | `true` = admin write actions disabled |
| `SECURITY_LEVEL` | `demo` | `demo` / `basic` / `production` |
| `DATABASE_URL` | `sqlite:///dev.db` | Swap to a PostgreSQL/MySQL connection string |
| `FLASK_CONFIG` | `development` | `development` / `production` / `testing` |

Full configuration reference: see `CONFIGURATION.md` (created in Session 15).

---

## Project Layout

    sing-app-flask/
    ├── app/
    │   ├── __init__.py       # create_app() factory
    │   ├── extensions.py     # db, login_manager, cache
    │   ├── models.py         # User model
    │   ├── main/             # Dashboard blueprint
    │   ├── auth/             # Login / logout / register
    │   ├── admin/            # User CRUD (admin-only)
    │   ├── examples/         # 50+ demo pages
    │   └── api/              # REST API
    ├── templates/
    ├── static/               # Pre-staged CSS, JS, images
    ├── config.py
    ├── run.py
    └── requirements.txt

---

## Licence

MIT — see [LICENSE](LICENSE).
Sing App HTML5 template: MIT, [Flatlogic LLC](https://flatlogic.com).
