import os

# PIL Python Imaging Library
from PIL import Image

currentDirectory = os.path.dirname(__file__)
imagesPath = os.path.join(currentDirectory, 'images/')

# Create pillow instance based on the fossil image
fossil = Image.open(imagesPath + 'fossil.jpg')
square_fossil_image =  fossil.resize((100, 100))
# square_fossil_image.show()

# Flips image vertically
flipped_fossil_image = fossil.transpose(Image.FLIP_TOP_BOTTOM)
# flipped_fossil_image.show()

# Rotate Fossil
rotated_fossil_image = fossil.transpose(Image.ROTATE_90)
rotated_fossil_image.show()
