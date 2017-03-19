import os

# PIL Python Imaging Library
from PIL import Image

currentDirectory = os.path.dirname(__file__)
imagesPath = os.path.join(currentDirectory, 'images/')

# Convert image to a pillow object
img = Image.open(imagesPath + 'dino.jpg')

print(img.size)  # A tuple with dimensions (636, 431)
print(img.format)  # JPEG

# Creates temporary image from the pillow object to show
img.show()  # Opens preview of image in whatever program is set to open images
