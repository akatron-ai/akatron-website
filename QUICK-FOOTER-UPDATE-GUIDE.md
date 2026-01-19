# ⚡ QUICK FOOTER UPDATE - Find & Replace Method

## Fastest Way to Update All 6 Remaining Files (2 Minutes!)

Instead of editing each file manually, use GitHub's built-in editor with find-replace:

---

## 📋 STEP-BY-STEP:

### For Each File (email-risk.html, threat-intelligence.html, blog.html, privacy-policy.html, terms-of-service.html, disclaimer.html):

1. **Open the file on GitHub**
2. **Click Edit (pencil icon)**
3. **Press `Ctrl + H` (Windows) or `Cmd + H` (Mac)** - This opens Find & Replace
4. **In "Find" box, paste this:**

```html
    <footer class="site-footer">
        <p><strong>AKATRON</strong> — Elite Cybersecurity & OSINT Intelligence</p>
        <p>
            <a href="privacy-policy.html" style="color: #DAA520; text-decoration: none; margin: 0 10px;">Privacy Policy</a> | 
            <a href="terms-of-service.html" style="color: #DAA520; text-decoration: none; margin: 0 10px;">Terms of Service</a> | 
            <a href="disclaimer.html" style="color: #DAA520; text-decoration: none; margin: 0 10px;">Disclaimer</a>
        </p>
        <p>Delivering confidential, ethical, and actionable intelligence.</p>
        <p>© 2025 AKATRON. All rights reserved.</p>
```

5. **In "Replace" box, paste this:**

```html
    <footer class="site-footer">
        <p><strong>AKATRON</strong> — Elite Cybersecurity & OSINT Intelligence</p>
        
        <!-- Social Media Links -->
        <div style="margin: 20px 0;">
            <a href="https://www.linkedin.com/in/arpit-katiyar-akatron" target="_blank" rel="noopener noreferrer" style="color: #DAA520; text-decoration: none; margin: 0 15px; font-size: 16px; transition: all 0.3s ease;">
                <span style="display: inline-flex; align-items: center; gap: 8px;">
                    <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                    </svg>
                    LinkedIn
                </span>
            </a>
            <a href="https://twitter.com/AKATRON_Cyber" target="_blank" rel="noopener noreferrer" style="color: #DAA520; text-decoration: none; margin: 0 15px; font-size: 16px; transition: all 0.3s ease;">
                <span style="display: inline-flex; align-items: center; gap: 8px;">
                    <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                    </svg>
                    Twitter
                </span>
            </a>
            <a href="https://github.com/akatron-ai" target="_blank" rel="noopener noreferrer" style="color: #DAA520; text-decoration: none; margin: 0 15px; font-size: 16px; transition: all 0.3s ease;">
                <span style="display: inline-flex; align-items: center; gap: 8px;">
                    <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                    </svg>
                    GitHub
                </span>
            </a>
        </div>
        
        <p>
            <a href="privacy-policy.html" style="color: #DAA520; text-decoration: none; margin: 0 10px;">Privacy Policy</a> | 
            <a href="terms-of-service.html" style="color: #DAA520; text-decoration: none; margin: 0 10px;">Terms of Service</a> | 
            <a href="disclaimer.html" style="color: #DAA520; text-decoration: none; margin: 0 10px;">Disclaimer</a> | 
            <a href="blog.html" style="color: #DAA520; text-decoration: none; margin: 0 10px;">Blog</a>
        </p>
        <p>Delivering confidential, ethical, and actionable intelligence.</p>
        <p>© 2026 AKATRON. All rights reserved.</p>
```

6. **Click "Replace All"**
7. **Scroll down and commit:** `Add LinkedIn profile to footer`
8. **Done! Move to next file**

---

## ⚠️ IMPORTANT NOTES:

- **blog.html** doesn't have the last `<p class="disclaimer">` line, so the find text is slightly different
- **Some files** might have `© 2025` instead of `© 2026` - that's fine, the replace will update it
- If "Replace All" doesn't work, just manually find the footer and replace it

---

## 📝 FILES TO UPDATE:

1. ✅ email-risk.html
2. ✅ threat-intelligence.html  
3. ✅ blog.html
4. ✅ privacy-policy.html
5. ✅ terms-of-service.html
6. ✅ disclaimer.html

---

## ⏱️ TIME ESTIMATE:

- 20 seconds per file
- Total: 2 minutes for all 6 files

---

## 🎉 AFTER YOU'RE DONE:

All 8 HTML pages will have:
- ✅ LinkedIn profile link with icon
- ✅ Twitter link with icon
- ✅ GitHub link with icon
- ✅ Updated copyright to 2026
- ✅ Blog link added to footer

**Then we move to Step 2: Google Search Console!**
