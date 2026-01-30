#!/bin/bash

# Fix All Pricing Buttons - Automated Script
# This script replaces all #contact links with payment.html links

echo "🔧 Fixing all pricing buttons across all pages..."
echo "=================================================="

# Array of files to update
files=(
    "osint.html"
    "threat-intelligence.html"
    "email-risk.html"
    "pricing.html"
    "about.html"
)

# Backup directory
mkdir -p backups

# Process each file
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo ""
        echo "📄 Processing $file..."
        
        # Create backup
        cp "$file" "backups/${file}.backup"
        
        # Replace href="#contact" with href="payment.html"
        sed -i 's/href="#contact"/href="payment.html"/g' "$file"
        
        # Replace href='#contact' with href='payment.html'
        sed -i "s/href='#contact'/href='payment.html'/g" "$file"
        
        # Add Request Demo to navigation if missing
        if ! grep -q 'request-demo.html' "$file"; then
            echo "   Adding Request Demo to navigation..."
            sed -i 's|<a href="pricing.html">Pricing</a>|<a href="pricing.html">Pricing</a>\n            <a href="request-demo.html">Request Demo</a>|' "$file"
        fi
        
        # Add Payment to navigation if missing
        if ! grep -q 'href="payment.html">Payment</a>' "$file"; then
            echo "   Adding Payment to navigation..."
            sed -i 's|<a href="request-demo.html">Request Demo</a>|<a href="request-demo.html">Request Demo</a>\n            <a href="payment.html">Payment</a>|' "$file"
        fi
        
        echo "   ✅ Updated $file"
    else
        echo "   ⚠️  $file not found"
    fi
done

echo ""
echo "=================================================="
echo "✅ All files updated successfully!"
echo ""
echo "Changes made:"
echo "  • All #contact links → payment.html"
echo "  • Request Demo added to navigation"
echo "  • Payment added to navigation"
echo ""
echo "Backups saved in: backups/"
echo ""
echo "To test: Open each HTML file and click pricing buttons"
