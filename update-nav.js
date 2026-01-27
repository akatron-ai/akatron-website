const fs = require('fs');
const path = require('path');

// Files to update
const files = [
    'index.html',
    'osint.html',
    'threat-intelligence.html',
    'email-risk.html',
    'blog.html'
];

// Navigation templates for each page
const navTemplates = {
    'index.html': `        <nav>
            <a href="index.html" class="active">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>`,
    
    'osint.html': `        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html" class="active">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>`,
    
    'threat-intelligence.html': `        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html" class="active">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>`,
    
    'email-risk.html': `        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html" class="active">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html">Blog</a>
            <a href="about.html">About</a>
        </nav>`,
    
    'blog.html': `        <nav>
            <a href="index.html">Home</a>
            <a href="osint.html">OSINT</a>
            <a href="threat-intelligence.html">Threat Intel</a>
            <a href="email-risk.html">Email Risk</a>
            <a href="pricing.html">Pricing</a>
            <a href="blog.html" class="active">Blog</a>
            <a href="about.html">About</a>
        </nav>`
};

console.log('🚀 Starting Navigation Update...\n');

let updated = 0;
let failed = 0;

files.forEach(file => {
    try {
        console.log(`📝 Processing ${file}...`);
        
        // Read file
        const content = fs.readFileSync(file, 'utf8');
        
        // Replace navigation using regex
        const navRegex = /<nav>[\s\S]*?<\/nav>/;
        const newContent = content.replace(navRegex, navTemplates[file]);
        
        // Write back
        fs.writeFileSync(file, newContent, 'utf8');
        
        console.log(`✅ ${file} updated successfully\n`);
        updated++;
    } catch (error) {
        console.log(`❌ Error updating ${file}: ${error.message}\n`);
        failed++;
    }
});

console.log('================================');
console.log(`✨ Update Complete!`);
console.log(`   ✅ Successfully updated: ${updated} files`);
console.log(`   ❌ Failed: ${failed} files`);
console.log('================================\n');

if (updated > 0) {
    console.log('📝 Next steps:');
    console.log('   1. Review changes: git diff');
    console.log('   2. Commit: git add *.html');
    console.log('   3. Commit: git commit -m "✨ Update navigation menus"');
    console.log('   4. Push: git push origin main');
}
