# 📝 HOW TO ADD PRICING TO YOUR WEBSITE

## **SIMPLE COPY-PASTE METHOD**

---

### **STEP 1: Open index.html for editing**

1. Go to: https://github.com/akatron-ai/akatron-website/edit/main/index.html
2. The file will open in edit mode

---

### **STEP 2: Find the insertion point**

3. Press `Ctrl+F` (or `Cmd+F` on Mac)
4. Search for: `<!-- CONTACT SECTION -->`
5. You'll find it around line 560

---

### **STEP 3: Insert pricing section**

6. Place your cursor **BEFORE** the line `<!-- CONTACT SECTION -->`
7. Press Enter to create a new blank line
8. Open this file in a new tab: https://github.com/akatron-ai/akatron-website/blob/main/pricing-section.html
9. Click the "Raw" button (top right)
10. Select ALL the code (`Ctrl+A` or `Cmd+A`)
11. Copy it (`Ctrl+C` or `Cmd+C`)
12. Go back to the index.html edit tab
13. Paste the code (`Ctrl+V` or `Cmd+V`)

---

### **STEP 4: Save changes**

14. Scroll to the bottom
15. Click "Commit changes..."
16. Add commit message: "Add pricing section to homepage"
17. Click "Commit changes"

---

## **WHAT IT SHOULD LOOK LIKE:**

```html
    </section>

    <!-- PREMIUM PRICING SECTION -->
    <section id="pricing" class="section" style="background: linear-gradient(135deg, #0a0e17 0%, #1a1f2e 50%, #0a0e17 100%);">
        ... (pricing code here) ...
    </section>

    <!-- CONTACT SECTION -->
    <section id="contact" class="section">
```

---

## **VERIFICATION:**

After committing:
1. Wait 1-2 minutes for GitHub Pages to rebuild
2. Visit: https://akatron-ai.github.io/akatron-website/
3. Scroll down - you should see the pricing section!

---

## **NEED HELP?**

If you get stuck, just reply with a screenshot and I'll guide you through it!

---

**Estimated Time:** 3-5 minutes