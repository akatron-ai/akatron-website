#!/bin/bash

# AKATRON Website - Fix All Pricing Buttons
# This script replaces all href="#contact" with href="payment.html"

echo "🔧 AKATRON - Fixing all pricing button links..."
echo ""

# Array of files to fix
files=("osint.html" "threat-intelligence.html" "email-risk.html" "pricing.html" "about.html")

# Counter for changes
total_changes=0

# Process each file
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "📝 Processing: $file"
        
        # Count occurrences before replacement
        count=$(grep -o 'href="#contact"' "$file" | wc -l)
        
        if [ "$count" -gt 0 ]; then
            # Perform replacement (Mac compatible)
            if [[ "$OSTYPE" == "darwin"* ]]; then
                sed -i '' 's/href="#contact"/href="payment.html"/g' "$file"
            else
                sed -i 's/href="#contact"/href="payment.html"/g' "$file"
            fi
            
            echo "   ✅ Fixed $count button(s)"
            total_changes=$((total_changes + count))
        else
            echo "   ⏭️  No changes needed"
        fi
    else
        echo "   ❌ File not found: $file"
    fi
    echo ""
done

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ COMPLETE! Fixed $total_changes button(s) total"
echo ""
echo "Next steps:"
echo "1. Review changes: git diff"
echo "2. Commit: git add . && git commit -m '🔗 Fix all pricing buttons - Redirect to payment.html'"
echo "3. Push: git push"
echo ""
echo "🎉 Your website will be updated in 1-2 minutes!"
