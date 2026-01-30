#!/bin/bash

# AKATRON Website - Fix All Pricing Buttons
# This script fixes all #contact links to payment.html across all pages

echo "🚀 AKATRON Website - Pricing Button Fixer"
echo "=========================================="
echo ""

# Check if we're in the right directory
if [ ! -f "index.html" ]; then
    echo "❌ Error: Please run this script from the repository root"
    exit 1
fi

# Create backup directory
BACKUP_DIR="backups_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
echo "📦 Creating backups in: $BACKUP_DIR"

# Files to fix
FILES=(
    "osint.html"
    "threat-intelligence.html"
    "email-risk.html"
    "pricing.html"
    "about.html"
)

# Counter
FIXED=0
SKIPPED=0

echo ""
echo "🔧 Processing files..."
echo ""

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "📄 Processing: $file"
        
        # Create backup
        cp "$file" "$BACKUP_DIR/$file"
        
        # Count occurrences before
        BEFORE=$(grep -c 'href="#contact"' "$file" 2>/dev/null || echo "0")
        
        if [ "$BEFORE" -gt 0 ]; then
            # Fix the file
            sed -i.tmp 's/href="#contact"/href="payment.html"/g' "$file"
            rm -f "${file}.tmp"
            
            # Count occurrences after
            AFTER=$(grep -c 'href="#contact"' "$file" 2>/dev/null || echo "0")
            
            CHANGED=$((BEFORE - AFTER))
            echo "   ✅ Fixed $CHANGED button(s)"
            FIXED=$((FIXED + 1))
        else
            echo "   ℹ️  No changes needed"
            SKIPPED=$((SKIPPED + 1))
        fi
    else
        echo "   ⚠️  File not found: $file"
        SKIPPED=$((SKIPPED + 1))
    fi
    echo ""
done

echo "=========================================="
echo "✅ Complete!"
echo ""
echo "Summary:"
echo "  • Files fixed: $FIXED"
echo "  • Files skipped: $SKIPPED"
echo "  • Backups saved in: $BACKUP_DIR"
echo ""
echo "Next steps:"
echo "  1. Review changes: git diff"
echo "  2. Test locally: open index.html in browser"
echo "  3. Commit: git add . && git commit -m '🔗 Fix all pricing buttons'"
echo "  4. Push: git push"
echo ""
echo "🎉 All pricing buttons now redirect to payment.html!"
