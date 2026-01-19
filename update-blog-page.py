#!/usr/bin/env python3
"""
Script to add the 2 new blog posts to blog.html
"""

import re

# New blog post cards to add at the top
NEW_BLOG_POSTS = '''                <!-- NEW ARTICLE 1 - Email Hacked -->
                <div class="blog-card" data-category="security" onclick="window.location.href='blog/top-5-signs-email-hacked-2026.html'">
                    <div class="blog-image">📧</div>
                    <div class="blog-content">
                        <div class="blog-meta">
                            <span class="blog-category">Security</span>
                            <span>•</span>
                            <span>12 min read</span>
                            <span>•</span>
                            <span>Jan 19, 2026</span>
                        </div>
                        <h3>Top 5 Signs Your Email Was Hacked in 2026</h3>
                        <p>Discover the critical warning signs that your email account has been compromised and learn immediate steps to secure your digital identity.</p>
                        <a href="blog/top-5-signs-email-hacked-2026.html" class="read-more">Read More →</a>
                    </div>
                </div>

                <!-- NEW ARTICLE 2 - OSINT Techniques -->
                <div class="blog-card" data-category="osint" onclick="window.location.href='blog/osint-techniques-personal-security.html'">
                    <div class="blog-image">🔍</div>
                    <div class="blog-content">
                        <div class="blog-meta">
                            <span class="blog-category">OSINT</span>
                            <span>•</span>
                            <span>15 min read</span>
                            <span>•</span>
                            <span>Jan 19, 2026</span>
                        </div>
                        <h3>OSINT Techniques for Personal Security in 2026</h3>
                        <p>Master open-source intelligence techniques to protect your digital footprint and enhance your personal security in the modern age.</p>
                        <a href="blog/osint-techniques-personal-security.html" class="read-more">Read More →</a>
                    </div>
                </div>

'''

def update_blog_html():
    """Update blog.html with new blog posts"""
    try:
        # Read the file
        with open('blog.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the blog-grid div and insert new posts after it
        pattern = r'(<div class="blog-grid">)\s*\n(\s*<!-- Article 1 -->)'
        replacement = r'\1\n' + NEW_BLOG_POSTS + r'\2'
        
        updated_content = re.sub(pattern, replacement, content)
        
        # Write back
        with open('blog.html', 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print("✅ Successfully updated blog.html!")
        print()
        print("Added 2 new blog posts:")
        print("  1. Top 5 Signs Your Email Was Hacked in 2026")
        print("  2. OSINT Techniques for Personal Security in 2026")
        print()
        print("Next steps:")
        print("  1. Commit and push the changes")
        print("  2. Verify the blog page looks good")
        print("  3. Test the links to the new blog posts")
        
        return True
        
    except FileNotFoundError:
        print("❌ Error: blog.html not found")
        print("Make sure you're running this script from the repository root directory")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Updating blog.html with new blog posts...")
    print("=" * 50)
    print()
    update_blog_html()
