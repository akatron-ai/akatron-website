# AKATRON Website - Demo Button Integration Guide

## ✅ COMPLETED
- Formspree form connected with ID: `xwvbeajl`
- Demo form is live at: https://akatron-ai.github.io/akatron-website/request-demo.html

## 🎯 PENDING UPDATES

### Step 1: Update index.html - Add Button Group CSS

**Location:** After line 218 (after `.hero .btn span` styles)

**Add this CSS:**

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

/* Primary Button - Uses existing .hero .btn styles */
.btn-primary {
    /* Inherits from .hero .btn */
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

### Step 2: Update index.html - Replace Hero Button

**Location:** Line 454 (in hero section)

**Replace:**
```html
<a href="#services" class="btn"><span>Explore Services</span></a>
```

**With:**
```html
<div class="btn-group">
    <a href="#services" class="btn btn-primary"><span>Explore Services</span></a>
    <a href="request-demo.html" class="btn btn-secondary"><span>Request Demo</span></a>
</div>
```

---

## 📄 SERVICE PAGES UPDATES

### osint.html - Add Demo Button

**Location:** After main description paragraph in hero section

**Add:**
```html
<div class="btn-group" style="margin-top: 30px;">
    <a href="pricing.html" class="btn btn-primary"><span>View Pricing</span></a>
    <a href="request-demo.html" class="btn btn-secondary"><span>Request Demo</span></a>
</div>
```

### threat-intelligence.html - Add Demo Button

**Location:** After main description paragraph in hero section

**Add:**
```html
<div class="btn-group" style="margin-top: 30px;">
    <a href="pricing.html" class="btn btn-primary"><span>View Pricing</span></a>
    <a href="request-demo.html" class="btn btn-secondary"><span>Request Demo</span></a>
</div>
```

### email-risk.html - Add Demo Button

**Location:** After main description paragraph in hero section

**Add:**
```html
<div class="btn-group" style="margin-top: 30px;">
    <a href="pricing.html" class="btn btn-primary"><span>View Pricing</span></a>
    <a href="request-demo.html" class="btn btn-secondary"><span>Request Demo</span></a>
</div>
```

### pricing.html - Add Demo Buttons to Cards

**Location:** In each pricing card, replace or add alongside "Get Started" buttons

**Add:**
```html
<div class="btn-group" style="margin-top: 20px;">
    <a href="request-demo.html" class="btn btn-primary"><span>Request Demo</span></a>
</div>
```

---

## 🎨 DESIGN NOTES

- **Primary Button (Gold):** Solid gold gradient - main call-to-action
- **Secondary Button (Outline):** Gold outline with transparent background - secondary action
- Both buttons have smooth hover effects and glow animations
- Fully responsive: side-by-side on desktop, stacked on mobile
- Matches existing AKATRON gold theme (#d4af37, #f4e4a6)

---

## ✅ TESTING CHECKLIST

After implementing:
- [ ] Homepage hero has both buttons
- [ ] Buttons are side-by-side on desktop
- [ ] Buttons stack vertically on mobile
- [ ] Hover effects work smoothly
- [ ] "Request Demo" links to request-demo.html
- [ ] Service pages have demo buttons
- [ ] All buttons match gold theme
- [ ] Form submissions work (test at request-demo.html)

---

## 📧 FORMSPREE SETUP

✅ **Already Connected!**
- Form ID: `xwvbeajl`
- Submissions go to: arpitkatiayar261@gmail.com
- Form URL: https://akatron-ai.github.io/akatron-website/request-demo.html

---

## 🚀 NEXT STEPS

1. Implement CSS changes in index.html
2. Update hero button in index.html
3. Add demo buttons to service pages
4. Test on desktop and mobile
5. Monitor form submissions in Formspree dashboard

---

**Need help?** All code snippets are ready to copy-paste!
