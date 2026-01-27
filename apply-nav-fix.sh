#!/bin/bash
# Navigation update script using sed

echo "🚀 Updating navigation on all HTML files..."

# Update index.html
sed -i 's|<a href="blog.html">Blog</a>|<a href="pricing.html">Pricing</a>\n            <a href="blog.html">Blog</a>|g' index.html
sed -i 's|<a href="#contact">Contact</a>|<a href="about.html">About</a>|g' index.html

# Update osint.html
sed -i 's|<a href="blog.html">Blog</a>|<a href="pricing.html">Pricing</a>\n            <a href="blog.html">Blog</a>|g' osint.html
sed -i 's|<a href="#contact">Contact</a>|<a href="about.html">About</a>|g' osint.html

# Update threat-intelligence.html
sed -i 's|<a href="blog.html">Blog</a>|<a href="pricing.html">Pricing</a>\n            <a href="blog.html">Blog</a>|g' threat-intelligence.html
sed -i 's|<a href="#contact">Contact</a>|<a href="about.html">About</a>|g' threat-intelligence.html

# Update email-risk.html
sed -i 's|<a href="blog.html">Blog</a>|<a href="pricing.html">Pricing</a>\n            <a href="blog.html">Blog</a>|g' email-risk.html
sed -i 's|<a href="#contact">Contact</a>|<a href="about.html">About</a>|g' email-risk.html

# Update blog.html
sed -i 's|<a href="blog.html" class="active">Blog</a>|<a href="pricing.html">Pricing</a>\n            <a href="blog.html" class="active">Blog</a>|g' blog.html
sed -i 's|<a href="#contact">Contact</a>|<a href="about.html">About</a>|g' blog.html

echo "✅ Navigation updated on all files!"
