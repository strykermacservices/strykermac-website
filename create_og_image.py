#!/usr/bin/env python3
"""
Create professional OG share image for StrykerMac Services
1200x630px with dark theme matching the website design
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Create 1200x630 image
width, height = 1200, 630
image = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(image)

# Create gradient background (dark navy)
for y in range(height):
    # Gradient from #0a0e1a to #0f1935
    r1, g1, b1 = 10, 14, 26     # #0a0e1a
    r2, g2, b2 = 15, 25, 53     # #0f1935
    
    # Linear interpolation
    ratio = y / height
    r = int(r1 + (r2 - r1) * ratio)
    g = int(g1 + (g2 - g1) * ratio)
    b = int(b1 + (b2 - b1) * ratio)
    
    draw.line([(0, y), (width, y)], fill=(r, g, b))

# Define colors
white = '#FFFFFF'
blue_accent = '#3B82F6'
light_gray = '#E5E7EB'

# Try to load Segoe UI font (Windows default)
try:
    font_bold_large = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 72)
    font_bold_medium = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 48)
    font_regular_medium = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 32)
    font_regular_small = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 24)
    font_light_small = ImageFont.truetype("C:/Windows/Fonts/segoeuil.ttf", 20)
except:
    # Fallback to default font if Segoe UI not available
    try:
        font_bold_large = ImageFont.truetype("arial.ttf", 72)
        font_bold_medium = ImageFont.truetype("arialbd.ttf", 48)
        font_regular_medium = ImageFont.truetype("arial.ttf", 32)
        font_regular_small = ImageFont.truetype("arial.ttf", 24)
        font_light_small = ImageFont.truetype("arial.ttf", 20)
    except:
        font_bold_large = ImageFont.load_default()
        font_bold_medium = ImageFont.load_default()
        font_regular_medium = ImageFont.load_default()
        font_regular_small = ImageFont.load_default()
        font_light_small = ImageFont.load_default()

# Company name - prominent at top
company_name = "StrykerMac Services"
name_bbox = draw.textbbox((0, 0), company_name, font=font_bold_large)
name_width = name_bbox[2] - name_bbox[0]
name_x = (width - name_width) // 2
name_y = 80
draw.text((name_x, name_y), company_name, fill=white, font=font_bold_large)

# Tagline
tagline = "AI Assistants for Small Business"
tagline_bbox = draw.textbbox((0, 0), tagline, font=font_regular_medium)
tagline_width = tagline_bbox[2] - tagline_bbox[0]
tagline_x = (width - tagline_width) // 2
tagline_y = name_y + 90
draw.text((tagline_x, tagline_y), tagline, fill=light_gray, font=font_regular_medium)

# Value props in a clean grid
props = ["24/7 Availability", "48hr Deployment", "Custom Built"]
prop_y = tagline_y + 80
prop_spacing = 380  # Space between props horizontally
start_x = (width - (len(props) * prop_spacing - prop_spacing)) // 2

for i, prop in enumerate(props):
    prop_x = start_x + i * prop_spacing
    
    # Create a subtle box for each prop
    box_width = 340
    box_height = 80
    box_x = prop_x - box_width // 2
    box_y = prop_y - 10
    
    # Draw subtle border
    draw.rectangle([box_x, box_y, box_x + box_width, box_y + box_height], 
                  outline=blue_accent, width=2)
    
    # Add the text
    prop_bbox = draw.textbbox((0, 0), prop, font=font_bold_medium)
    prop_width = prop_bbox[2] - prop_bbox[0]
    text_x = prop_x - prop_width // 2
    text_y = prop_y + 20
    
    draw.text((text_x, text_y), prop, fill=blue_accent, font=font_bold_medium)

# Website URL at bottom
url = "strykermacservices.services"
url_bbox = draw.textbbox((0, 0), url, font=font_light_small)
url_width = url_bbox[2] - url_bbox[0]
url_x = (width - url_width) // 2
url_y = height - 60
draw.text((url_x, url_y), url, fill=light_gray, font=font_light_small)

# Add subtle accent line above URL
line_width = 200
line_x = (width - line_width) // 2
line_y = url_y - 20
draw.rectangle([line_x, line_y, line_x + line_width, line_y + 2], fill=blue_accent)

# Save the image
output_path = "C:/Users/Stryk/.openclaw/workspace/strykermac-website-repo/og-image.png"
image.save(output_path, "PNG", quality=95)

print(f"[SUCCESS] OG image created successfully: {output_path}")
print(f"[INFO] Dimensions: {width}x{height}px")
print(f"[INFO] Design: Dark gradient background with blue accents")
print(f"[INFO] Content: Company name, tagline, value props, and URL")