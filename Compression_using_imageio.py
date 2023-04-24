import imageio

# Load the image
img = imageio.imread('image.jpg')

# Compress the image using JPEG
imageio.imwrite('compressed.jpg', img, format='jpeg', quality=50)
