import cv2

# Load the image
img = cv2.imread('image.jpg')

# Compress the image by reducing the quality
cv2.imwrite('compressed.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])
