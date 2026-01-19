#!/usr/bin/env python3
"""
AKATRON Footer Update Script
Automatically updates the footer section in all HTML files with LinkedIn profile
"""

import re
import os
from pathlib import Path

# New footer HTML
NEW_FOOTER = '''    <!-- FOOTER -->
    <footer class="site-footer">
        <p><strong>AKATRON</strong> — Elite Cybersecurity & OSINT Intelligence</p>
        
        <!-- Social Media Links -->
        <div style="margin: 20px 0;">
            <a href="https://www.linkedin.com/in/arpit-katiyar-akatron" target="_blank" rel="noopener noreferrer" style="color: #DAA520; text-decoration: none; margin: 0 15px; font-size: 16px; transition: all 0.3s ease;">
                <span style="display: inline-flex; align-items: center; gap: 8px;">
                    <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                    </svg>
                    LinkedIn
                </span>
            </a>
            <a href="https://twitter.com/AKATRON_Cyber" target="_blank" rel="noopener noreferrer" style="color: #DAA520; text-decoration: none; margin: 0 15px; font-size: 16px; transition: all 0.3s ease;">
                <span style="display: inline-flex; align-items: center; gap: 8px;">
                    <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                    </svg>
                    Twitter
                </span>
            </a>
            <a href="https://github.com/akatron-ai" target="_blank" rel="noopener noreferrer" style="color: #DAA520; text-decoration: none; margin: 0 15px; font-size: 16px; transition: all 0.3s ease;">
                <span style="display: inline-flex; align-items: center; gap: 8px;">
                    <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                    </svg>
                    GitHub
                </span>
            </a>
        </div>
        
        <p>
            <a href="privacy-policy.html" style="color: #DAA520; text-decoration: none; margin: 0 10px;">Privacy Policy</a> | 
            <a href="terms-of-service.html" style="color: #DAA520; text-decoration: none; margin: 0 10px;">Terms of Service</a> | 
            <a href="disclaimer.html" style="color: #DAA520; text-decoration: none; margin: 0 10px;">Disclaimer</a> | 
            <a href="blog.html" style="color: #DAA520; text-decoration: none; margin: 0 10px;">Blog</a>
        </p>
        <p>Delivering confidential, ethical, and actionable intelligence.</p>
        <p>© 2026 AKATRON. All rights reserved.</p>
        <p class="disclaimer">
            AKATRON provides cybersecurity intelligence and OSINT research for defensive, ethical, and lawful purposes only.
        </p>
    </footer>'''

# Files to update
HTML_FILES = [
    'index.html',
    'osint.html',
    'email-risk.html',
    'threat-intelligence.html',
    'blog.html',
    'privacy-policy.html',
    'terms-of-service.html',
    'disclaimer.html'
]

def update_footer(file_path):
    """Update footer in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match the footer section
        pattern = r'    <!-- FOOTER -->.*?</footer>'
        
        # Replace the footer
        updated_content = re.sub(
            pattern,
            NEW_FOOTER,
            content,
            flags=re.DOTALL
        )
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✅ Updated: {file_path}")
        return True
        
    except FileNotFoundError:
        print(f"⚠️  File not found: {file_path}")
        return False
    except Exception as e:
        print(f"❌ Error updating {file_path}: {str(e)}")
        return False

def main():
    """Main function to update all HTML files"""
    print("🚀 AKATRON Footer Update Script")
    print("=" * 50)
    print()
    
    updated_count = 0
    failed_count = 0
    
    for html_file in HTML_FILES:
        if update_footer(html_file):
            updated_count += 1
        else:
            failed_count += 1
    
    print()
    print("=" * 50)
    print(f"✅ Successfully updated: {updated_count} files")
    if failed_count > 0:
        print(f"❌ Failed to update: {failed_count} files")
    print()
    print("🎉 Footer update complete!")
    print()
    print("What was added:")
    print("  ✅ LinkedIn profile: https://www.linkedin.com/in/arpit-katiyar-akatron")
    print("  ✅ Twitter link (placeholder)")
    print("  ✅ GitHub organization link")
    print("  ✅ Blog link in footer navigation")
    print("  ✅ Updated copyright year to 2026")
    print("  ✅ Professional social media icons")

if __name__ == "__main__":
    main()
