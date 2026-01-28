#!/bin/bash
# Script to apply demo button patches to index.html
# This script downloads index.html, applies the patches, and shows the result

echo "AKATRON Demo Button Patch Script"
echo "================================="
echo ""

# Check if we're in the right directory
if [ ! -f "index.html" ]; then
    echo "❌ Error: index.html not found in current directory"
    echo "Please run this script from the repository root"
    exit 1
fi

# Create backup
echo "📦 Creating backup..."
cp index.html index.html.backup
echo "✅ Backup created: index.html.backup"
echo ""

# Apply CSS patch (after line 219)
echo "🎨 Applying button group CSS..."
CSS_MARKER=".hero .btn span {"
CSS_INSERT_AFTER="        }"

# Read the button group CSS from patch file
if [ -f "patches/button-group-styles.css" ]; then
    # Insert CSS after line 219
    sed -i.tmp '/\.hero \.btn span {/,/^        }$/ {
        /^        }$/ r patches/button-group-styles.css
    }' index.html
    rm index.html.tmp 2>/dev/null
    echo "✅ CSS patch applied"
else
    echo "⚠️  Warning: patches/button-group-styles.css not found"
fi

echo ""

# Apply HTML patch (replace button on line 454)
echo "🔘 Applying hero button update..."
OLD_BUTTON='<a href="#services" class="btn"><span>Explore Services</span></a>'
NEW_BUTTON='<div class="btn-group">
            <a href="#services" class="btn btn-primary"><span>Explore Services</span></a>
            <a href="request-demo.html" class="btn btn-secondary"><span>Request Demo</span></a>
        </div>'

# Replace the button
sed -i.tmp "s|${OLD_BUTTON}|${NEW_BUTTON}|g" index.html
rm index.html.tmp 2>/dev/null
echo "✅ Hero button updated"
echo ""

echo "✅ All patches applied successfully!"
echo ""
echo "📋 Next steps:"
echo "1. Review the changes: git diff index.html"
echo "2. Test locally by opening index.html in a browser"
echo "3. Commit changes: git add index.html && git commit -m '🎨 Add demo button to homepage'"
echo "4. Push to GitHub: git push"
echo ""
echo "💡 To restore backup: mv index.html.backup index.html"
