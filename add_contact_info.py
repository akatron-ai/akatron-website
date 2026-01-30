#!/usr/bin/env python3
"""
AKATRON Website - Add Contact Information
Adds professional contact section with correct email and phone
"""

import os
import sys
import re

# HTML files to update
HTML_FILES = [
    'index.html',
    'about.html',
    'request-demo.html'
]

# Contact section HTML with correct information
CONTACT_SECTION = '''
    <!-- Contact Information Section -->
    <section class="section" id="contact" style="background: var(--bg-secondary); padding: 80px 20px;">
        <div class="container" style="max-width: 900px;">
            <h2 style="color: #DAA520; font-size: 42px; margin-bottom: 20px; text-align: center;">Get In Touch</h2>
            <p style="color: #b8bcc8; font-size: 18px; text-align: center; margin-bottom: 50px; max-width: 700px; margin-left: auto; margin-right: auto;">
                Ready to secure your digital assets? Contact us for consultations, investigations, or custom security solutions.
            </p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; margin-bottom: 40px;">
                
                <!-- Email Card -->
                <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 35px; text-align: center; transition: all 0.3s ease;">
                    <div style="font-size: 48px; margin-bottom: 20px;">📧</div>
                    <h3 style="color: #DAA520; margin-bottom: 15px; font-size: 20px;">Email</h3>
                    <a href="mailto:arpit.akatron@gmail.com" style="color: #b8bcc8; text-decoration: none; font-size: 16px; word-break: break-all; transition: color 0.3s ease;">
                        arpit.akatron@gmail.com
                    </a>
                </div>

                <!-- Phone Card -->
                <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 35px; text-align: center; transition: all 0.3s ease;">
                    <div style="font-size: 48px; margin-bottom: 20px;">📱</div>
                    <h3 style="color: #DAA520; margin-bottom: 15px; font-size: 20px;">Phone</h3>
                    <a href="tel:+919214297017" style="color: #b8bcc8; text-decoration: none; font-size: 16px; transition: color 0.3s ease;">
                        +91 9214297017
                    </a>
                </div>

                <!-- WhatsApp Card -->
                <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 35px; text-align: center; transition: all 0.3s ease;">
                    <div style="font-size: 48px; margin-bottom: 20px;">💬</div>
                    <h3 style="color: #DAA520; margin-bottom: 15px; font-size: 20px;">WhatsApp</h3>
                    <a href="https://wa.me/919214297017" target="_blank" style="color: #b8bcc8; text-decoration: none; font-size: 16px; transition: color 0.3s ease;">
                        +91 9214297017
                    </a>
                </div>

            </div>

            <!-- Quick Action Buttons -->
            <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; margin-top: 40px;">
                <a href="request-demo.html" style="background: #DAA520; color: #0a0b0f; padding: 15px 40px; border-radius: 8px; text-decoration: none; font-weight: 700; font-size: 16px; display: inline-block; transition: all 0.3s ease;">
                    Request Demo →
                </a>
                <a href="pricing.html" style="background: transparent; border: 2px solid #DAA520; color: #DAA520; padding: 15px 40px; border-radius: 8px; text-decoration: none; font-weight: 700; font-size: 16px; display: inline-block; transition: all 0.3s ease;">
                    View Pricing →
                </a>
            </div>
        </div>
    </section>
'''

def add_contact_section(filename):
    """Add contact section to a file before the footer"""
    if not os.path.exists(filename):
        print(f"⏭️  {filename}: File not found, skipping")
        return False
    
    # Read file
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if contact section already exists
    if 'id="contact"' in content or 'Get In Touch' in content:
        print(f"⏭️  {filename}: Contact section already exists")
        return False
    
    # Find footer and insert contact section before it
    if '<footer class="site-footer">' in content:
        new_content = content.replace(
            '<footer class="site-footer">',
            CONTACT_SECTION + '\n    <footer class="site-footer">'
        )
        
        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ {filename}: Added contact section")
        return True
    else:
        print(f"❌ {filename}: Could not find footer")
        return False

def main():
    """Main execution"""
    print("📞 AKATRON - Adding Contact Information...")
    print()
    print("Contact Details:")
    print("  📧 Email: arpit.akatron@gmail.com")
    print("  📱 Phone: +91 9214297017")
    print("  💬 WhatsApp: +91 9214297017")
    print()
    
    updated = 0
    for filename in HTML_FILES:
        if add_contact_section(filename):
            updated += 1
    
    print()
    print("━" * 50)
    print(f"✨ COMPLETE! Updated {updated} file(s)")
    print()
    
    if updated > 0:
        print("Next steps:")
        print("1. Review: git diff")
        print("2. Commit: git add . && git commit -m '📞 Add contact information section'")
        print("3. Push: git push")
        print()
        print("🎉 Contact information is now live!")
    
    return 0 if updated > 0 else 1

if __name__ == '__main__':
    sys.exit(main())
