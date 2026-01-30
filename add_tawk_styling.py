#!/usr/bin/env python3
"""
AKATRON Website - Add Professional Tawk.to Styling
Adds custom CSS link to all HTML pages for professional chat widget styling
"""

import os
import sys
import re

# HTML files to update
HTML_FILES = [
    'index.html',
    'osint.html',
    'threat-intelligence.html',
    'email-risk.html',
    'pricing.html',
    'about.html',
    'blog.html',
    'request-demo.html',
    'payment.html',
    'privacy-policy.html',
    'terms-of-service.html',
    'disclaimer.html'
]

# CSS link to add
TAWK_CSS_LINK = '    <link rel="stylesheet" href="css/tawk-custom.css">'

def add_tawk_styling(filename):
    """Add Tawk.to custom styling CSS link to a file"""
    if not os.path.exists(filename):
        print(f"⏭️  {filename}: File not found, skipping")
        return False
    
    # Read file
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already added
    if 'tawk-custom.css' in content:
        print(f"⏭️  {filename}: Already has Tawk styling")
        return False
    
    # Check if file has Tawk.to script
    if 'tawk.to' not in content.lower():
        print(f"⏭️  {filename}: No Tawk.to widget found")
        return False
    
    # Find the last stylesheet link before </head>
    # We'll add our CSS right before </head>
    if '</head>' in content:
        # Add before closing head tag
        new_content = content.replace('</head>', f'{TAWK_CSS_LINK}\n</head>')
        
        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ {filename}: Added professional Tawk styling")
        return True
    else:
        print(f"❌ {filename}: Could not find </head> tag")
        return False

def main():
    """Main execution"""
    print("🎨 AKATRON - Adding Professional Tawk.to Styling...")
    print()
    
    updated = 0
    for filename in HTML_FILES:
        if add_tawk_styling(filename):
            updated += 1
    
    print()
    print("━" * 50)
    print(f"✨ COMPLETE! Updated {updated} file(s)")
    print()
    
    if updated > 0:
        print("Next steps:")
        print("1. Review: git diff")
        print("2. Commit: git add . && git commit -m '🎨 Add professional Tawk.to styling'")
        print("3. Push: git push")
        print()
        print("🎉 Chat widget will look professional!")
    
    return 0 if updated > 0 else 1

if __name__ == '__main__':
    sys.exit(main())
