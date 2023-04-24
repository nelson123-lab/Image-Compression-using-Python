import pywt
import numpy as np

# Load the image
img = cv2.imread('image.jpg')

# Perform the 2D discrete wavelet transform
coeffs = pywt.dwt2(img, 'haar')

# Discard high-frequency coefficients to compress the image
coeffs = [coeffs[0], (np.zeros_like(coeffs[1]), np.zeros_like(coeffs[2]))]

# Perform the inverse transform to reconstruct the compressed image
compressed_img = pywt.idwt2(coeffs, 'haar')

# Save the compressed image
cv2.imwrite('compressed.jpg', compressed_img)
