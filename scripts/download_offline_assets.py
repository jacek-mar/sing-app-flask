#!/usr/bin/env python
"""
Download all CDN assets needed for offline operation.
This script downloads CSS and JS files from CDN to local static folder.
"""

import os
import urllib.request
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent
STATIC_DIR = BASE_DIR / "static"

# URLs to download
ASSETS = [
    # Line Awesome CSS and fonts
    ("https://cdnjs.cloudflare.com/ajax/libs/line-awesome/1.3.0/css/line-awesome.min.css", "css/vendor/line-awesome.min.css"),
    ("https://cdnjs.cloudflare.com/ajax/libs/line-awesome/1.3.0/fonts/line-awesome.svg", "fonts/line-awesome/line-awesome.svg"),
    ("https://cdnjs.cloudflare.com/ajax/libs/line-awesome/1.3.0/fonts/line-awesome.ttf", "fonts/line-awesome/line-awesome.ttf"),
    ("https://cdnjs.cloudflare.com/ajax/libs/line-awesome/1.3.0/fonts/line-awesome.woff", "fonts/line-awesome/line-awesome.woff"),
    ("https://cdnjs.cloudflare.com/ajax/libs/line-awesome/1.3.0/fonts/line-awesome.woff2", "fonts/line-awesome/line-awesome.woff2"),
    
    # Summernote CSS and fonts
    ("https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.18/summernote-bs4.min.css", "css/vendor/summernote-bs4.min.css"),
    ("https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.18/summernote.min.js", "js/vendor/summernote.min.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.18/font/summernote.eot", "fonts/summernote/summernote.eot"),
    ("https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.18/font/summernote.ttf", "fonts/summernote/summernote.ttf"),
    ("https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.18/font/summernote.woff", "fonts/summernote/summernote.woff"),
    ("https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.18/font/summernote.woff2", "fonts/summernote/summernote.woff2"),
    
    # Owl Carousel
    ("https://cdnjs.cloudflare.com/ajax/libs/owl-carousel/1.3.3/owl.carousel.min.js", "js/vendor/owl.carousel.min.js"),
    
    # Intro.js
    ("https://cdnjs.cloudflare.com/ajax/libs/intro.js/7.0.0/introjs.min.css", "css/vendor/introjs.min.css"),
    ("https://cdnjs.cloudflare.com/ajax/libs/intro.js/7.0.0/introjs.min.js", "js/vendor/introjs.min.js"),
    
    # Additional CSS/JS from templates
    ("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css", "css/vendor/font-awesome.min.css"),
    ("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/webfonts/fa-solid-900.woff2", "fonts/font-awesome/fa-solid-900.woff2"),
    ("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/webfonts/fa-regular-400.woff2", "fonts/font-awesome/fa-regular-400.woff2"),
    ("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/webfonts/fa-brands-400.woff2", "fonts/font-awesome/fa-brands-400.woff2"),
    
    # Chart.js
    ("https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js", "js/vendor/chart.umd.min.js"),
    
    # Morris.js and Raphael
    ("https://cdnjs.cloudflare.com/ajax/libs/morris.js/0.5.1/morris.min.js", "js/vendor/morris.min.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/morris.js/0.5.1/morris.css", "css/vendor/morris.css"),
    ("https://cdnjs.cloudflare.com/ajax/libs/raphael/2.3.0/raphael.min.js", "js/vendor/raphael.min.js"),
    
    # Flot
    ("https://cdnjs.cloudflare.com/ajax/libs/flot/0.8.3/jquery.flot.min.js", "js/vendor/jquery.flot.min.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/flot/0.8.3/jquery.flot.time.min.js", "js/vendor/jquery.flot.time.min.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/flot/0.8.3/jquery.flot.pie.min.js", "js/vendor/jquery.flot.pie.min.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/flot/0.8.3/jquery.flot.stack.min.js", "js/vendor/jquery.flot.stack.min.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/flot/0.8.3/jquery.flot.resize.min.js", "js/vendor/jquery.flot.resize.min.js"),
    
    # D3.js
    ("https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.17/d3.min.js", "js/vendor/d3.min.js"),
    
    # Rickshaw
    ("https://cdnjs.cloudflare.com/ajax/libs/rickshaw/1.6.6/rickshaw.min.js", "js/vendor/rickshaw.min.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/rickshaw/1.6.6/rickshaw.min.css", "css/vendor/rickshaw.css"),
    
    # jQuery AnimateNumber
    ("https://cdnjs.cloudflare.com/ajax/libs/jquery-animateNumber/0.0.14/jquery.animateNumber.min.js", "js/vendor/jquery.animateNumber.min.js"),
    
    # FullCalendar
    ("https://cdn.jsdelivr.net/npm/fullcalendar@6.1.8/index.global.min.js", "js/vendor/fullcalendar.global.min.js"),
    
    # Leaflet
    ("https://unpkg.com/leaflet@1.9.4/dist/leaflet.css", "css/vendor/leaflet.css"),
    ("https://unpkg.com/leaflet@1.9.4/dist/leaflet.js", "js/vendor/leaflet.js"),
    
    # DataTables
    ("https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css", "css/vendor/dataTables.bootstrap5.min.css"),
    ("https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js", "js/vendor/jquery.dataTables.min.js"),
    ("https://cdn.datatables.net/1.13.6/js/dataTables.bootstrap5.min.js", "js/vendor/dataTables.bootstrap5.min.js"),
    
    # Select2
    ("https://cdnjs.cloudflare.com/ajax/libs/select2/4.1.0-rc.0/css/select2.min.css", "css/vendor/select2.min.css"),
    ("https://cdnjs.cloudflare.com/ajax/libs/select2/4.1.0-rc.0/js/select2.min.js", "js/vendor/select2.min.js"),
    
    # Bootstrap Select
    ("https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.14.0-beta2/css/bootstrap-select.min.css", "css/vendor/bootstrap-select.min.css"),
    ("https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.14.0-beta2/js/bootstrap-select.min.js", "js/vendor/bootstrap-select.min.js"),
    
    # Dropzone
    ("https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.3/min/dropzone.min.js", "js/vendor/dropzone.min.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.3/min/dropzone.min.css", "css/vendor/dropzone.min.css"),
    
    # jQuery UI
    ("https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.13.2/jquery-ui.min.js", "js/vendor/jquery-ui.min.js"),
    
    # Moment.js
    ("https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.29.4/moment.min.js", "js/vendor/moment.min.js"),
    
    # Toastr
    ("https://cdnjs.cloudflare.com/ajax/libs/toastr.js/2.1.4/toastr.min.js", "js/vendor/toastr.min.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/toastr.js/2.1.4/toastr.min.css", "css/vendor/toastr.min.css"),
    
    # Animate.css
    ("https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css", "css/vendor/animate.min.css"),
    
    # SweetAlert
    ("https://cdnjs.cloudflare.com/ajax/libs/sweetalert2/11.7.32/sweetalert2.min.js", "js/vendor/sweetalert2.min.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/sweetalert2/11.7.32/sweetalert2.min.css", "css/vendor/sweetalert2.min.css"),
    
    # Magnific Popup
    ("https://cdnjs.cloudflare.com/ajax/libs/magnific-popup.js/1.1.0/jquery.magnific-popup.min.js", "js/vendor/jquery.magnific-popup.min.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/magnific-popup.js/1.1.0/magnific-popup.css", "css/vendor/magnific-popup.css"),
    
    # Google Fonts - download as CSS (will need font files too)
    # We can't easily download Google Fonts, but we'll note them in a separate file
]


