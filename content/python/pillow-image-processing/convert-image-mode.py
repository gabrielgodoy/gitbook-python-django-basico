import os

# PIL Python Imaging Library
from PIL import Image

# Built-in filters
from PIL import ImageFilter

currentDirectory = os.path.dirname(__file__)
imagesPath = os.path.join(currentDirectory, 'images/')

sunrise = Image.open(imagesPath + 'sunrise.jpg')

# Black and White Mode
# black_and_white = sunrise.convert('L')  # Luminescence
# black_and_white.show()  # black and white image

# Blurred image
blurred_sunrise = sunrise.filter(ImageFilter.BLUR)
# blurred_sunrise.show()

# Detail effect, makes image more crispy
edges_sunrise = sunrise.filter(ImageFilter.DETAIL)
edges_sunrise.show()

# Highlights the edges
edges_sunrise = sunrise.filter(ImageFilter.FIND_EDGES)
# edges_sunrise.show()
