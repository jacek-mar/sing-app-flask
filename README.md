# Sing App Flask

A reusable Flask + Sing App HTML5 admin dashboard foundation.

## Features

- **No Node.js required** - Pure Python Flask application
- **Application Factory Pattern** - Modular Flask architecture with Blueprints
- **SQLAlchemy** - SQLite database with User model
- **Feature Toggles** - Enable/disable example pages and features
- **SCSS Ready** - Flask-Assets integration for SCSS compilation
- **50+ Example Pages** - From original Sing App HTML5 template

## Quick Start

```cmd
# Clone and navigate to project
cd sing-app-flask

# Create virtual environment
python -m venv .venv

# Activate and install dependencies
.venv\Scripts\pip install -r requirements.txt

# Run the application
.venv\Scripts\python run.py
```

Open http://localhost:49251 in your browser.

## Configuration

### Environment Variables

Create a `.env` file in `sing-app-flask/` directory:

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
SQLALCHEMY_DATABASE_URI=sqlite:///app.db
ENABLE_EXAMPLES=True
ENABLE_DARK_THEME=True
```

### Feature Toggles

| Variable | Default | Description |
|----------|---------|-------------|
| `ENABLE_EXAMPLES` | True | Enable example/demo pages |
| `ENABLE_DARK_THEME` | False | Enable dark theme support |

## Commands

```cmd
# Initialize database
.venv\Scripts\flask init-db

# Seed database with sample data
.venv\Scripts\flask seed-db

# Compile SCSS assets
.venv\Scripts\flask compile-assets
```

## Project Structure

```
sing-app-flask/
├── app/
│   ├── __init__.py      # Application factory
│   ├── assets.py        # Flask-Assets configuration
│   ├── extensions.py    # Flask extensions
│   ├── models.py       # SQLAlchemy models
│   ├── main/           # Main dashboard blueprint
│   ├── api/            # API blueprint
│   └── examples/       # Example pages blueprint
├── static/              # Static assets (CSS, JS, images)
├── templates/           # Jinja2 templates
├── scripts/            # Utility scripts
├── config.py           # Configuration classes
└── run.py             # Entry point
```

## Blueprints

### Main Blueprint (`/`)
Core dashboard page - always enabled regardless of `ENABLE_EXAMPLES`.

### API Blueprint (`/api`)
REST API endpoints:
- `GET /api/users` - List users
- `GET /api/settings` - App settings

### Examples Blueprint (`/examples`)
50+ demo pages from Sing App HTML5:
- Dashboard variants
- Charts (Flot, Chart.js, Morris, etc.)
- Forms (elements, validation, wizard)
- Tables (basic, dynamic)
- Maps (Google, Vector)
- And more...

Disable via `ENABLE_EXAMPLES=False` in config.

## SCSS Compilation

The project includes Flask-Assets + libsass for SCSS compilation:

```cmd
.venv\Scripts\flask compile-assets
```

Output: `static/css/application.css`

Note: Original Sing App SCSS references node_modules paths. For full SCSS support, install Bootstrap separately or modify import paths.

## Development

```cmd
# Development server with auto-reload
.venv\Scripts\flask run --reload

# Specify port
.venv\Scripts\flask run --port 5000
```

## License

Based on Sing App HTML5 (MIT) - https://github.com/flatlogic/sing-app-html5
