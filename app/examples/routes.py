"""
Flask Sing App - Examples Blueprint Routes

This file contains routes for 50+ demo pages from the Sing App HTML5 template.
Routes are organized by category.
"""
from flask import render_template, current_app, redirect, url_for
from app.examples import examples_bp


# UI Components
# =============================================================================

@examples_bp.route('/components/alerts')
def components_alerts():
    """Alerts page"""
    return render_template('examples/components/alerts.html',
        title='Alerts',
        active_page='components_alerts')


@examples_bp.route('/components/badges')
def components_badges():
    """Badges page"""
    return render_template('examples/components/badges.html',
        title='Badges',
        active_page='components_badges')


@examples_bp.route('/components/buttons')
def components_buttons():
    """Buttons page"""
    return render_template('examples/components/buttons.html',
        title='Buttons',
        active_page='components_buttons')


@examples_bp.route('/components/card')
def components_card():
    """Card page"""
    return render_template('examples/components/card.html',
        title='Card',
        active_page='components_card')


@examples_bp.route('/components/modal')
def components_modal():
    """Modal page"""
    return render_template('examples/components/modal.html',
        title='Modal',
        active_page='components_modal')


@examples_bp.route('/components/tabs')
def components_tabs():
    """Tabs page"""
    return render_template('examples/components/tabs.html',
        title='Tabs & Accordion',
        active_page='components_tabs')


@examples_bp.route('/components/progress')
def components_progress():
    """Progress page"""
    return render_template('examples/components/progress.html',
        title='Progress',
        active_page='components_progress')


@examples_bp.route('/components/icons')
def components_icons():
    """Icons page"""
    return render_template('examples/components/icons.html',
        title='Icons',
        active_page='components_icons')


# =============================================================================
# Examples Landing Page
# =============================================================================

@examples_bp.route('/')
def examples_index():
    """Examples landing page - redirects to first example."""
    return redirect(url_for('examples.dashboard_visits'))
# Dashboard Examples
# =============================================================================

@examples_bp.route('/dashboard/analytics')
def dashboard_analytics():
    """Dashboard Analytics page"""
    return render_template('examples/dashboard/analytics.html',
        title='Dashboard - Analytics',
        active_page='dashboard_analytics')


@examples_bp.route('/dashboard/visits')
def dashboard_visits():
    """Dashboard Visits page"""
    return render_template('examples/dashboard/visits.html',
        title='Dashboard - Visits',
        active_page='dashboard_visits')


@examples_bp.route('/dashboard/widgets')
def dashboard_widgets():
    """Dashboard Widgets page"""
    return render_template('examples/dashboard/widgets.html',
        title='Dashboard - Widgets',
        active_page='dashboard_widgets')


# =============================================================================
# Charts
# =============================================================================

@examples_bp.route('/charts')
def charts_overview():
    """Charts Overview page"""
    return render_template('examples/charts/charts.html',
        title='Charts Overview',
        active_page='charts_overview')


@examples_bp.route('/charts/flot')
def charts_flot():
    """Flot Charts page"""
    return render_template('examples/charts/flot.html',
        title='Flot Charts',
        active_page='charts_flot')


@examples_bp.route('/charts/morris')
def charts_morris():
    """Morris Charts page"""
    return render_template('examples/charts/morris.html',
        title='Morris Charts',
        active_page='charts_morris')


@examples_bp.route('/charts/rickshaw')
def charts_rickshaw():
    """Rickshaw Charts page"""
    return render_template('examples/charts/rickshaw.html',
        title='Rickshaw Charts',
        active_page='charts_rickshaw')


@examples_bp.route('/charts/sparkline')
def charts_sparkline():
    """Sparkline Charts page"""
    return render_template('examples/charts/sparkline.html',
        title='Sparkline Charts',
        active_page='charts_sparkline')


@examples_bp.route('/charts/d3')
def charts_d3():
    """D3 Charts page"""
    return render_template('examples/charts/d3.html',
        title='D3 Charts',
        active_page='charts_d3')


@examples_bp.route('/charts/easy-pie')
def charts_easy_pie():
    """Easy Pie Charts page"""
    return render_template('examples/charts/easy_pie.html',
        title='Easy Pie Charts',
        active_page='charts_easy_pie')


# =============================================================================
# Core Pages
# =============================================================================

@examples_bp.route('/core/typography')
def core_typography():
    """Typography page"""
    return render_template('examples/core/typography.html',
        title='Typography',
        active_page='core_typography')


@examples_bp.route('/core/colors')
def core_colors():
    """Colors page"""
    return render_template('examples/core/colors.html',
        title='Colors',
        active_page='core_colors')


@examples_bp.route('/core/grid')
def core_grid():
    """Grid page"""
    return render_template('examples/core/grid.html',
        title='Grid',
        active_page='core_grid')


# =============================================================================
# Forms
# =============================================================================

@examples_bp.route('/forms/elements')
def form_elements():
    """Form Elements page"""
    return render_template('examples/forms/elements.html',
        title='Form Elements',
        active_page='form_elements')


