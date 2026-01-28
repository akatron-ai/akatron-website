# Manual Update Steps - COPY & PASTE READY

## ⚡ FASTEST METHOD (GitHub Web Editor - 3 Minutes)

### STEP 1: Open index.html for Editing
1. Go to: https://github.com/akatron-ai/akatron-website/blob/main/index.html
2. Click the **pencil icon** (✏️) in the top right to edit
3. You're now in the GitHub web editor

---

### STEP 2: Add Button Group CSS

**Find this code (around line 216-219):**
```css
        .hero .btn span {
            position: relative;
            z-index: 1;
        }
```

**Add this CSS RIGHT AFTER the closing brace `}`:**

```css
        
        /* Button Group Styles */
        .btn-group {
            position: relative;
            z-index: 1;
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
        }

        /* Secondary Button (Outline Gold) */
        .btn-secondary {
            background: transparent !important;
            color: #d4af37 !important;
            border: 2px solid #d4af37 !important;
            box-shadow: 
                0 10px 40px rgba(212, 175, 55, 0.2),
                inset 0 0 0 rgba(212, 175, 55, 0.1) !important;
        }

        .btn-secondary::before {
            background: linear-gradient(135deg, rgba(212, 175, 55, 0.1), rgba(244, 228, 166, 0.1)) !important;
        }

        .btn-secondary:hover {
            background: rgba(212, 175, 55, 0.1) !important;
            border-color: #f4e4a6 !important;
            color: #f4e4a6 !important;
            box-shadow: 
                0 15px 50px rgba(212, 175, 55, 0.4),
                0 0 0 1px rgba(212, 175, 55, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
        }

        @media (max-width: 768px) {
            .btn-group {
                flex-direction: column;
                width: 100%;
            }
            
            .btn-group .btn {
                width: 100%;
                max-width: 300px;
            }
        }
```

**Result should look like:**
```css
        .hero .btn span {
            position: relative;
            z-index: 1;
        }
        
        /* Button Group Styles */
        .btn-group {
            position: relative;
            z-index: 1;
            ...
        }
        
        /* Floating particles effect */
        @keyframes float {
```

---

### STEP 3: Update Hero Button

**Use Ctrl+F (or Cmd+F on Mac) to find:**
```
Explore Services
```

**You'll find this line (around line 454):**
```html
        <a href="#services" class="btn"><span>Explore Services</span></a>
```

**Replace it with:**
```html
        <div class="btn-group">
            <a href="#services" class="btn btn-primary"><span>Explore Services</span></a>
            <a href="request-demo.html" class="btn btn-secondary"><span>Request Demo</span></a>
        </div>
```

---

### STEP 4: Commit Changes

1. Scroll to the bottom of the page
2. In the "Commit changes" box, enter:
   - **Title:** `🎨 Add Request Demo button to homepage`
   - **Description:** `Added button group with Explore Services and Request Demo buttons`
3. Click **"Commit changes"** button

---

## ✅ VERIFICATION

After committing (wait ~1 minute for GitHub Pages to rebuild):

1. Visit: https://akatron-ai.github.io/akatron-website/
2. Check that you see TWO buttons in the hero section
3. Verify the buttons look good on desktop and mobile
4. Click "Request Demo" - should open the demo form page
5. Test form submission

---

## 🎯 WHAT YOU'LL SEE

### Before:
```
AKATRON
Elite Cybersecurity & OSINT Intelligence

[Explore Services]
```

### After:
```
AKATRON
Elite Cybersecurity & OSINT Intelligence

[Explore Services] [Request Demo]
```

---

## 🔧 TROUBLESHOOTING

### If buttons don't appear:
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Wait 2-3 minutes for GitHub Pages to rebuild
- Check browser console for errors (F12)

### If styling looks wrong:
- Verify you copied ALL the CSS code
- Check that there are no syntax errors (missing braces, etc.)
- Make sure the CSS was added in the right location

### If you made a mistake:
- Go to the repository
- Click "History" or "Commits"
- Find the previous version
- Click "Revert this commit"

---

## 📊 EXPECTED TIMELINE

- **Opening file:** 30 seconds
- **Adding CSS:** 1 minute
- **Updating button:** 30 seconds
- **Committing:** 30 seconds
- **GitHub Pages rebuild:** 1-2 minutes
- **Testing:** 1 minute

**Total:** ~5 minutes

---

## 💡 PRO TIPS

1. **Use Ctrl+F / Cmd+F** to quickly find the sections
2. **Copy the entire code blocks** - don't type manually
3. **Check line numbers** in the editor to verify location
4. **Preview before committing** if your editor supports it
5. **Test on mobile** after deployment

---

## 🚀 NEXT STEPS AFTER IMPLEMENTATION

1. ✅ Test the homepage thoroughly
2. ✅ Submit a test demo request
3. ✅ Check Formspree dashboard for the submission
4. ✅ Add demo buttons to service pages (optional)
5. ✅ Set up Google Ads campaigns

---

**Ready? Let's do this!** 🎉

Open the file and follow the 4 steps above. You've got this!
