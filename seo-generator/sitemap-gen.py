#!/usr/bin/env python3
"""Generate sitemap.xml from all existing SEO pages."""
import os, glob
from datetime import datetime

SITE_URL = "https://whatsapp-viewer.netlify.app"
OUTPUT = "../sitemap.xml"

def generate():
    urls = [
        ("/", "1.0", "weekly"),
        ("/app", "0.9", "weekly"),
        ("/how-to-view-whatsapp-messages", "0.8", "monthly"),
        ("/read-whatsapp-messages-online-free", "0.8", "monthly"),
        ("/whatsapp-spy-tool-free", "0.8", "monthly"),
        ("/whatsapp-tracker-online", "0.8", "monthly"),
        ("/whatsapp-message-viewer-2026", "0.8", "monthly"),
        ("/free-whatsapp-spy", "0.8", "monthly"),
        ("/whatsapp-viewer-no-verification", "0.8", "monthly"),
        ("/voir-messages-whatsapp-gratuit", "0.8", "monthly"),
        ("/espionner-whatsapp-en-ligne", "0.8", "monthly"),
    ]
    
    # Add generated SEO pages
    for html_file in glob.glob("../seo-pages/*/*.html"):
        path = "/" + html_file
        urls.append((path, "0.6", "monthly"))
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    for path, priority, freq in urls:
        xml.append("  <url>")
        xml.append(f"    <loc>{SITE_URL}{path}</loc>")
        xml.append(f"    <changefreq>{freq}</changefreq>")
        xml.append(f"    <priority>{priority}</priority>")
        xml.append(f"    <lastmod>{today}</lastmod>")
        xml.append("  </url>")
    
    xml.append("</urlset>")
    
    with open(OUTPUT, "w") as f:
        f.write("\n".join(xml))
    
    print(f"✅ Sitemap generated: {len(urls)} URLs")

if __name__ == "__main__":
    generate()
