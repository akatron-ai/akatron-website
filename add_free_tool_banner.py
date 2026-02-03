#!/usr/bin/env python3
"""
Add Free Email Checker Banner to Homepage
Inserts prominent free tool banner after hero section
"""

import os

# HTML for the free tool banner
FREE_TOOL_BANNER = '''
    <!-- FREE TOOL BANNER -->
    <section class="section" style="background: linear-gradient(135deg, rgba(218,165,32,0.15) 0%, rgba(218,165,32,0.05) 100%); padding: 60px 20px;">
        <div class="container" style="max-width: 1000px; text-align: center;">
            <div style="display: inline-block; background: #DAA520; color: #0a0b0f; padding: 8px 20px; border-radius: 20px; font-weight: 700; font-size: 14px; margin-bottom: 20px;">
                🎁 FREE TOOL
            </div>
            <h2 style="color: #DAA520; font-size: 42px; margin-bottom: 20px;">Check If Your Email Has Been Hacked</h2>
            <p style="color: #b8bcc8; font-size: 18px; max-width: 700px; margin: 0 auto 30px;">
                Instantly scan your email against millions of data breaches. Get a free security report in seconds.
            </p>
            <a href="email-checker.html" style="display: inline-block; padding: 18px 50px; background: #DAA520; color: #0a0b0f; text-decoration: none; border-radius: 50px; font-weight: 700; font-size: 18px; transition: all 0.3s ease; box-shadow: 0 10px 40px rgba(218,165,32,0.3);">
                Check Your Email Now - FREE →
            </a>
            <p style="color: #8a8f98; font-size: 14px; margin-top: 20px;">
                ✓ Instant results  ✓ No signup required  ✓ 100% confidential
            </p>
        </div>
    </section>
'''

def add_banner():
    """Add free tool banner to index.html"""
    filename = 'index.html'
    
    if not os.path.exists(filename):
        print(f"❌ {filename} not found")
        return False
    
    # Read file
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if banner already exists
    if 'FREE TOOL BANNER' in content or 'email-checker.html' in content:
        print(f"⏭️  Banner already exists in {filename}")
        return False
    
    # Find the position to insert (after hero section, before services)
    insert_marker = '    <!-- SERVICES SECTION -->'
    
    if insert_marker in content:
        content = content.replace(insert_marker, FREE_TOOL_BANNER + '\n' + insert_marker)
        
        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {filename}: Added free email checker banner")
        return True
    else:
        print(f"❌ {filename}: Could not find insertion point")
        return False

def main():
    """Main execution"""
    print("🎁 Adding Free Email Checker Banner...")
    print()
    
    if add_banner():
        print()
        print("━" * 50)
        print("✨ COMPLETE! Free tool banner added to homepage")
        print()
        print("The banner appears right after the hero section")
        print("and directs users to email-checker.html")
        print()
        print("Next: Commit and push changes")
    else:
        print()
        print("No changes made")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
