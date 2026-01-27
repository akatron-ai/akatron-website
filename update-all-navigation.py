#!/usr/bin/env python3
"""
Automated Navigation Update Script for AKATRON Website
Updates navigation menus across all HTML pages to include Pricing and About links
"""

import re
from pathlib import Path

# Define the files that need navigation updates
FILES_TO_UPDATE = [
    'index.html',
    'osint.html',
    'threat-intelligence.html',
    'email-risk.html',
    'blog.html'
]

# Old navigation pattern (regex to match various formats)
OLD_NAV_PATTERN = r'<nav>\s*<a href="index\.html"[^>]*>Home</a>\s*<a href="osint\.html"[^>]*>OSINT</a>\s*<a href="threat-intelligence\.html"[^>]*>Threat Intel</a>\s*<a href="email-risk\.html"[^>]*>Email Risk</a>\s*<a href="blog\.html"[^>]*>Blog</a>\s*<a href="#contact"[^>]*>Contact</a>\s*</nav>'

# Navigation templates for each page
NAV_TEMPLATES = {
    'index.html': '''<nav>
            <a href="index.html" class="active">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>''',
    
    'osint.html': '''<nav>
            <a href="index.html">Home</a>
            <a href="osint.html" class="active">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>''',
    
    'threat-intelligence.html': '''<nav>
            <a href="index.html">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html" class="active">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>''',
    
    'email-risk.html': '''<nav>
            <a href="index.html">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html" class="active">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>''',
    
    'blog.html': '''<nav>
            <a href="index.html">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html" class="active">Blog</a>
            <a href="about.html">About</a>
        </nav>'''
}

def update_navigation(file_path):
    """Update navigation in a single HTML file"""
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = Path(file_path).name
        
        # Check if file needs updating
        if filename not in NAV_TEMPLATES:
            print(f"⏭️  Skipping {filename} - no template defined")
            return False
        
        # Find and replace navigation
        # More flexible pattern that handles whitespace variations
        nav_pattern = r'<nav>.*?</nav>'
        
        if not re.search(nav_pattern, content, re.DOTALL):
            print(f"❌ No navigation found in {filename}")
            return False
        
        # Replace with new navigation
        new_content = re.sub(
            nav_pattern,
            NAV_TEMPLATES[filename],
            content,
            count=1,  # Only replace first occurrence
            flags=re.DOTALL
        )
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Updated navigation in {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def main():
    """Main execution function"""
    print("🚀 Starting Navigation Update Script")
    print("=" * 60)
    
    updated_count = 0
    failed_count = 0
    
    for filename in FILES_TO_UPDATE:
        print(f"\n📄 Processing {filename}...")
        if update_navigation(filename):
            updated_count += 1
        else:
            failed_count += 1
    
    print("\n" + "=" * 60)
    print(f"✨ Navigation Update Complete!")
    print(f"   ✅ Successfully updated: {updated_count} files")
    print(f"   ❌ Failed: {failed_count} files")
    print("=" * 60)
    
    if updated_count > 0:
        print("\n📝 Next steps:")
        print("   1. Review the changes in each file")
        print("   2. Test the navigation on all pages")
        print("   3. Commit and push the changes to GitHub")
        print("   4. Verify on live site")

if __name__ == "__main__":
    main()
