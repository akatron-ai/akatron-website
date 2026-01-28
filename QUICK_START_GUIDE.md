# 🚀 QUICK START - Add Demo Button (3 Minutes)

## ✅ DEMO PAGE IS READY!

Your demo page is now **beautifully redesigned** with your gold theme:
- **Live URL:** https://akatron-ai.github.io/akatron-website/request-demo.html
- **Status:** ✅ Working and styled perfectly
- **Form:** ✅ Connected to Formspree (submissions go to your email)

---

## 🎯 NEXT STEP: Add Button to Homepage

You need to make **2 simple changes** to `index.html`:

### 📍 CHANGE #1: Add Button CSS

**Location:** After line 219

1. Open: https://github.com/akatron-ai/akatron-website/edit/main/index.html
2. Press `Ctrl+F` (or `Cmd+F`) and search for: `.hero .btn span`
3. You'll find this code around line 216-219:

```css
        .hero .btn span {
            position: relative;
            z-index: 1;
        }
```

4. **Place your cursor RIGHT AFTER the closing `}`**
5. **Press Enter** to create a new line
6. **Copy and paste this CSS:**

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
        
        /* Button Group Styles */    ← YOUR NEW CSS STARTS HERE
        .btn-group {
            ...
        }
        
        /* Floating particles effect */
        @keyframes float {
```

---

### 📍 CHANGE #2: Update Hero Button

**Location:** Around line 454

1. Still in the same editor, press `Ctrl+F` and search for: `Explore Services`
2. You'll find this line:

```html
        <a href="#services" class="btn"><span>Explore Services</span></a>
```

3. **Select and DELETE that entire line**
4. **Replace it with:**

```html
        <div class="btn-group">
            <a href="#services" class="btn btn-primary"><span>Explore Services</span></a>
            <a href="request-demo.html" class="btn btn-secondary"><span>Request Demo</span></a>
        </div>
```

---

### 💾 SAVE YOUR CHANGES

1. Scroll to the bottom of the page
2. In "Commit changes" box:
   - **Title:** `Add Request Demo button to homepage`
   - **Description:** `Added dual CTA buttons with gold theme`
3. Click **"Commit changes"**

---

## ✅ VERIFICATION (After 1-2 minutes)

1. Visit: https://akatron-ai.github.io/akatron-website/
2. You should see **TWO buttons** in the hero section:
   - **[Explore Services]** - Gold gradient
   - **[Request Demo]** - Gold outline
3. Click "Request Demo" - should open your beautiful demo page
4. Test the form - submit a test request

---

## 🎉 WHAT YOU'LL HAVE

### Homepage Before:
```
┌────────────────────────┐
│      AKATRON           │
│                        │
│  [Explore Services]    │
└────────────────────────┘
```

### Homepage After:
```
┌──────────────────────────────────┐
│          AKATRON                 │
│                                  │
│  [Explore Services] [Request Demo]
└──────────────────────────────────┘
```

### Demo Page:
- ✅ Premium gold theme matching your website
- ✅ Professional form with all fields
- ✅ Responsive design (mobile + desktop)
- ✅ Working Formspree integration
- ✅ Success message after submission

---

## 🔧 TROUBLESHOOTING

### If you can't find the lines:
- Use `Ctrl+F` / `Cmd+F` to search
- Look for line numbers on the left side of the editor
- The CSS is around line 216-219
- The button is around line 454

### If something goes wrong:
- GitHub keeps all versions - you can always revert
- Check the commit history
- Or ask me for help!

---

## 📊 TIMELINE

- **Opening editor:** 30 seconds
- **Change #1 (CSS):** 1 minute
- **Change #2 (Button):** 30 seconds
- **Committing:** 30 seconds
- **GitHub Pages rebuild:** 1-2 minutes
- **Testing:** 1 minute

**Total:** ~5 minutes

---

## 🚀 READY?

**Click here to start:** https://github.com/akatron-ai/akatron-website/edit/main/index.html

Follow the 2 changes above, commit, and you're done! 🎉

---

**Need help?** Just ask - I'm here to assist! 💪
