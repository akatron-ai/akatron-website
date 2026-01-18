#!/bin/bash

# Automated SEO Tags Insertion Script for AKATRON Website
# This script adds enhanced SEO meta tags to all HTML pages

echo "🚀 Starting SEO Enhancement..."

# Function to add SEO tags after meta description
add_seo_tags() {
    local file=$1
    local url=$2
    local title=$3
    local description=$4
    local keywords=$5
    
    # Create temporary file with SEO tags
    cat > /tmp/seo_tags.txt << EOF
    
    <!-- Enhanced SEO Meta Tags -->
    <meta name="keywords" content="$keywords">
    <meta name="author" content="AKATRON">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="$url">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="$url">
    <meta property="og:title" content="$title">
    <meta property="og:description" content="$description">
    <meta property="og:image" content="https://akatron-ai.github.io/akatron-website/akatron-logo.png">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="$url">
    <meta property="twitter:title" content="$title">
    <meta property="twitter:description" content="$description">
    <meta property="twitter:image" content="https://akatron-ai.github.io/akatron-website/akatron-logo.png">
EOF
    
    # Insert after the meta description line
    sed -i '/meta name="description"/r /tmp/seo_tags.txt' "$file"
    
    echo "✅ Updated $file"
}

# Update index.html
add_seo_tags "index.html" \
    "https://akatron-ai.github.io/akatron-website/" \
    "AKATRON - Elite Cybersecurity & OSINT Intelligence Services" \
    "Professional cybersecurity services starting at ₹999. Email risk analysis, OSINT investigations, and threat intelligence for individuals and businesses in India." \
    "cybersecurity services India, OSINT investigation, email security check, threat intelligence, data breach check, digital footprint analysis, cyber security audit"

# Update osint.html
add_seo_tags "osint.html" \
    "https://akatron-ai.github.io/akatron-website/osint.html" \
    "OSINT Investigations - Professional Background Checks | AKATRON" \
    "Professional OSINT investigations starting at ₹3,999. Digital footprint analysis, background verification, and threat actor research." \
    "OSINT services India, open source intelligence, background check, digital footprint analysis, online investigation, OSINT India"

# Update email-risk.html
add_seo_tags "email-risk.html" \
    "https://akatron-ai.github.io/akatron-website/email-risk.html" \
    "Email Risk Analysis - Check If Your Email Was Hacked | AKATRON" \
    "₹999 comprehensive email security check. Scan 500+ breach databases to detect if your email was compromised. Get results in 24 hours." \
    "email security check, data breach check, email hack check, credential leak, email risk analysis India, check if email hacked"

# Update threat-intelligence.html
add_seo_tags "threat-intelligence.html" \
    "https://akatron-ai.github.io/akatron-website/threat-intelligence.html" \
    "Threat Intelligence Services - Proactive Cyber Defense | AKATRON" \
    "Strategic cyber threat intelligence for organizations. Adversary tracking, dark web monitoring, and real-time threat alerts." \
    "threat intelligence India, cyber threat monitoring, dark web monitoring, vulnerability intelligence, IOC feeds, threat analysis"

# Add Schema.org markup to index.html
cat >> index.html << 'EOF'

    <!-- Schema.org Markup for Google -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "ProfessionalService",
      "name": "AKATRON",
      "description": "Elite Cybersecurity & OSINT Intelligence Services",
      "url": "https://akatron-ai.github.io/akatron-website/",
      "logo": "https://akatron-ai.github.io/akatron-website/akatron-logo.png",
      "priceRange": "₹999 - ₹5,999",
      "areaServed": "IN",
      "serviceType": ["Cybersecurity", "OSINT Investigation", "Threat Intelligence", "Email Security"],
      "offers": [
        {
          "@type": "Offer",
          "name": "Email Risk Analysis",
          "price": "999",
          "priceCurrency": "INR"
        },
        {
          "@type": "Offer",
          "name": "OSINT Background Check",
          "price": "3999",
          "priceCurrency": "INR"
        },
        {
          "@type": "Offer",
          "name": "Cybersecurity Audit",
          "price": "5999",
          "priceCurrency": "INR"
        }
      ]
    }
    </script>
EOF

echo ""
echo "✅ SEO Enhancement Complete!"
echo ""
echo "📋 Next Steps:"
echo "1. Review the changes in each HTML file"
echo "2. Commit and push to GitHub"
echo "3. Verify at: https://www.opengraph.xyz/"
echo "4. Submit sitemap to Google Search Console"
echo ""
