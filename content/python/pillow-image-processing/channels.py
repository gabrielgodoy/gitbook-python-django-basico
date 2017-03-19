import os

# PIL Python Imaging Library
from PIL import Image

currentDirectory = os.path.dirname(__file__)
imagesPath = os.path.join(currentDirectory, 'images/')

# Convert image to a pillow object
balloons_img = Image.open(imagesPath + 'balloons.jpg')

# Separates the amount of red, green and blue on the image
r, g, b = balloons_img.split() # Split pillow object in different channels

# Displaying only the amount of green on the image
g.show()
