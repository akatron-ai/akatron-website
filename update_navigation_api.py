#!/usr/bin/env python3
"""
Navigation Update Script using GitHub API
Updates navigation menus across all HTML pages
"""

import requests
import base64
import os
import re

# GitHub configuration
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')  # Set this as environment variable
REPO_OWNER = 'akatron-ai'
REPO_NAME = 'akatron-website'
BRANCH = 'main'

# Files to update
FILES = [
    'index.html',
    'osint.html',
    'threat-intelligence.html',
    'email-risk.html',
    'blog.html'
]

# Navigation templates for each page
NAV_TEMPLATES = {
    'index.html': '''        <nav>
            <a href="index.html" class="active">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>''',
    
    'osint.html': '''        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html" class="active">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>''',
    
    'threat-intelligence.html': '''        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html" class="active">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>''',
    
    'email-risk.html': '''        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html" class="active">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>''',
    
    'blog.html': '''        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html" class="active">Blog</a>
            <a href="about.html">About</a>
        </nav>'''
}

def get_file_content(filename):
    """Get file content and SHA from GitHub"""
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{filename}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        content = base64.b64decode(data['content']).decode('utf-8')
        return content, data['sha']
    else:
        print(f"❌ Error fetching {filename}: {response.status_code}")
        return None, None

def update_file_content(filename, content, sha):
    """Update file content on GitHub"""
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{filename}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    
    data = {
        'message': f'✨ Update navigation in {filename}',
        'content': encoded_content,
        'sha': sha,
        'branch': BRANCH
    }
    
    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 200:
        return True
    else:
        print(f"❌ Error updating {filename}: {response.status_code} - {response.text}")
        return False

def update_navigation(filename):
    """Update navigation in a single file"""
    print(f"📝 Processing {filename}...")
    
    # Get current content
    content, sha = get_file_content(filename)
    if not content:
        return False
    
    # Replace navigation
    nav_pattern = r'<nav>[\s\S]*?</nav>'
    new_content = re.sub(nav_pattern, NAV_TEMPLATES[filename], content, count=1)
    
    # Update file
    if update_file_content(filename, new_content, sha):
        print(f"✅ {filename} updated successfully\n")
        return True
    else:
        return False

def main():
    """Main execution"""
    if not GITHUB_TOKEN:
        print("❌ ERROR: GITHUB_TOKEN environment variable not set!")
        print("Set it with: export GITHUB_TOKEN='your_token_here'")
        return
    
    print("🚀 Starting Navigation Update via GitHub API...\n")
    print("=" * 60)
    
    updated = 0
    failed = 0
    
    for filename in FILES:
        if update_navigation(filename):
            updated += 1
        else:
            failed += 1
    
    print("=" * 60)
    print(f"✨ Update Complete!")
    print(f"   ✅ Successfully updated: {updated} files")
    print(f"   ❌ Failed: {failed} files")
    print("=" * 60)
    
    if updated > 0:
        print("\n🌐 Your website will be updated in 2-3 minutes!")
        print("Visit: https://akatron-ai.github.io/akatron-website/")

if __name__ == "__main__":
    main()
