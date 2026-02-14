from PIL import Image, ImageDraw, ImageFont
import os

# Thumbnail size
WIDTH, HEIGHT = 1280, 720

# Background image (first from images folder)
images = sorted(os.listdir("images"))
bg = Image.open(os.path.join("images", images[0])).resize((WIDTH, HEIGHT))

draw = ImageDraw.Draw(bg)

# Title text
topic = open("script.txt", "r").read().split("\n")[0][:50] 
text = f"{topic}"

# Load a font
try:
    font = ImageFont.truetype("arial.ttf", 80)
except:
    font = ImageFont.load_default()

# Text Position
text_w, text_h = draw.textsize(text, font=font)
x = (WIDTH - text_w) / 2
y = HEIGHT - text_h - 50

# Draw text with outline
outline_color = "black"
fill_color = "white"

# Outline
for offset in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
    draw.text((x+offset[0], y+offset[1]), text, font=font, fill=outline_color)

# Main text
draw.text((x, y), text, font=font, fill=fill_color)

# Save
bg.save("thumbnail.png")
print("Thumbnail created → thumbnail.png")
