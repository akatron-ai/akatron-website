#!/usr/bin/env python3
"""
Automated SEO Tags Updater for AKATRON Website
This script adds enhanced SEO meta tags to all HTML pages
"""

import re

def add_seo_tags_to_file(filename, seo_tags):
    """Add SEO tags after the meta description line"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the meta description line and add SEO tags after it
        pattern = r'(<meta name="description"[^>]*>)'
        replacement = r'\1\n' + seo_tags
        
        updated_content = re.sub(pattern, replacement, content, count=1)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✅ Updated {filename}")
        return True
    except Exception as e:
        print(f"❌ Error updating {filename}: {e}")
        return False

# SEO tags for index.html
index_seo = """    
    <!-- Enhanced SEO Meta Tags -->
    <meta name="keywords" content="cybersecurity services India, OSINT investigation, email security check, threat intelligence, data breach check, digital footprint analysis, cyber security audit">
    <meta name="author" content="AKATRON">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://akatron-ai.github.io/akatron-website/">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://akatron-ai.github.io/akatron-website/">
    <meta property="og:title" content="AKATRON - Elite Cybersecurity & OSINT Intelligence Services">
    <meta property="og:description" content="Professional cybersecurity services starting at ₹999. Email risk analysis, OSINT investigations, and threat intelligence for individuals and businesses in India.">
    <meta property="og:image" content="https://akatron-ai.github.io/akatron-website/akatron-logo.png">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://akatron-ai.github.io/akatron-website/">
    <meta property="twitter:title" content="AKATRON - Elite Cybersecurity & OSINT Intelligence">
    <meta property="twitter:description" content="Professional cybersecurity services starting at ₹999. Email risk analysis, OSINT investigations, and threat intelligence.">
    <meta property="twitter:image" content="https://akatron-ai.github.io/akatron-website/akatron-logo.png">"""

# SEO tags for osint.html
osint_seo = """    
    <!-- Enhanced SEO Meta Tags -->
    <meta name="keywords" content="OSINT services India, open source intelligence, background check, digital footprint analysis, online investigation, OSINT India">
    <meta name="author" content="AKATRON">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://akatron-ai.github.io/akatron-website/osint.html">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://akatron-ai.github.io/akatron-website/osint.html">
    <meta property="og:title" content="OSINT Investigations - Professional Background Checks | AKATRON">
    <meta property="og:description" content="Professional OSINT investigations starting at ₹3,999. Digital footprint analysis, background verification, and threat actor research.">
    <meta property="og:image" content="https://akatron-ai.github.io/akatron-website/akatron-logo.png">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://akatron-ai.github.io/akatron-website/osint.html">
    <meta property="twitter:title" content="OSINT Investigations - Professional Background Checks | AKATRON">
    <meta property="twitter:description" content="Professional OSINT investigations starting at ₹3,999. Digital footprint analysis, background verification, and threat actor research.">
    <meta property="twitter:image" content="https://akatron-ai.github.io/akatron-website/akatron-logo.png">"""

# SEO tags for email-risk.html
email_seo = """    
    <!-- Enhanced SEO Meta Tags -->
    <meta name="keywords" content="email security check, data breach check, email hack check, credential leak, email risk analysis India, check if email hacked">
    <meta name="author" content="AKATRON">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://akatron-ai.github.io/akatron-website/email-risk.html">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://akatron-ai.github.io/akatron-website/email-risk.html">
    <meta property="og:title" content="Email Risk Analysis - Check If Your Email Was Hacked | AKATRON">
    <meta property="og:description" content="₹999 comprehensive email security check. Scan 500+ breach databases to detect if your email was compromised. Get results in 24 hours.">
    <meta property="og:image" content="https://akatron-ai.github.io/akatron-website/akatron-logo.png">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://akatron-ai.github.io/akatron-website/email-risk.html">
    <meta property="twitter:title" content="Email Risk Analysis - Check If Your Email Was Hacked | AKATRON">
    <meta property="twitter:description" content="₹999 comprehensive email security check. Scan 500+ breach databases to detect if your email was compromised. Get results in 24 hours.">
    <meta property="twitter:image" content="https://akatron-ai.github.io/akatron-website/akatron-logo.png">"""

# SEO tags for threat-intelligence.html
threat_seo = """    
    <!-- Enhanced SEO Meta Tags -->
    <meta name="keywords" content="threat intelligence India, cyber threat monitoring, dark web monitoring, vulnerability intelligence, IOC feeds, threat analysis">
    <meta name="author" content="AKATRON">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://akatron-ai.github.io/akatron-website/threat-intelligence.html">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://akatron-ai.github.io/akatron-website/threat-intelligence.html">
    <meta property="og:title" content="Threat Intelligence Services - Proactive Cyber Defense | AKATRON">
    <meta property="og:description" content="Strategic cyber threat intelligence for organizations. Adversary tracking, dark web monitoring, and real-time threat alerts.">
    <meta property="og:image" content="https://akatron-ai.github.io/akatron-website/akatron-logo.png">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://akatron-ai.github.io/akatron-website/threat-intelligence.html">
    <meta property="twitter:title" content="Threat Intelligence Services - Proactive Cyber Defense | AKATRON">
    <meta property="twitter:description" content="Strategic cyber threat intelligence for organizations. Adversary tracking, dark web monitoring, and real-time threat alerts.">
    <meta property="twitter:image" content="https://akatron-ai.github.io/akatron-website/akatron-logo.png">"""

def main():
    print("🚀 Starting SEO Enhancement...\n")
    
    files_to_update = [
        ('index.html', index_seo),
        ('osint.html', osint_seo),
        ('email-risk.html', email_seo),
        ('threat-intelligence.html', threat_seo)
    ]
    
    success_count = 0
    for filename, seo_tags in files_to_update:
        if add_seo_tags_to_file(filename, seo_tags):
            success_count += 1
    
    print(f"\n✅ SEO Enhancement Complete!")
    print(f"📊 Updated {success_count}/{len(files_to_update)} files")
    print("\n📋 Next Steps:")
    print("1. Review the changes: git diff")
    print("2. Commit: git add . && git commit -m '✨ Add enhanced SEO meta tags'")
    print("3. Push: git push")
    print("4. Verify at: https://www.opengraph.xyz/")

if __name__ == "__main__":
    main()
