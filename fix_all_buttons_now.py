#!/usr/bin/env python3
"""
AKATRON Website - Fix All Pricing Buttons
Run this script to fix all #contact links to payment.html

Usage:
    python3 fix_all_buttons_now.py
"""

import os
import sys
from pathlib import Path

# Files to fix
FILES_TO_FIX = [
    "osint.html",
    "threat-intelligence.html",
    "email-risk.html",
    "pricing.html",
    "about.html"
]

def fix_file(filepath):
    """Fix pricing buttons in a single file"""
    try:
        # Read file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count occurrences
        before_count = content.count('href="#contact"')
        
        if before_count == 0:
            return 0, "No changes needed"
        
        # Replace all occurrences
        new_content = content.replace('href="#contact"', 'href="payment.html"')
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        # Count after
        after_count = new_content.count('href="#contact"')
        fixed_count = before_count - after_count
        
        return fixed_count, "Success"
        
    except Exception as e:
        return 0, f"Error: {str(e)}"

def main():
    print("🚀 AKATRON Website - Pricing Button Fixer")
    print("=" * 50)
    print()
    
    # Check if we're in the right directory
    if not os.path.exists("index.html"):
        print("❌ Error: Please run this script from the repository root")
        print("   (The directory containing index.html)")
        sys.exit(1)
    
    print("📂 Working directory:", os.getcwd())
    print()
    
    total_fixed = 0
    success_count = 0
    
    for filename in FILES_TO_FIX:
        print(f"📄 Processing: {filename}")
        
        if not os.path.exists(filename):
            print(f"   ⚠️  File not found")
            print()
            continue
        
        fixed_count, status = fix_file(filename)
        
        if "Success" in status:
            print(f"   ✅ Fixed {fixed_count} button(s)")
            total_fixed += fixed_count
            success_count += 1
        else:
            print(f"   ℹ️  {status}")
        
        print()
    
    print("=" * 50)
    print("✅ Complete!")
    print()
    print(f"Summary:")
    print(f"  • Files processed: {success_count}/{len(FILES_TO_FIX)}")
    print(f"  • Total buttons fixed: {total_fixed}")
    print()
    print("Next steps:")
    print("  1. Review changes: git diff")
    print("  2. Commit: git add . && git commit -m '🔗 Fix all pricing buttons'")
    print("  3. Push: git push")
    print()
    print("🎉 All pricing buttons now redirect to payment.html!")

if __name__ == "__main__":
    main()
