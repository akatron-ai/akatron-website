#!/bin/bash

# Add JSON-LD structured data to index.html (Organization + LocalBusiness schema)
sed -i '/<\/head>/i\    \n    <!-- JSON-LD Structured Data for SEO -->\n    <script type="application/ld+json">\n    {\n      "@context": "https://schema.org",\n      "@type": "Organization",\n      "name": "AKATRON",\n      "url": "https://akatron-ai.github.io/akatron-website/",\n      "logo": "https://akatron-ai.github.io/akatron-website/akatron-logo.png",\n      "description": "Professional cybersecurity services, OSINT investigations, threat intelligence, and email risk analysis",\n      "address": {\n        "@type": "PostalAddress",\n        "addressCountry": "IN"\n      },\n      "sameAs": [],\n      "contactPoint": {\n        "@type": "ContactPoint",\n        "contactType": "Customer Service",\n        "availableLanguage": ["English", "Hindi"]\n      },\n      "offers": [\n        {\n          "@type": "Offer",\n          "name": "Email Risk Analysis",\n          "price": "999",\n          "priceCurrency": "INR",\n          "url": "https://akatron-ai.github.io/akatron-website/email-risk.html"\n        },\n        {\n          "@type": "Offer",\n          "name": "OSINT Investigation",\n          "price": "3999",\n          "priceCurrency": "INR",\n          "url": "https://akatron-ai.github.io/akatron-website/osint.html"\n        },\n        {\n          "@type": "Offer",\n          "name": "Threat Intelligence",\n          "price": "5999",\n          "priceCurrency": "INR",\n          "url": "https://akatron-ai.github.io/akatron-website/threat-intelligence.html"\n        }\n      ]\n    }\n    </script>' index.html

echo "✅ Added structured data to index.html"

# Add Service schema to osint.html
sed -i '/<\/head>/i\    \n    <!-- JSON-LD Structured Data -->\n    <script type="application/ld+json">\n    {\n      "@context": "https://schema.org",\n      "@type": "Service",\n      "serviceType": "OSINT Investigation Services",\n      "provider": {\n        "@type": "Organization",\n        "name": "AKATRON",\n        "url": "https://akatron-ai.github.io/akatron-website/"\n      },\n      "areaServed": "IN",\n      "description": "Professional OSINT investigations starting at ₹3,999. Digital footprint analysis, background verification, and threat actor research.",\n      "offers": {\n        "@type": "Offer",\n        "price": "3999",\n        "priceCurrency": "INR"\n      }\n    }\n    </script>' osint.html

echo "✅ Added structured data to osint.html"

# Add Service schema to email-risk.html
sed -i '/<\/head>/i\    \n    <!-- JSON-LD Structured Data -->\n    <script type="application/ld+json">\n    {\n      "@context": "https://schema.org",\n      "@type": "Service",\n      "serviceType": "Email Security Analysis",\n      "provider": {\n        "@type": "Organization",\n        "name": "AKATRON",\n        "url": "https://akatron-ai.github.io/akatron-website/"\n      },\n      "areaServed": "IN",\n      "description": "₹999 comprehensive email security check. Scan 500+ breach databases to detect if your email was compromised.",\n      "offers": {\n        "@type": "Offer",\n        "price": "999",\n        "priceCurrency": "INR"\n      }\n    }\n    </script>' email-risk.html

echo "✅ Added structured data to email-risk.html"

# Add Service schema to threat-intelligence.html
sed -i '/<\/head>/i\    \n    <!-- JSON-LD Structured Data -->\n    <script type="application/ld+json">\n    {\n      "@context": "https://schema.org",\n      "@type": "Service",\n      "serviceType": "Threat Intelligence Services",\n      "provider": {\n        "@type": "Organization",\n        "name": "AKATRON",\n        "url": "https://akatron-ai.github.io/akatron-website/"\n      },\n      "areaServed": "IN",\n      "description": "Strategic cyber threat intelligence for organizations. Adversary tracking, dark web monitoring, and real-time threat alerts.",\n      "offers": {\n        "@type": "Offer",\n        "price": "5999",\n        "priceCurrency": "INR"\n      }\n    }\n    </script>' threat-intelligence.html

echo "✅ Added structured data to threat-intelligence.html"

echo ""
echo "🎉 JSON-LD structured data added to all pages!"
echo "📊 This will help search engines understand your business better"
