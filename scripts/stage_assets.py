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
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
SING_APP_SRC = PROJECT_ROOT / "sing-app-html5-master" / "src"
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
    print()
    
    # Copy assets
    print("Copying assets...")
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
    print("=" * 60)
    print(f"Completed: {success_count}/{len(ASSET_MAPPINGS)} asset groups copied")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Review copied templates in templates/")
    print("  2. Run: cd sing-app-flask && .venv\\Scripts\\flask run")
    print("  3. Visit http://localhost:5000/examples/dashboard")


if __name__ == "__main__":
    main()
