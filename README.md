# Image-Compression-using-Python

There are several ways to perform image compression in Python, but one of the most common approaches is to use the Pillow library. Pillow is a fork of the Python Imaging Library (PIL), which provides a variety of image processing capabilities.

## Using PIL
In the above code, we first open the image file using the Image.open() method from Pillow. We then use the save() method to save the image in a compressed format by specifying the optimize and quality parameters. The optimize parameter tells Pillow to optimize the Huffman coding used in the JPEG format, while the quality parameter controls the amount of compression applied to the image.

You can experiment with different values of the quality parameter to achieve the desired level of compression. However, keep in mind that reducing the quality too much can result in a loss of detail and visual artifacts in the compressed image.

# Using OpenCV
In the above code, we first load the image using the cv2.imread() method from OpenCV. We then use the cv2.imwrite() method to save the compressed image in JPEG format by specifying the cv2.IMWRITE_JPEG_QUALITY flag with a value of 50. This value controls the amount of compression applied to the image, with higher values resulting in less compression and better image quality.

You can experiment with different values of the compression quality to achieve the desired level of compression. However, keep in mind that reducing the quality too much can result in a loss of detail and visual artifacts in the compressed image.

There are several other Python libraries that support image compression. Here are a few examples:

scikit-image: scikit-image is an image processing library that provides a range of algorithms for image compression. It includes functions for lossless compression using the Lempel-Ziv-Welch (LZW) algorithm, as well as lossy compression using the Discrete Cosine Transform (DCT) and other techniques.

imageio: imageio is a library for reading and writing a wide range of image formats, including compressed formats like JPEG, PNG, and GIF. It provides a simple interface for compressing and decompressing images using various codecs.

PyWavelets: PyWavelets is a library for wavelet transforms and signal processing. It includes functions for image compression using wavelet-based methods like the discrete wavelet transform (DWT) and the lifting scheme.

tensorflow-io: tensorflow-io is a library for loading and processing various file formats including images. It provides several image compression options for JPEG, PNG, and WebP image formats.

Pillow-SIMD: Pillow-SIMD is a drop-in replacement for the Pillow library that uses SIMD (Single Instruction Multiple Data) instructions to accelerate image processing tasks, including image compression.

All of these libraries offer different compression techniques and features. You can choose the one that best suits your needs based on your specific use case.

# Using Tensorflow
This czn be achieved using autoencoders by training the auto encoder as an image compression filter.
