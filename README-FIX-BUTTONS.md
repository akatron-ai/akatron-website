# Fix All Pricing Buttons - Complete Guide

## ✅ What's Been Done

1. ✅ **request-demo.html** - Made "Company Name" and "Your Role" optional
2. ⏳ **Pricing buttons** - Need to be fixed on 5 pages

---

## 🎯 What Needs to Be Fixed

All pricing buttons currently link to `#contact` (scroll to bottom) but should link to `payment.html` (payment page).

### Files to Fix:
- osint.html (4 buttons)
- threat-intelligence.html (4 buttons)
- email-risk.html (4 buttons)
- pricing.html (3 buttons)
- about.html (2 buttons)

---

## 🚀 3 Ways to Fix (Choose One)

### Method 1: GitHub Actions (Easiest - 1 Click!)

1. Go to: https://github.com/akatron-ai/akatron-website/actions
2. Click on "Fix All Pricing Buttons" workflow
3. Click "Run workflow" button
4. Click green "Run workflow" button
5. Wait 30 seconds
6. ✅ Done! All files fixed automatically

---

### Method 2: Run Python Script Locally (2 Minutes)

```bash
# Clone the repo
git clone https://github.com/akatron-ai/akatron-website.git
cd akatron-website

# Run the fix script
python3 fix_all_buttons_now.py

# Commit and push
git add .
git commit -m "🔗 Fix all pricing buttons"
git push
```

---

### Method 3: Manual Fix via GitHub Web (5 Minutes)

For each file, do this:

#### 1. osint.html
1. Go to: https://github.com/akatron-ai/akatron-website/blob/main/osint.html
2. Click ✏️ Edit
3. Press `Ctrl+H` (Find & Replace)
4. Find: `#contact`
5. Replace: `payment.html`
6. Click "Commit changes"

#### 2. threat-intelligence.html
1. Go to: https://github.com/akatron-ai/akatron-website/blob/main/threat-intelligence.html
2. Click ✏️ Edit
3. `Ctrl+H` → Find: `#contact` → Replace: `payment.html`
4. Commit changes

#### 3. email-risk.html
1. Go to: https://github.com/akatron-ai/akatron-website/blob/main/email-risk.html
2. Click ✏️ Edit
3. `Ctrl+H` → Find: `#contact` → Replace: `payment.html`
4. Commit changes

#### 4. pricing.html
1. Go to: https://github.com/akatron-ai/akatron-website/blob/main/pricing.html
2. Click ✏️ Edit
3. `Ctrl+H` → Find: `#contact` → Replace: `payment.html`
4. Commit changes

#### 5. about.html
1. Go to: https://github.com/akatron-ai/akatron-website/blob/main/about.html
2. Click ✏️ Edit
3. `Ctrl+H` → Find: `#contact` → Replace: `payment.html`
4. Commit changes

---

## 🧪 Testing

After fixing:

1. Wait 1-2 minutes for GitHub Pages to rebuild
2. Visit: https://akatron-ai.github.io/akatron-website/osint.html
3. Scroll to pricing section
4. Click any "Start Analysis" or "Get Started" button
5. Should redirect to: https://akatron-ai.github.io/akatron-website/payment.html
6. ✅ If it works, you're done!

Test all pages:
- https://akatron-ai.github.io/akatron-website/osint.html
- https://akatron-ai.github.io/akatron-website/threat-intelligence.html
- https://akatron-ai.github.io/akatron-website/email-risk.html
- https://akatron-ai.github.io/akatron-website/pricing.html
- https://akatron-ai.github.io/akatron-website/about.html

---

## 📊 Progress Tracker

- [x] index.html - ✅ Already fixed
- [x] request-demo.html - ✅ Company & Role made optional
- [ ] osint.html - ⏳ Pending
- [ ] threat-intelligence.html - ⏳ Pending
- [ ] email-risk.html - ⏳ Pending
- [ ] pricing.html - ⏳ Pending
- [ ] about.html - ⏳ Pending

---

## 🎉 Expected Result

**Before:**
```html
<a href="#contact" class="btn">Start Analysis →</a>
```
Clicking this scrolls to contact form at bottom of page.

**After:**
```html
<a href="payment.html" class="btn">Start Analysis →</a>
```
Clicking this redirects to payment page with QR code.

---

## 💡 Recommendation

**Use Method 1 (GitHub Actions)** - It's the fastest and most reliable!

Just go to Actions tab and click "Run workflow". Done in 30 seconds!

---

## 📞 Need Help?

If you encounter issues:
1. Clear browser cache (`Ctrl+Shift+R`)
2. Wait 2-3 minutes for GitHub Pages to rebuild
3. Check that all files were saved after editing
4. Verify the replacement was done correctly

---

## 🔗 Quick Links

- **Repository**: https://github.com/akatron-ai/akatron-website
- **Website**: https://akatron-ai.github.io/akatron-website/
- **Actions**: https://github.com/akatron-ai/akatron-website/actions
- **Payment Page**: https://akatron-ai.github.io/akatron-website/payment.html

---

**Ready to fix? Choose your method above and let's do this! 🚀**
