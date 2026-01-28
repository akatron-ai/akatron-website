# AKATRON Website - Demo Button Implementation Guide

## ✅ STATUS UPDATE

### COMPLETED ✓
1. **Formspree Integration** - Form ID `xwvbeajl` connected
2. **Demo Page Live** - https://akatron-ai.github.io/akatron-website/request-demo.html
3. **Documentation Created** - UPDATE_INSTRUCTIONS.md added to repo
4. **Helper Script Created** - scripts/add-demo-buttons.py added to repo

### PENDING (Manual Implementation Required)
Due to file size (48KB), the following changes need manual implementation:

---

## 🎯 IMPLEMENTATION STEPS

### STEP 1: Update index.html - Add Button CSS

**File:** `index.html`  
**Line:** After line 218 (after `.hero .btn span { ... }`)

**Action:** Insert this CSS block:

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

---

### STEP 2: Update index.html - Replace Hero Button

**File:** `index.html`  
**Line:** ~454 (in hero section)

**Find:**
```html
        <a href="#services" class="btn"><span>Explore Services</span></a>
```

**Replace with:**
```html
        <div class="btn-group">
            <a href="#services" class="btn btn-primary"><span>Explore Services</span></a>
            <a href="request-demo.html" class="btn btn-secondary"><span>Request Demo</span></a>
        </div>
```

---

### STEP 3: Update Service Pages (Optional but Recommended)

#### osint.html
Find the hero section and add after the description:
```html
<div class="btn-group" style="margin-top: 30px;">
    <a href="pricing.html" class="btn btn-primary"><span>View Pricing</span></a>
    <a href="request-demo.html" class="btn btn-secondary"><span>Request Demo</span></a>
</div>
```

#### threat-intelligence.html
Same as above - add button group in hero section

#### email-risk.html
Same as above - add button group in hero section

#### pricing.html
Add to each pricing card:
```html
<a href="request-demo.html" class="btn" style="margin-top: 15px; display: block;">Request Demo</a>
```

---

## 🔍 HOW TO IMPLEMENT

### Option A: GitHub Web Interface (Easiest)
1. Go to https://github.com/akatron-ai/akatron-website
2. Click on `index.html`
3. Click the pencil icon (Edit)
4. Make the two changes above
5. Scroll down and commit changes

### Option B: Local Development
1. Clone the repository
2. Open `index.html` in your code editor
3. Make the changes
4. Commit and push

### Option C: Use GitHub Codespaces
1. Open repository in Codespaces
2. Edit `index.html`
3. Commit changes

---

## ✅ VERIFICATION CHECKLIST

After implementation, verify:

- [ ] Homepage loads without errors
- [ ] Two buttons appear in hero section
- [ ] "Explore Services" button is gold (primary)
- [ ] "Request Demo" button is outline gold (secondary)
- [ ] Buttons are side-by-side on desktop
- [ ] Buttons stack vertically on mobile
- [ ] Hover effects work smoothly
- [ ] "Request Demo" links to request-demo.html
- [ ] Form submissions work

---

## 📊 EXPECTED RESULTS

### Desktop View
```
[Explore Services] [Request Demo]
   (Gold Button)   (Outline Gold)
```

### Mobile View
```
[Explore Services]
   (Gold Button)
       
[Request Demo]
 (Outline Gold)
```

---

## 🎨 DESIGN SPECIFICATIONS

- **Primary Button:** Solid gold gradient (#d4af37 to #f4e4a6)
- **Secondary Button:** Transparent with gold border (#d4af37)
- **Gap:** 20px between buttons
- **Hover:** Glow effect with color shift
- **Mobile Breakpoint:** 768px
- **Font:** Space Grotesk, uppercase, letter-spacing 0.1em

---

## 🚀 NEXT STEPS AFTER IMPLEMENTATION

1. Test on multiple devices
2. Monitor form submissions in Formspree
3. Set up Google Ads campaigns
4. Track conversion rates
5. A/B test button copy

---

## 📞 SUPPORT

If you need help implementing:
1. Check the gists created:
   - https://gist.github.com/akatron-ai/c819fe122e63b0730bd8ccee816a957b
   - https://gist.github.com/akatron-ai/488f6af634a2b4339b3680030af97ef9
2. Review UPDATE_INSTRUCTIONS.md in the repo
3. Use the Python script in scripts/add-demo-buttons.py

---

**Last Updated:** 2026-01-28  
**Status:** Ready for Implementation  
**Estimated Time:** 10-15 minutes
