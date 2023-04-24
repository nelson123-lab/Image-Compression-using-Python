# Image-Compression-using-Python

There are several ways to perform image compression in Python, but one of the most common approaches is to use the Pillow library. Pillow is a fork of the Python Imaging Library (PIL), which provides a variety of image processing capabilities.

## Using PIL
In the above code, we first open the image file using the Image.open() method from Pillow. We then use the save() method to save the image in a compressed format by specifying the optimize and quality parameters. The optimize parameter tells Pillow to optimize the Huffman coding used in the JPEG format, while the quality parameter controls the amount of compression applied to the image.

You can experiment with different values of the quality parameter to achieve the desired level of compression. However, keep in mind that reducing the quality too much can result in a loss of detail and visual artifacts in the compressed image.

# Using OpenCV
In the above code, we first load the image using the cv2.imread() method from OpenCV. We then use the cv2.imwrite() method to save the compressed image in JPEG format by specifying the cv2.IMWRITE_JPEG_QUALITY flag with a value of 50. This value controls the amount of compression applied to the image, with higher values resulting in less compression and better image quality.

You can experiment with different values of the compression quality to achieve the desired level of compression. However, keep in mind that reducing the quality too much can result in a loss of detail and visual artifacts in the compressed image.
