#!/usr/bin/env python3
"""
Fix all pricing buttons to redirect to payment.html instead of #contact
This script updates all HTML pages in the repository
"""

import re
import os
from pathlib import Path

# Pages to update
PAGES = [
    'osint.html',
    'threat-intelligence.html',
    'email-risk.html',
    'pricing.html',
    'about.html'
]

def fix_pricing_buttons(content):
    """Fix all pricing button links to point to payment.html"""
    
    # Pattern 1: href="#contact" in buttons
    content = re.sub(
        r'href="#contact"',
        r'href="payment.html"',
        content,
        flags=re.IGNORECASE
    )
    
    # Pattern 2: href="#pricing" in buttons
    content = re.sub(
        r'href="#pricing"',
        r'href="payment.html"',
        content,
        flags=re.IGNORECASE
    )
    
    # Pattern 3: onclick="location.href='#contact'"
    content = re.sub(
        r"onclick=\"location\.href='#contact'\"",
        r'onclick="location.href=\'payment.html\'"',
        content,
        flags=re.IGNORECASE
    )
    
    # Pattern 4: onclick="window.location.href='#contact'"
    content = re.sub(
        r"onclick=\"window\.location\.href='#contact'\"",
        r'onclick="window.location.href=\'payment.html\'"',
        content,
        flags=re.IGNORECASE
    )
    
    return content

def add_request_demo_to_nav(content):
    """Add Request Demo link to navigation if missing"""
    
    # Check if Request Demo already exists
    if 'request-demo.html' in content:
        return content
    
    # Pattern to find navigation and add Request Demo before Payment
    nav_pattern = r'(<a href="pricing\.html">Pricing</a>)'
    replacement = r'\1\n            <a href="request-demo.html">Request Demo</a>'
    
    content = re.sub(nav_pattern, replacement, content)
    
    return content

def main():
    print("🔧 Fixing all pricing buttons across all pages...")
    print("=" * 60)
    
    for page in PAGES:
        if os.path.exists(page):
            print(f"\n📄 Processing {page}...")
            
            with open(page, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix pricing buttons
            original_content = content
            content = fix_pricing_buttons(content)
            content = add_request_demo_to_nav(content)
            
            if content != original_content:
                with open(page, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"   ✅ Updated {page}")
            else:
                print(f"   ℹ️  No changes needed for {page}")
        else:
            print(f"   ⚠️  {page} not found")
    
    print("\n" + "=" * 60)
    print("✅ All pages updated successfully!")
    print("\nChanges made:")
    print("  • All pricing buttons now redirect to payment.html")
    print("  • Request Demo added to navigation (if missing)")
    print("  • All #contact links changed to payment.html")

if __name__ == "__main__":
    main()
