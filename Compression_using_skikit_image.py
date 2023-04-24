from skimage.io import imread, imsave
from skimage.measure import compare_psnr

# Load the image
img = imread('image.jpg')

# Compress the image using LZW
compressed_img = imsave('compressed_lzw.tiff', img, plugin='tifffile', compress='lzw')

# Compute the peak signal-to-noise ratio (PSNR)
psnr = compare_psnr(img, compressed_img)
