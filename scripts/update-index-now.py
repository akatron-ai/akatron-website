#!/usr/bin/env python3
"""
Automated script to add demo button to index.html
This script will:
1. Download current index.html
2. Add button group CSS after line 219
3. Replace single button with button group on line 454
4. Update the file on GitHub
"""

import re

# CSS to add after line 219 (after .hero .btn span block)
BUTTON_CSS = """        
        /* Button Group Styles */
        .btn-group {
            position: relative;
            z-index: 1;
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
        }

        /* Secondary Button (Outline Gold) */
        .btn-secondary {
            background: transparent !important;
            color: #d4af37 !important;
            border: 2px solid #d4af37 !important;
            box-shadow: 
                0 10px 40px rgba(212, 175, 55, 0.2),
                inset 0 0 0 rgba(212, 175, 55, 0.1) !important;
        }

        .btn-secondary::before {
            background: linear-gradient(135deg, rgba(212, 175, 55, 0.1), rgba(244, 228, 166, 0.1)) !important;
        }

        .btn-secondary:hover {
            background: rgba(212, 175, 55, 0.1) !important;
            border-color: #f4e4a6 !important;
            color: #f4e4a6 !important;
            box-shadow: 
                0 15px 50px rgba(212, 175, 55, 0.4),
                0 0 0 1px rgba(212, 175, 55, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
        }

        @media (max-width: 768px) {
            .btn-group {
                flex-direction: column;
                width: 100%;
            }
            
            .btn-group .btn {
                width: 100%;
                max-width: 300px;
            }
        }
"""

# Old button HTML to find and replace
OLD_BUTTON = '        <a href="#services" class="btn"><span>Explore Services</span></a>'

# New button group HTML
NEW_BUTTON = '''        <div class="btn-group">
            <a href="#services" class="btn btn-primary"><span>Explore Services</span></a>
            <a href="request-demo.html" class="btn btn-secondary"><span>Request Demo</span></a>
        </div>'''

def update_index_html(content):
    """Update index.html content with demo button changes"""
    
    # Step 1: Add CSS after .hero .btn span block
    css_marker = """        .hero .btn span {
            position: relative;
            z-index: 1;
        }"""
    
    if css_marker in content and BUTTON_CSS.strip() not in content:
        content = content.replace(css_marker, css_marker + BUTTON_CSS)
        print("✅ Added button group CSS")
    else:
        print("⚠️  CSS already added or marker not found")
    
    # Step 2: Replace single button with button group
    if OLD_BUTTON in content:
        content = content.replace(OLD_BUTTON, NEW_BUTTON)
        print("✅ Replaced hero button with button group")
    else:
        print("⚠️  Button already updated or not found")
    
    return content

# Instructions for manual use
print("""
AKATRON Demo Button Update Script
==================================

This script contains the logic to update index.html.

To use with GitHub API:
1. Download current index.html
2. Run: updated_content = update_index_html(current_content)
3. Upload updated_content back to GitHub

Or use the manual steps in MANUAL_UPDATE_STEPS.md
""")
