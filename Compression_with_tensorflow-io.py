import tensorflow_io as tfio
import tensorflow as tf

# Load the image
img = tf.io.read_file('image.jpg')
img = tf.image.decode_jpeg(img, channels=3)

# Compress the image using JPEG
compressed_img = tfio.image.encode_jpeg(img, quality=50)

# Save the compressed image
tf.io.write_file('compressed.jpg', compressed_img)
