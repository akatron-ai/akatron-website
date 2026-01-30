#!/usr/bin/env python3
"""
Automatic Page Fixer - Updates all pricing buttons via GitHub API
Run this script to fix all pages at once
"""

import requests
import base64
import json
from typing import List, Dict

# GitHub Configuration
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN_HERE"  # Replace with your token
REPO_OWNER = "akatron-ai"
REPO_NAME = "akatron-website"
BRANCH = "main"

# Files to update
FILES_TO_UPDATE = [
    "osint.html",
    "threat-intelligence.html",
    "email-risk.html",
    "pricing.html",
    "about.html"
]

def get_file_content(filename: str) -> Dict:
    """Get file content from GitHub"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{filename}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        content = base64.b64decode(data['content']).decode('utf-8')
        return {
            'content': content,
            'sha': data['sha'],
            'filename': filename
        }
    else:
        print(f"❌ Error fetching {filename}: {response.status_code}")
        return None

def fix_content(content: str) -> str:
    """Fix all pricing button links"""
    # Replace all #contact links with payment.html
    content = content.replace('href="#contact"', 'href="payment.html"')
    content = content.replace("href='#contact'", "href='payment.html'")
    
    # Add Request Demo to navigation if missing
    if 'request-demo.html' not in content:
        content = content.replace(
            '<a href="pricing.html">Pricing</a>',
            '<a href="pricing.html">Pricing</a>\n            <a href="request-demo.html">Request Demo</a>'
        )
    
    # Add Payment to navigation if missing
    if 'href="payment.html">Payment</a>' not in content:
        if 'request-demo.html' in content:
            content = content.replace(
                '<a href="request-demo.html">Request Demo</a>',
                '<a href="request-demo.html">Request Demo</a>\n            <a href="payment.html">Payment</a>'
            )
    
    return content

def update_file(filename: str, content: str, sha: str) -> bool:
    """Update file on GitHub"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{filename}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    
    data = {
        "message": f"🔗 Fix pricing buttons in {filename} - Redirect to payment.html",
        "content": encoded_content,
        "sha": sha,
        "branch": BRANCH
    }
    
    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"   ✅ Updated {filename}")
        return True
    else:
        print(f"   ❌ Error updating {filename}: {response.status_code}")
        print(f"   Response: {response.text}")
        return False

def main():
    print("🤖 Automatic Page Fixer")
    print("=" * 60)
    print(f"Repository: {REPO_OWNER}/{REPO_NAME}")
    print(f"Branch: {BRANCH}")
    print("=" * 60)
    print()
    
    if GITHUB_TOKEN == "YOUR_GITHUB_TOKEN_HERE":
        print("❌ ERROR: Please set your GitHub token in the script")
        print("   Get your token from: https://github.com/settings/tokens")
        return
    
    success_count = 0
    fail_count = 0
    
    for filename in FILES_TO_UPDATE:
        print(f"📄 Processing {filename}...")
        
        # Get current file
        file_data = get_file_content(filename)
        if not file_data:
            fail_count += 1
            continue
        
        # Fix content
        original_content = file_data['content']
        fixed_content = fix_content(original_content)
        
        # Check if changes were made
        if original_content == fixed_content:
            print(f"   ℹ️  No changes needed for {filename}")
            continue
        
        # Update file
        if update_file(filename, fixed_content, file_data['sha']):
            success_count += 1
        else:
            fail_count += 1
        
        print()
    
    print("=" * 60)
    print(f"✅ Successfully updated: {success_count} files")
    print(f"❌ Failed: {fail_count} files")
    print("=" * 60)
    print()
    print("Changes made:")
    print("  • All pricing buttons now redirect to payment.html")
    print("  • Request Demo added to navigation")
    print("  • Payment added to navigation")
    print()
    print("Test your website:")
    print("  https://akatron-ai.github.io/akatron-website/")

if __name__ == "__main__":
    main()
