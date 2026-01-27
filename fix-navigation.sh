#!/bin/bash

# Navigation Fix Script for AKATRON Website
# This script updates navigation menus on all HTML pages

echo "🚀 Starting Navigation Update..."
echo "================================"

# Define the old and new navigation patterns
OLD_NAV='<a href="blog.html">Blog</a>
            <a href="#contact">Contact</a>'

NEW_NAV='<a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>'

# Files to update
FILES=("index.html" "osint.html" "threat-intelligence.html" "email-risk.html" "blog.html")

# Update each file
for file in "${FILES[@]}"; do
    echo "📝 Updating $file..."
    
    # Use sed to replace the navigation
    sed -i.bak 's|<a href="blog.html">Blog</a>[[:space:]]*<a href="#contact">Contact</a>|<a href="pricing.html">Pricing</a>\n            <a href="blog.html">Blog</a>\n            <a href="about.html">About</a>|g' "$file"
    
    # Remove backup file
    rm "${file}.bak"
    
    echo "✅ $file updated"
done

echo "================================"
echo "✨ Navigation update complete!"
echo ""
echo "Next steps:"
echo "1. Review changes: git diff"
echo "2. Commit: git add *.html && git commit -m '✨ Update navigation menus'"
echo "3. Push: git push origin main"
