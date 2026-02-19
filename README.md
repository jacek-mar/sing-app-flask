# Sing App Flask

A reusable Flask + Sing App HTML5 admin dashboard foundation - **50+ pages migrated from HTML5 to Jinja2 templates**.

## Features

- **No Node.js required** - Pure Python Flask application
- **Application Factory Pattern** - Modular Flask architecture with Blueprints
- **SQLAlchemy** - SQLite database with User model
- **Feature Toggles** - Enable/disable example pages and features
- **MIT License Compatible** - Using Bootstrap, Font Awesome, jQuery (all MIT licensed)
- **50+ Example Pages** - Fully migrated from original Sing App HTML5 template

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

## Example Pages (50+ Templates)

### Dashboard
- Main Dashboard
- Dashboard - Visits
- Dashboard - Widgets
- Dashboard - Dark Theme

### UI Components
- Alerts
- Badges
- Buttons
- Cards
- Modal
- Tabs
- Progress
- Icons (Font Awesome + Bootstrap Icons)

### Core
- Typography
- Colors
- Grid System

### Forms
- Form Elements
- Form Validation
- Form Wizard

### Tables
- Basic Tables
- Dynamic Tables (DataTables)

### Charts
- Chart Overview
- Flot Charts
- Morris Charts
- Rickshaw Charts
- Sparkline Charts
- Easy Pie Charts
- D3.js Visualizations

### Maps
- Google Maps (requires API key)
- Vector Maps

### Extra Pages
- Calendar
- Gallery
- Timeline
- Invoice
- Search
- Pricing
- Login

### E-commerce
- Product Detail
- Product Grid
- Orders
- Cart

### Other
- Profile
- Inbox
- Grid System Showcase
- Package Info
- Landing Page

## Technology Stack

### Backend
- Flask 3.x
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Assets
- Python 3.x

### Frontend (CDN)
- Bootstrap 5.3.x (MIT)
- jQuery 3.7.x (MIT)
- Font Awesome 6.4.x (MIT - Free)
- Bootstrap Icons 1.11.x (MIT)
- Chart.js 4.4.x (MIT)

## Project Structure

```
sing-app-flask/
├── app/
│   ├── __init__.py      # Application factory
│   ├── assets.py        # Flask-Assets configuration
│   ├── extensions.py    # Flask extensions
│   ├── models.py       # SQLAlchemy models
│   ├── config.py       # Configuration
│   ├── main/           # Main dashboard blueprint
│   ├── api/            # API blueprint
│   └── examples/       # Example pages blueprint
├── static/              # Static assets (CSS, JS, images)
├── templates/           # Jinja2 templates
│   ├── base.html       # Base template with sidebar
│   └── examples/       # Example page templates
├── design_docs/         # Design documentation
├── scripts/            # Utility scripts
├── config.py           # Configuration classes
└── run.py             # Entry point
```

## Development

```cmd
# Development server with auto-reload
.venv\Scripts\flask run --reload

# Specify port
.venv\Scripts\flask run --port 5000
```

## Credits & License

### MIT License

This project is licensed under the **MIT License**. See LICENSE file for details.

### Open Source Libraries

This project uses the following MIT-licensed libraries:

| Library | Version | License | Purpose |
|---------|---------|---------|---------|
| **Flask** | 3.x | MIT | Python web framework |
| **Flask-SQLAlchemy** | 3.x | MIT | ORM integration |
| **Flask-Migrate** | 4.x | MIT | Database migrations |
| **Flask-Assets** | 2.x | MIT | Asset compilation |
| **Bootstrap** | 5.3.x | MIT | CSS framework |
| **jQuery** | 3.7.x | MIT | JavaScript library |
| **Font Awesome** | 6.4.x | MIT (Free) | Icon library |
| **Bootstrap Icons** | 1.11.x | MIT | Icon library |
| **Chart.js** | 4.4.x | MIT | Charting library |
| **DataTables** | 2.x | MIT | Table plugin |
| **Popper.js** | 2.x | MIT | Tooltip/popover library |
| **Morris.js** | 0.5.x | MIT | Charting library |
| **Flot** | 0.8.x | MIT | Charting library |
| **jQuery Sparkline** | 2.1.x | MIT | Sparkline charts |
| **jVectorMap** | 2.0.x | MIT | Vector maps |
| **D3.js** | 7.x | ISC | Data visualization |
| **FullCalendar** | 6.1.x | MIT | Calendar widget |

### Third-Party Resources

- **Google Maps** - Requires API key (free tier available). See [Google Cloud Console](https://console.cloud.google.com/) for setup.

### Original Template

This project is based on [Sing App HTML5](https://github.com/flatlogic/sing-app-html5) by Flatlogic (MIT License).

## Design Documentation

See [`design_docs/`](design_docs/) directory for:
- [`complete_migration_plan.md`](design_docs/complete_migration_plan.md) - Full migration overview
- [`implementation_roadmap.md`](design_docs/implementation_roadmap.md) - Detailed implementation plan
- [`migration_checklist.md`](design_docs/migration_checklist.md) - Progress tracking
- [`component_mapping.md`](design_docs/component_mapping.md) - Handlebars to Jinja2 guide
- [`technical_specification.md`](design_docs/technical_specification.md) - Technical requirements

## Status: Complete ✅

All 50+ templates have been migrated from HTML5 Handlebars to Jinja2. The project is ready for production use.
