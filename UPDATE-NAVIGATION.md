# Navigation Update Required

## Files to Update (5 total):
1. `index.html` - Line ~430
2. `osint.html` - Line ~67
3. `threat-intelligence.html` - Line ~67
4. `email-risk.html` - Line ~67
5. `blog.html` - Line ~30

## Current Navigation:
```html
<nav>
    <a href="index.html">Home</a>
    <a href="osint.html">OSINT</a>
    <a href="threat-intelligence.html">Threat Intel</a>
    <a href="email-risk.html">Email Risk</a>
    <a href="blog.html">Blog</a>
    <a href="#contact">Contact</a>
</nav>
```

## New Navigation (with Pricing + About):
```html
<nav>
    <a href="index.html">Home</a>
    <a href="osint.html">OSINT</a>
    <a href="threat-intelligence.html">Threat Intel</a>
    <a href="email-risk.html">Email Risk</a>
    <a href="pricing.html">Pricing</a>
    <a href="blog.html">Blog</a>
    <a href="about.html">About</a>
</nav>
```

## Manual Update Steps:
1. Open each file in GitHub web editor
2. Find the `<nav>` section
3. Replace the navigation links
4. Add appropriate `class="active"` to current page
5. Commit changes

## Active States Per Page:
- **index.html**: `<a href="index.html" class="active">Home</a>`
- **osint.html**: `<a href="osint.html" class="active">OSINT</a>`
- **threat-intelligence.html**: `<a href="threat-intelligence.html" class="active">Threat Intel</a>`
- **email-risk.html**: `<a href="email-risk.html" class="active">Email Risk</a>`
- **pricing.html**: `<a href="pricing.html" class="active">Pricing</a>` (already done)
- **blog.html**: `<a href="blog.html" class="active">Blog</a>`
- **about.html**: `<a href="about.html" class="active">About</a>` (already done)

## Status:
- ✅ pricing.html - Navigation complete
- ✅ about.html - Navigation complete
- ✅ Blog posts (3) - Navigation complete
- ⏳ index.html - Needs update
- ⏳ osint.html - Needs update
- ⏳ threat-intelligence.html - Needs update
- ⏳ email-risk.html - Needs update
- ⏳ blog.html - Needs update
