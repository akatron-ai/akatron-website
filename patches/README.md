# Patches Folder - Demo Button Implementation

This folder contains ready-to-use patch files for adding "Request Demo" buttons to the AKATRON website.

## 📁 Files in This Folder

| File | Purpose | Use When |
|------|---------|----------|
| `button-group-styles.css` | CSS for button styling | Adding button styles to index.html |
| `hero-button-update.html` | HTML for hero buttons | Updating homepage hero section |
| `VISUAL_GUIDE.md` | Visual implementation guide | Need step-by-step visual instructions |

## 🚀 Quick Start (5 Minutes)

### Step 1: Add CSS
1. Open `index.html` in GitHub
2. Find line 218 (search for `.hero .btn span`)
3. Copy content from `button-group-styles.css`
4. Paste after the `.hero .btn span { ... }` block

### Step 2: Update Button
1. Still in `index.html`
2. Find line 454 (search for `Explore Services`)
3. Copy content from `hero-button-update.html`
4. Replace the single button line
5. Commit changes

**Done!** Your homepage now has dual call-to-action buttons.

## 📖 Documentation

For detailed instructions, see:
- [VISUAL_GUIDE.md](VISUAL_GUIDE.md) - Step-by-step visual guide
- [../DEMO_BUTTONS_SUMMARY.md](../DEMO_BUTTONS_SUMMARY.md) - Complete summary
- [../IMPLEMENTATION_GUIDE.md](../IMPLEMENTATION_GUIDE.md) - Full implementation guide

## 🎯 What You'll Get

```
BEFORE:                    AFTER:
[Explore Services]    →    [Explore Services] [Request Demo]
```

## ✅ Verification

After implementation:
- [ ] Two buttons visible on homepage
- [ ] Buttons styled with gold theme
- [ ] Desktop: buttons side-by-side
- [ ] Mobile: buttons stacked
- [ ] "Request Demo" links to request-demo.html
- [ ] Form submissions work

## 🔗 Related Files

- Main guide: [../DEMO_BUTTONS_SUMMARY.md](../DEMO_BUTTONS_SUMMARY.md)
- Update instructions: [../UPDATE_INSTRUCTIONS.md](../UPDATE_INSTRUCTIONS.md)
- Python script: [../scripts/add-demo-buttons.py](../scripts/add-demo-buttons.py)

## 💡 Tips

- **Backup first:** GitHub keeps version history, but you can create a branch
- **Test locally:** Clone repo and test before pushing
- **Use GitHub editor:** Easiest way for small changes
- **Check mobile:** Test responsive behavior

## 📞 Support

If you need help:
1. Check [VISUAL_GUIDE.md](VISUAL_GUIDE.md) for detailed steps
2. Review the patch files - they have inline comments
3. All code is ready to copy-paste!

---

**Last Updated:** 2026-01-28  
**Status:** Ready to Use  
**Difficulty:** Easy (copy-paste)
