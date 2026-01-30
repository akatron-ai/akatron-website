#!/usr/bin/env python3
"""
AKATRON Website - Fix All Pricing Buttons
Replaces all href="#contact" with href="payment.html"
"""

import os
import sys

# Files to update
FILES = [
    'osint.html',
    'threat-intelligence.html',
    'email-risk.html',
    'pricing.html',
    'about.html'
]

def fix_file(filename):
    """Fix pricing buttons in a single file"""
    if not os.path.exists(filename):
        print(f"❌ File not found: {filename}")
        return 0
    
    # Read file
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count replacements
    count = content.count('href="#contact"')
    
    if count == 0:
        print(f"⏭️  {filename}: No changes needed")
        return 0
    
    # Replace
    new_content = content.replace('href="#contact"', 'href="payment.html"')
    
    # Write back
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ {filename}: Fixed {count} button(s)")
    return count

def main():
    """Main execution"""
    print("🔧 AKATRON - Fixing all pricing button links...")
    print()
    
    total = 0
    for filename in FILES:
        total += fix_file(filename)
    
    print()
    print("━" * 50)
    print(f"✨ COMPLETE! Fixed {total} button(s) total")
    print()
    
    if total > 0:
        print("Next steps:")
        print("1. Review: git diff")
        print("2. Commit: git add . && git commit -m '🔗 Fix pricing buttons'")
        print("3. Push: git push")
        print()
        print("🎉 Website will update in 1-2 minutes!")
    
    return 0 if total > 0 else 1

if __name__ == '__main__':
    sys.exit(main())
