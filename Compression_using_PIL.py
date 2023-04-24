from PIL import Image

# Open the image file
img = Image.open("image.jpg")

# Compress the image by reducing the quality
img.save("compressed.jpg", optimize=True, quality=50)
