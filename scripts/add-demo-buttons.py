#!/usr/bin/env python3
"""
Script to add demo buttons to AKATRON website pages
This script automates the integration of "Request Demo" buttons across all pages
"""

import re

# Button Group CSS to add after line 218
BUTTON_GROUP_CSS = """
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

        /* Primary Button - Uses existing .hero .btn styles */
        .btn-primary {
            /* Inherits from .hero .btn */
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

# Hero button replacement
OLD_HERO_BUTTON = '<a href="#services" class="btn"><span>Explore Services</span></a>'
NEW_HERO_BUTTON = '''<div class="btn-group">
            <a href="#services" class="btn btn-primary"><span>Explore Services</span></a>
            <a href="request-demo.html" class="btn btn-secondary"><span>Request Demo</span></a>
        </div>'''

def update_index_html(content):
    """Update index.html with button group CSS and new hero buttons"""
    
    # Add button group CSS after .hero .btn span styles
    css_marker = '.hero .btn span {\n            position: relative;\n            z-index: 1;\n        }'
    if css_marker in content:
        content = content.replace(css_marker, css_marker + '\n' + BUTTON_GROUP_CSS)
        print("✅ Added button group CSS")
    else:
        print("⚠️  Could not find CSS insertion point")
    
    # Replace hero button
    if OLD_HERO_BUTTON in content:
        content = content.replace(OLD_HERO_BUTTON, NEW_HERO_BUTTON)
        print("✅ Updated hero button")
    else:
        print("⚠️  Could not find hero button")
    
    return content

def add_service_page_buttons(content, page_name):
    """Add demo buttons to service pages"""
    # This would need to be customized per page
    # For now, return instructions
    return content

if __name__ == "__main__":
    print("AKATRON Demo Button Integration Script")
    print("=" * 50)
    print("\nThis script will:")
    print("1. Add button group CSS to index.html")
    print("2. Update hero section with demo button")
    print("3. Provide instructions for service pages")
    print("\nRun this script after downloading index.html")
    print("Then upload the modified file back to GitHub")
