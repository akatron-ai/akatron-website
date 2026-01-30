# Manual Fix Guide - Update All Pricing Buttons

## Quick Fix Instructions

### Method 1: GitHub Web Interface (Easiest)

For each file below, follow these steps:

1. Go to: https://github.com/akatron-ai/akatron-website
2. Click on the file name
3. Click the pencil icon (Edit this file)
4. Press `Ctrl+H` (Windows) or `Cmd+F` (Mac) to open Find & Replace
5. Find: `href="#contact"`
6. Replace with: `href="payment.html"`
7. Click "Replace All"
8. Scroll to bottom and click "Commit changes"

### Files to Update:

#### 1. osint.html
- **Location**: Root directory
- **Find**: `href="#contact"`
- **Replace**: `href="payment.html"`
- **Expected changes**: 4 buttons (Hero + 3 pricing cards)

#### 2. threat-intelligence.html
- **Location**: Root directory
- **Find**: `href="#contact"`
- **Replace**: `href="payment.html"`
- **Expected changes**: 4 buttons

#### 3. email-risk.html
- **Location**: Root directory
- **Find**: `href="#contact"`
- **Replace**: `href="payment.html"`
- **Expected changes**: 4 buttons

#### 4. pricing.html
- **Location**: Root directory
- **Find**: `href="#contact"`
- **Replace**: `href="payment.html"`
- **Expected changes**: 3-4 buttons

#### 5. about.html
- **Location**: Root directory
- **Find**: `href="#contact"`
- **Replace**: `href="payment.html"`
- **Expected changes**: 1-2 buttons

---

### Method 2: VS Code (If you have the repo cloned)

1. Open the repository in VS Code
2. Press `Ctrl+Shift+H` to open "Search and Replace in Files"
3. In "Search" box: `href="#contact"`
4. In "Replace" box: `href="payment.html"`
5. Click "Replace All"
6. Save all files
7. Commit and push:
   ```bash
   git add .
   git commit -m "🔗 Fix all pricing buttons - Redirect to payment.html"
   git push
   ```

---

### Method 3: Command Line (Advanced)

```bash
# Clone the repository
git clone https://github.com/akatron-ai/akatron-website.git
cd akatron-website

# Run the fix script
chmod +x fix-buttons.sh
./fix-buttons.sh

# Commit and push
git add .
git commit -m "🔗 Fix all pricing buttons - Redirect to payment.html"
git push
```

---

## Verification Checklist

After making changes, test each page:

### ✅ osint.html
- [ ] Hero button "Request Investigation" → payment.html
- [ ] Email Risk "Start Analysis" → payment.html
- [ ] OSINT "Request Background Check" → payment.html
- [ ] Cybersecurity "Start Audit" → payment.html

### ✅ threat-intelligence.html
- [ ] Hero button → payment.html
- [ ] All pricing card buttons → payment.html

### ✅ email-risk.html
- [ ] Hero button → payment.html
- [ ] All pricing card buttons → payment.html

### ✅ pricing.html
- [ ] All pricing card buttons → payment.html

### ✅ about.html
- [ ] CTA buttons → payment.html

---

## Expected Result

**Before:**
```html
<a href="#contact" class="btn">Start Analysis →</a>
```

**After:**
```html
<a href="payment.html" class="btn">Start Analysis →</a>
```

---

## Testing

1. Visit: https://akatron-ai.github.io/akatron-website/
2. Go to each service page
3. Click any pricing button
4. Should redirect to: https://akatron-ai.github.io/akatron-website/payment.html
5. ✅ If it works, you're done!

---

## Need Help?

If you encounter any issues:
1. Check that you replaced ALL instances
2. Make sure you saved the file
3. Wait 1-2 minutes for GitHub Pages to rebuild
4. Clear your browser cache (Ctrl+Shift+R)

---

## Quick Links

- **Website**: https://akatron-ai.github.io/akatron-website/
- **Repository**: https://github.com/akatron-ai/akatron-website
- **Payment Page**: https://akatron-ai.github.io/akatron-website/payment.html