def download_file(url, local_path):
    """Download a file from URL to local path."""
    full_path = STATIC_DIR / local_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        print(f"Downloading: {url}")
        urllib.request.urlretrieve(url, full_path)
        print(f"  Saved to: {local_path}")
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def main():
    print(f"Downloading offline assets to: {STATIC_DIR}")
    print("-" * 60)
    
    success_count = 0
    fail_count = 0
    
    for url, local_path in ASSETS:
        if download_file(url, local_path):
            success_count += 1
        else:
            fail_count += 1
    
    print("-" * 60)
    print(f"Downloaded: {success_count} files")
    if fail_count > 0:
        print(f"Failed: {fail_count} files")
    
    # Also download Font Awesome 4.7 (required by some older components)
    print("\nDownloading Font Awesome 4.7...")
    fa4_urls = [
        ("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", "css/vendor/font-awesome-4.7.min.css"),
        ("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/fonts/fontawesome-webfont.eot", "fonts/font-awesome-4.7/fontawesome-webfont.eot"),
        ("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/fonts/fontawesome-webfont.woff", "fonts/font-awesome-4.7/fontawesome-webfont.woff"),
        ("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/fonts/fontawesome-webfont.ttf", "fonts/font-awesome-4.7/fontawesome-webfont.ttf"),
    ]
    for url, path in fa4_urls:
        download_file(url, path)


if __name__ == "__main__":
    main()
