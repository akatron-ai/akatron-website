#!/bin/bash

# Update GTM Container ID from GTM-AKATRON to GTM-PM5C4K52

# Update index.html
sed -i 's/GTM-AKATRON/GTM-PM5C4K52/g' index.html

# Update blog.html  
sed -i 's/GTM-AKATRON/GTM-PM5C4K52/g' blog.html

echo "✅ GTM Container ID updated to GTM-PM5C4K52 in both files!"
echo "Files updated: index.html, blog.html"