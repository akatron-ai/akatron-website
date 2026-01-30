# 🎯 EXECUTE THIS TO COMPLETE EVERYTHING

## ✅ Status:
1. ✅ **Demo Form** - Company Name and Role are now optional (COMPLETED)
2. ⏳ **Pricing Buttons** - Need to fix 17 buttons across 5 files (PENDING)

---

## 🚀 FASTEST SOLUTION (Copy & Paste):

### For Mac/Linux:
```bash
cd /path/to/akatron-ai/akatron-website

# Fix all files at once
sed -i '' 's/href="#contact"/href="payment.html"/g' osint.html threat-intelligence.html email-risk.html pricing.html about.html

# Commit and push
git add .
git commit -m "🔗 Fix all pricing buttons - Redirect to payment.html"
git push
```

### For Linux (without Mac):
```bash
cd /path/to/akatron-ai/akatron-website

# Fix all files at once
sed -i 's/href="#contact"/href="payment.html"/g' osint.html threat-intelligence.html email-risk.html pricing.html about.html

# Commit and push
git add .
git commit -m "🔗 Fix all pricing buttons - Redirect to payment.html"
git push
```

### For Windows (PowerShell):
```powershell
cd C:\path\to\akatron-ai\akatron-website

# Fix all files
@('osint.html','threat-intelligence.html','email-risk.html','pricing.html','about.html') | ForEach-Object {
    (Get-Content $_) -replace 'href="#contact"', 'href="payment.html"' | Set-Content $_
}

# Commit and push
git add .
git commit -m "🔗 Fix all pricing buttons - Redirect to payment.html"
git push
```

---

## 📊 What This Fixes:

| File | Buttons Fixed | Lines Changed |
|------|---------------|---------------|
| osint.html | 4 buttons | Lines 80, 37, 91, 145 |
| threat-intelligence.html | 4 buttons | Lines 82, 237, 291, 345 |
| email-risk.html | 4 buttons | Lines 82, 237, 291, 345 |
| pricing.html | 3 buttons | Lines 73, 127, 251 |
| about.html | 2 buttons | Lines 268, 272 |

**Total**: 17 buttons across 5 files

---

## ✅ After Running:

1. Wait 1-2 minutes for GitHub Pages to rebuild
2. Test: https://akatron-ai.github.io/akatron-website/osint.html
3. Click any pricing button
4. Should redirect to: https://akatron-ai.github.io/akatron-website/payment.html
5. ✅ DONE!

---

## 🎉 Result:

**Before**: Clicking "Get Started" → Scrolls to contact form  
**After**: Clicking "Get Started" → Redirects to payment page

---

## 💡 If You Don't Have Repo Cloned:

1. Clone it first:
```bash
git clone https://github.com/akatron-ai/akatron-website.git
cd akatron-website
```

2. Then run the fix command above

---

## ⚡ Alternative: Manual Fix (5 minutes)

If you prefer to do it manually via GitHub web interface:

1. [Edit osint.html](https://github.com/akatron-ai/akatron-website/edit/main/osint.html)
2. [Edit threat-intelligence.html](https://github.com/akatron-ai/akatron-website/edit/main/threat-intelligence.html)
3. [Edit email-risk.html](https://github.com/akatron-ai/akatron-website/edit/main/email-risk.html)
4. [Edit pricing.html](https://github.com/akatron-ai/akatron-website/edit/main/pricing.html)
5. [Edit about.html](https://github.com/akatron-ai/akatron-website/edit/main/about.html)

For each file:
- Press `Ctrl+H` (Find & Replace)
- Find: `#contact`
- Replace: `payment.html`
- Click "Commit changes"

---

**Choose your method and execute now! Everything will be complete in under 2 minutes!** 🚀
