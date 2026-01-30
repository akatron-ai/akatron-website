# Batch Fix All Pricing Buttons

## Problem
All service pages (osint.html, threat-intelligence.html, email-risk.html, pricing.html) have pricing buttons that link to `#contact` instead of `payment.html`.

## Solution
Replace ALL instances of `href="#contact"` with `href="payment.html"` in the following files:

### Files to Update:
1. ✅ index.html (ALREADY FIXED)
2. ⏳ osint.html
3. ⏳ threat-intelligence.html
4. ⏳ email-risk.html
5. ⏳ pricing.html
6. ⏳ about.html

### Search & Replace Pattern:
```
FIND:    href="#contact"
REPLACE: href="payment.html"
```

### Additional Navigation Fix:
Add "Request Demo" and "Payment" links to navigation menu if missing:

```html
<a href="pricing.html">Pricing</a>
<a href="request-demo.html">Request Demo</a>
<a href="payment.html">Payment</a>
<a href="blog.html">Blog</a>
```

## Expected Result:
- All "Start Analysis" buttons → payment.html
- All "Get Started" buttons → payment.html  
- All "Request Background Check" buttons → payment.html
- All "Start Audit" buttons → payment.html
- Hero CTA buttons → payment.html

## Testing:
After update, verify each page:
1. Click pricing card buttons → Should go to payment.html
2. Click hero CTA → Should go to payment.html
3. Navigation menu → Should have Request Demo & Payment links
