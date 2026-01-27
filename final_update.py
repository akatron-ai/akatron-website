#!/usr/bin/env python3
"""Final navigation update script - uses direct file manipulation"""

import re

# Files to update
files = [
    'index.html',
    'osint.html', 
    'threat-intelligence.html',
    'email-risk.html',
    'blog.html'
]

# Navigation patterns for each file
nav_replacements = {
    'index.html': {
        'old': '''        <nav>
            <a href="index.html" class="active">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="blog.html">Blog</a>
            <a href="#contact">Contact</a>
        </nav>''',
        'new': '''        <nav>
            <a href="index.html" class="active">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>'''
    },
    'osint.html': {
        'old': '''        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html" class="active">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="blog.html">Blog</a>
            <a href="#contact">Contact</a>
        </nav>''',
        'new': '''        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html" class="active">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>'''
    },
    'threat-intelligence.html': {
        'old': '''        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html" class="active">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="blog.html">Blog</a>
            <a href="#contact">Contact</a>
        </nav>''',
        'new': '''        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html" class="active">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>'''
    },
    'email-risk.html': {
        'old': '''        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html" class="active">Email Risk</a>
            <a href="blog.html">Blog</a>
            <a href="#contact">Contact</a>
        </nav>''',
        'new': '''        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html" class="active">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>'''
    },
    'blog.html': {
        'old': '''        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="blog.html" class="active">Blog</a>
            <a href="#contact">Contact</a>
        </nav>''',
        'new': '''        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html" class="active">Blog</a>
            <a href="about.html">About</a>
        </nav>'''
    }
}

def update_file(filename):
    """Update navigation in a file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if filename in nav_replacements:
            old_nav = nav_replacements[filename]['old']
            new_nav = nav_replacements[filename]['new']
            
            if old_nav in content:
                content = content.replace(old_nav, new_nav)
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✅ Updated {filename}")
                return True
            else:
                print(f"⚠️  Navigation pattern not found in {filename}")
                return False
        else:
            print(f"❌ No replacement pattern for {filename}")
            return False
            
    except Exception as e:
        print(f"❌ Error updating {filename}: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Starting navigation update...\n")
    
    updated = 0
    for filename in files:
        if update_file(filename):
            updated += 1
    
    print(f"\n✨ Complete! Updated {updated}/{len(files)} files")
