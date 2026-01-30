#!/usr/bin/env python3
"""
AKATRON Website - Update ALL Contact Information
Finds and replaces ALL instances of old contact info with correct details
"""

import os
import sys
import re
import glob

# Correct contact information
CORRECT_EMAIL = "arpit.akatron@gmail.com"
CORRECT_PHONE = "+91 9214297017"
CORRECT_PHONE_DISPLAY = "+91 9214297017"
CORRECT_WHATSAPP = "919214297017"

# Old/incorrect contact information patterns to find and replace
OLD_EMAILS = [
    "arpitkatiayar261@gmail.com",
    "contact@akatron.com",
    "info@akatron.com",
    "support@akatron.com"
]

OLD_PHONES = [
    "+91 91512 35481",
    "+919151235481",
    "91512 35481",
    "9151235481",
    "+91-91512-35481"
]

def find_all_html_files():
    """Find all HTML files in the repository"""
    html_files = []
    for file in glob.glob("*.html"):
        html_files.append(file)
    for file in glob.glob("**/*.html", recursive=True):
        if not file.startswith('.'):
            html_files.append(file)
    return list(set(html_files))

def update_contact_info(filename):
    """Update contact information in a single file"""
    if not os.path.exists(filename):
        return False, "File not found"
    
    try:
        # Read file
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # Replace old emails
        for old_email in OLD_EMAILS:
            if old_email in content:
                content = content.replace(old_email, CORRECT_EMAIL)
                changes_made.append(f"Email: {old_email} → {CORRECT_EMAIL}")
        
        # Replace old phone numbers
        for old_phone in OLD_PHONES:
            if old_phone in content:
                content = content.replace(old_phone, CORRECT_PHONE_DISPLAY)
                changes_made.append(f"Phone: {old_phone} → {CORRECT_PHONE_DISPLAY}")
        
        # Update WhatsApp links
        whatsapp_patterns = [
            (r'https://wa\.me/\d+', f'https://wa.me/{CORRECT_WHATSAPP}'),
            (r'wa\.me/\d+', f'wa.me/{CORRECT_WHATSAPP}')
        ]
        
        for pattern, replacement in whatsapp_patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                changes_made.append(f"WhatsApp link updated")
        
        # Update tel: links
        tel_patterns = [
            (r'tel:\+?\d+', f'tel:{CORRECT_PHONE}'),
        ]
        
        for pattern, replacement in tel_patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                changes_made.append(f"Tel link updated")
        
        # Update mailto: links
        mailto_patterns = [
            (r'mailto:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', f'mailto:{CORRECT_EMAIL}'),
        ]
        
        for pattern, replacement in mailto_patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                changes_made.append(f"Mailto link updated")
        
        # Check if anything changed
        if content == original_content:
            return False, "No changes needed"
        
        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, changes_made
        
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Main execution"""
    print("🔧 AKATRON - Updating ALL Contact Information...")
    print()
    print("Correct Contact Details:")
    print(f"  📧 Email: {CORRECT_EMAIL}")
    print(f"  📱 Phone: {CORRECT_PHONE_DISPLAY}")
    print(f"  💬 WhatsApp: {CORRECT_WHATSAPP}")
    print()
    print("Searching for old contact information...")
    print()
    
    html_files = find_all_html_files()
    print(f"Found {len(html_files)} HTML files to check")
    print()
    
    updated_files = 0
    total_changes = 0
    
    for filename in sorted(html_files):
        success, result = update_contact_info(filename)
        
        if success:
            updated_files += 1
            print(f"✅ {filename}:")
            for change in result:
                print(f"   - {change}")
                total_changes += 1
            print()
        elif "No changes needed" not in result:
            print(f"⚠️  {filename}: {result}")
    
    print()
    print("━" * 60)
    print(f"✨ COMPLETE!")
    print(f"   Updated: {updated_files} file(s)")
    print(f"   Total changes: {total_changes}")
    print()
    
    if updated_files > 0:
        print("Next steps:")
        print("1. Review: git diff")
        print("2. Commit: git add . && git commit -m '📞 Update all contact information'")
        print("3. Push: git push")
        print()
        print("🎉 All contact information will be updated!")
    else:
        print("✅ All contact information is already correct!")
    
    return 0 if updated_files > 0 else 1

if __name__ == '__main__':
    sys.exit(main())
