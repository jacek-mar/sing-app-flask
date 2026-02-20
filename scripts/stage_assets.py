#!/usr/bin/env python
"""
Stage Assets Script

Copies static assets and templates from sing-app-html5-master to the Flask project.
This script should be run from the project root directory.

Usage:
    python scripts/stage_assets.py
"""

import os
import shutil
import urllib.request
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
SING_APP_SRC = PROJECT_ROOT / "sing-app-html5-master" / "src"
SING_APP_DIST = PROJECT_ROOT / "sing-app-html5-master" / "dist"
FLASK_APP = PROJECT_ROOT / "sing-app-flask"
STATIC_DIR = FLASK_APP / "static"
TEMPLATES_DIR = FLASK_APP / "templates"

# Asset mappings: (source_subdir, destination_subdir)
# None means copy to root of destination
ASSET_MAPPINGS = [
    # Static assets
    ("demo", None),        # demo/ -> static/demo/
    ("fonts", None),       # fonts/ -> static/fonts/
    ("img", None),         # img/ -> static/img/
    ("js", None),          # js/ -> static/js/
    ("sass", None),        # sass/ -> static/sass/
    # Templates
    ("pages", None),       # pages/ -> templates/
    ("partials", None),    # partials/ -> templates/partials/
]

# Vendor JS libraries to download (URL, destination_rel_path)
VENDOR_DOWNLOADS = [
    ("https://code.jquery.com/jquery-3.6.4.min.js", "js/vendor/jquery.min.js"),
    ("https://unpkg.com/popper.js@1.16.1/dist/umd/popper.min.js", "js/vendor/popper.min.js"),
    ("https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js", "js/vendor/bootstrap.min.js"),
]

# Prebuilt CSS files to copy from dist/
PREBUILT_CSS = [
    "application.min.css",
    "application-dark.min.css",
]


def ensure_dir(path: Path):
    """Ensure directory exists."""
    path.mkdir(parents=True, exist_ok=True)
    print(f"  Created: {path.relative_to(PROJECT_ROOT)}")


def copy_tree(src: Path, dst: Path, verbose: bool = True):
    """Copy entire directory tree, overwriting existing files."""
    if not src.exists():
        print(f"  WARNING: Source not found: {src.relative_to(PROJECT_ROOT)}")
        return False
    
    # Remove destination if exists (for clean copy)
    if dst.exists():
        shutil.rmtree(dst)
    
    # Copy tree
    shutil.copytree(src, dst)
    if verbose:
        print(f"  Copied: {src.relative_to(PROJECT_ROOT)} -> {dst.relative_to(PROJECT_ROOT)}")
    return True


def copy_file(src: Path, dst: Path, verbose: bool = True):
    """Copy a single file."""
    if not src.exists():
        print(f"  WARNING: Source not found: {src}")
        return False
    
    # Ensure destination directory exists
    dst.parent.mkdir(parents=True, exist_ok=True)
    
    shutil.copy2(src, dst)
    if verbose:
        print(f"  Copied: {src.relative_to(PROJECT_ROOT)} -> {dst.relative_to(PROJECT_ROOT)}")
    return True


def download_file(url: str, dst: Path, verbose: bool = True):
    """Download a file from URL."""
    # Ensure destination directory exists
    dst.parent.mkdir(parents=True, exist_ok=True)
    
    if dst.exists():
        if verbose:
            print(f"  Exists (skip): {dst.relative_to(PROJECT_ROOT)}")
        return True
    
    try:
        if verbose:
            print(f"  Downloading: {dst.name}...")
        urllib.request.urlretrieve(url, dst)
        size_kb = dst.stat().st_size // 1024
        if verbose:
            print(f"  OK: {dst.name} ({size_kb} KB)")
        return True
    except Exception as e:
        print(f"  FAILED: {dst.name} — {e}")
        print(f"    Manual download URL: {url}")
        return False


def main():
    print("=" * 60)
    print("Staging Assets from Sing App HTML5")
    print("=" * 60)
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Source: {SING_APP_SRC}")
    print()
    
    # Ensure destination directories exist
    print("Creating destination directories...")
    ensure_dir(STATIC_DIR)
    ensure_dir(TEMPLATES_DIR)
    ensure_dir(TEMPLATES_DIR / "partials")
    ensure_dir(STATIC_DIR / "js" / "vendor")
    print()
    
    # === Task 1: Copy pre-built CSS from dist/css/ ===
    print("Copying pre-built CSS from dist/css/...")
    css_src_dir = SING_APP_DIST / "css"
    css_dst_dir = STATIC_DIR / "css"
    ensure_dir(css_dst_dir)
    
    for css_file in PREBUILT_CSS:
        src_file = css_src_dir / css_file
        dst_file = css_dst_dir / css_file
        if copy_file(src_file, dst_file):
            print(f"    {css_file}: OK ({dst_file.stat().st_size // 1024} KB)")
        else:
            print(f"    {css_file}: SKIPPED (not found)")
    print()
    
    # Copy assets from src/ FIRST
    print("Copying assets from src/...")
    success_count = 0
    
    for src_subdir, dst_subdir in ASSET_MAPPINGS:
        src = SING_APP_SRC / src_subdir
        
        if dst_subdir:
            dst = STATIC_DIR / dst_subdir if src_subdir in ["demo", "fonts", "img", "js", "sass"] else TEMPLATES_DIR / dst_subdir
        else:
            # Determine destination based on source type
            if src_subdir in ["pages", "partials"]:
                dst = TEMPLATES_DIR / src_subdir
            else:
                dst = STATIC_DIR / src_subdir
        
        if copy_tree(src, dst):
            success_count += 1
    
    print()
    
    # === Task 2: Download vendor JS libraries AFTER copying src ===
    print("Downloading vendor JS libraries...")
    vendor_success = 0
    for url, rel_path in VENDOR_DOWNLOADS:
        dst = STATIC_DIR / rel_path
        if download_file(url, dst):
            vendor_success += 1
    print(f"    Downloaded: {vendor_success}/{len(VENDOR_DOWNLOADS)}")
    print()
    
    print("=" * 60)
    print(f"Completed: {success_count}/{len(ASSET_MAPPINGS)} asset groups copied")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Review copied templates in templates/")
    print("  2. Run: cd sing-app-flask && .venv\\Scripts\\flask run")
    print("  3. Visit http://localhost:49251")


if __name__ == "__main__":
    main()