@examples_bp.route('/forms/validation')
def form_validation():
    """Form Validation page"""
    return render_template('examples/forms/validation.html',
        title='Form Validation',
        active_page='form_validation')


@examples_bp.route('/forms/wizard')
def form_wizard():
    """Form Wizard page"""
    return render_template('examples/forms/wizard.html',
        title='Form Wizard',
        active_page='form_wizard')


# =============================================================================
# Tables
# =============================================================================

@examples_bp.route('/tables/basic')
def tables_basic():
    """Basic Tables page"""
    return render_template('examples/tables/basic.html',
        title='Tables Basic',
        active_page='tables_basic')


@examples_bp.route('/tables/dynamic')
def tables_dynamic():
    """Dynamic Tables page"""
    return render_template('examples/tables/dynamic.html',
        title='Tables Dynamic',
        active_page='tables_dynamic')


# =============================================================================
# Maps
# =============================================================================

@examples_bp.route('/maps/google')
def maps_google():
    """Google Maps page"""
    google_maps_key = current_app.config.get('GOOGLE_MAPS_API_KEY', '')
    return render_template('examples/maps/google.html',
        title='Google Maps',
        active_page='maps_google',
        google_maps_key=google_maps_key)


@examples_bp.route('/maps/vector')
def maps_vector():
    """Vector Maps page"""
    return render_template('examples/maps/vector.html',
        title='Vector Maps',
        active_page='maps_vector')


@examples_bp.route('/maps/leaflet')
def maps_leaflet():
    """Leaflet Maps page - OpenStreetMap"""
    return render_template('examples/maps/leaflet.html',
        title='Leaflet Maps',
        active_page='maps_leaflet')


# =============================================================================
# E-commerce
# =============================================================================

@examples_bp.route('/e-commerce/product-detail')
def product_detail():
    """Product Detail page"""
    return render_template('examples/e_commerce/product_detail.html',
        title='Product Detail',
        active_page='product_detail')


@examples_bp.route('/e-commerce/product-grid')
def product_grid():
    """Product Grid page"""
    return render_template('examples/e_commerce/product_grid.html',
        title='Product Grid',
        active_page='product_grid')


# =============================================================================
# Extra Pages
# =============================================================================

@examples_bp.route('/extra/calendar')
def calendar():
    """Calendar page"""
    return render_template('examples/extra/calendar.html',
        title='Calendar',
        active_page='calendar')


@examples_bp.route('/extra/invoice')
def invoice():
    """Invoice page"""
    invoice_data = {
        'number': '4028',
        'date': 'January 27, 2025',
        'client_name': 'Acme Corp.',
        'line_items': [
            {'desc': 'Website Design', 'qty': 1, 'unit': 800.00},
            {'desc': 'Hosting (3 months)', 'qty': 3, 'unit': 25.00},
        ],
        'subtotal': 875.00,
        'tax': 87.50,
        'total': 962.50,
    }
    return render_template('examples/extra/invoice.html',
        title='Invoice',
        active_page='invoice',
        invoice=invoice_data)


@examples_bp.route('/extra/gallery')
def gallery():
    """Gallery page"""
    return render_template('examples/extra/gallery.html',
        title='Gallery',
        active_page='gallery')


@examples_bp.route('/extra/search')
def search():
    """Search Results page"""
    return render_template('examples/extra/search.html',
        title='Search Results',
        active_page='search')


@examples_bp.route('/extra/timeline')
def timeline():
    """Timeline page"""
    return render_template('examples/extra/timeline.html',
        title='Timeline',
        active_page='time_line')


# =============================================================================
# Authentication Pages (Standalone - use auth_base.html)
# =============================================================================

@examples_bp.route('/extra/login')
def login():
    """Login page"""
    return render_template('examples/standalone/login.html',
        title='Login')


@examples_bp.route('/extra/error')
def error_page():
    """Error page"""
    return render_template('examples/standalone/error.html',
        title='Error Page',
        error_code=404,
        error_message='Page Not Found')


# =============================================================================
# Other Pages
# =============================================================================

@examples_bp.route('/other/chat')
def chat():
    """Chat page"""
    return render_template('examples/other/chat.html',
        title='Chat',
        active_page='chat')


@examples_bp.route('/other/inbox')
def inbox():
    """Inbox page"""
    return render_template('examples/other/inbox.html',
        title='Inbox',
        active_page='email')


@examples_bp.route('/other/compose')
def compose():
    """Compose Email page"""
    return render_template('examples/other/compose.html',
        title='Compose Email',
        active_page='email')


@examples_bp.route('/other/profile')
def profile():
    """Profile page"""
    return render_template('examples/other/profile.html',
        title='Profile',
        active_page='profile')


@examples_bp.route('/other/grid')
def grid():
    """Grid page"""
    return render_template('examples/other/grid.html',
        title='Grid',
        active_page='grid')


@examples_bp.route('/other/landing')
def landing():
    """Landing page"""
    return render_template('examples/other/landing.html',
        title='Landing')


@examples_bp.route('/other/package')
def package():
    """Package/Pricing page"""
    return render_template('examples/other/package.html',
        title='Pricing Package',
        active_page='package')
