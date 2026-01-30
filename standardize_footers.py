#!/usr/bin/env python3
"""
AKATRON Website - Standardize All Footers
Makes all page footers match the professional OSINT page footer
"""

import os
import sys
import re

# HTML files to update
HTML_FILES = [
    'index.html',
    'pricing.html',
    'request-demo.html',
    'payment.html',
    'about.html',
    'blog.html',
    'privacy-policy.html',
    'terms-of-service.html',
    'disclaimer.html'
]

# Standard footer HTML (from OSINT page)
STANDARD_FOOTER = '''    <footer class="site-footer">
        <p><strong>AKATRON</strong> — Elite Cybersecurity & OSINT Intelligence</p>
        <p>
            <a href="privacy-policy.html" style="color: #DAA520; text-decoration: none; margin: 0 10px;">Privacy Policy</a> | 
            <a href="terms-of-service.html" style="color: #DAA520; text-decoration: none; margin: 0 10px;">Terms of Service</a> | 
            <a href="disclaimer.html" style="color: #DAA520; text-decoration: none; margin: 0 10px;">Disclaimer</a>
        </p>
        <p>Delivering confidential, ethical, and actionable intelligence.</p>
        <p>© 2025 AKATRON. All rights reserved.</p>
        <p class="disclaimer">
            AKATRON provides cybersecurity intelligence and OSINT research for defensive, ethical, and lawful purposes only.
        </p>
    </footer>'''

def standardize_footer(filename):
    """Standardize footer in a single file"""
    if not os.path.exists(filename):
        print(f"⏭️  {filename}: File not found, skipping")
        return False
    
    # Read file
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find footer section - look for <footer or footer class
    footer_patterns = [
        r'<footer[^>]*>.*?</footer>',
        r'<div[^>]*class="footer"[^>]*>.*?</div>',
        r'<div[^>]*id="footer"[^>]*>.*?</div>'
    ]
    
    found_footer = False
    new_content = content
    
    for pattern in footer_patterns:
        if re.search(pattern, content, re.DOTALL | re.IGNORECASE):
            # Replace footer
            new_content = re.sub(pattern, STANDARD_FOOTER, content, flags=re.DOTALL | re.IGNORECASE)
            found_footer = True
            break
    
    if not found_footer:
        print(f"⚠️  {filename}: No footer found")
        return False
    
    # Check if anything changed
    if new_content == content:
        print(f"⏭️  {filename}: Footer already standardized")
        return False
    
    # Write back
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ {filename}: Footer standardized")
    return True

def main():
    """Main execution"""
    print("🔧 AKATRON - Standardizing All Page Footers...")
    print()
    print("Target footer style: OSINT page (professional)")
    print()
    
    updated = 0
    for filename in HTML_FILES:
        if standardize_footer(filename):
            updated += 1
    
    print()
    print("━" * 50)
    print(f"✨ COMPLETE! Updated {updated} file(s)")
    print()
    
    if updated > 0:
        print("Next steps:")
        print("1. Review: git diff")
        print("2. Commit: git add . && git commit -m '🎨 Standardize all footers'")
        print("3. Push: git push")
        print()
        print("🎉 All footers will match the professional OSINT style!")
    
    return 0 if updated > 0 else 1

if __name__ == '__main__':
    sys.exit(main())
