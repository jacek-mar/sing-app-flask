# Flask Sing App

A reusable Flask admin dashboard built on the
[Sing App HTML5](https://github.com/flatlogic/sing-app-html5) template
(Bootstrap 4, MIT licence). Zero Node.js required — assets are pre-staged.

This project was created to simplify the work of Python developers by providing a ready-to-use Flask admin dashboard framework. It transforms the popular Sing App HTML5 admin template into a production-ready Flask application, eliminating the need for complex setup or Node.js dependencies.

---

## Credits

### KiloCode

This application was created entirely with [KiloCode](https://www.kilocode.app/) — an open-source AI coding assistant for VSCode that supports over 500 different AI models, including the MiniMax M2.5 AI model. KiloCode is available as a free extension for Visual Studio Code and provides intelligent code generation, refactoring, and debugging assistance. Kilo often provides free access to models during limited promotional periods.

### Sing App HTML5

This project is built upon the excellent [Sing App HTML5](https://github.com/flatlogic/sing-app-html5) template by [Flatlogic LLC](https://flatlogic.com/). We are grateful for their open-source MIT-licensed template which serves as the foundation of this Flask application.

The entire project was built in **less than 48 hours** (not counting the preparations and research that took place several months earlier).

This project was also submitted as an entry into the [Developer Week 2026 Hackathon](https://developerweek-2026-hackathon.devpost.com/).

The author was particularly inspired to create this project by this hackathon criterion:

> **Kilo - Finally Ship It.**
> That side project you've been sitting on? This is your excuse to finally build it. Using Kilo Code, create and deploy something you'll actually use. No constraints on what—an app, a game, a tool, a weird experiment. We just want to see you ship it with Kilo. We're judging on creativity, execution, and that "I wish I'd thought of that" feeling.

---

## Online & Offline Usage

This application can be used both **online** and **offline**:

- **Online**: When internet is available, all features work seamlessly with CDN-backed libraries.
- **Offline**: All JavaScript libraries are pre-staged locally in `static/js/vendor/`. The app runs entirely offline after initial setup — no external network requests are required for the application to function.

---

## JavaScript Libraries & Credits

This project uses the following open-source JavaScript libraries (all MIT licensed):

| Library | Description | License |
|---------|-------------|---------|
| **jQuery** 2.1.4 | DOM manipulation | MIT |
| **Popper.js** 1.14.3 | Tooltip/popover positioning | MIT |
| **Bootstrap** 4.3.1 | CSS framework | MIT |
| **Chart.js** 4.4.0 | Charts | MIT |
| **D3.js** 3.5.17 | Data visualization | ISC |
| **Flot** 0.8.3 | Charts | MIT |
| **Morris.js** 0.5.1 | Charts | MIT |
| **Raphael** 2.1.4 | SVG manipulation | MIT |
| **Rickshaw** 1.6.6 | Real-time charts | MIT |
| **FullCalendar** 6.1.8 | Calendar | MIT |
| **Moment.js** 2.24.0 | Date/time | MIT |
| **Leaflet** 1.9.4 | Maps | BSD-2-Clause |
| **Select2** 4.0.6 | Select dropdowns | MIT |
| **Summernote** 0.8.10 | Rich text editor | MIT |
| **Dropzone** 5.5.1 | File uploads | MIT |
| **DataTables** 1.10.19 | Tables | MIT |
| **Toastr** 2.1.3 | Notifications | MIT |
| **SweetAlert2** | Alerts | MIT |
| **Owl Carousel** 2.3.4 | Carousel | MIT |
| **jQuery UI** 1.12.1 | UI components | MIT |
| **Magnific Popup** 1.1.0 | Lightbox | MIT |
| **Font Awesome** 6.4.0 | Icons | MIT/OFL |

All libraries are pre-staged locally and bundled with this application.

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
