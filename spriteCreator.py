from PIL import Image, ImageDraw, ImageFont

# Define image size (wider than it is tall)
width, height = 200, 100

# Create a new image with a white background
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Add some text (which will be oriented vertically)
text = "Hello, Unity!"
font_path = "/Users/tarakaul/Downloads/Roboto/Roboto-Light.ttf"  # Provide the path to a vertical TTF font
font_size = 20  # Use an appropriate font size

# Load the vertical font and calculate the text size
font = ImageFont.truetype(font_path, font_size)
text_size = draw.textsize(text, font)

# Calculate the position to center the text vertically and position it to read top to bottom
x = (width - text_size[0]) / 2
y = (height - text_size[1]) / 2

# Add the text to the image with a vertical orientation
for char in text:
    draw.text((x, y), char, fill="black", font=font)
    y += font.getsize(char)[1]

# Save the image as a PNG file
image.save("output.png", "PNG")
