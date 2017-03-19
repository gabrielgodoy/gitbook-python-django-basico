import os

# PIL Python Imaging Library
from PIL import Image

currentDirectory = os.path.dirname(__file__)
imagesPath = os.path.join(currentDirectory, 'images/')

# Convert image to a pillow object
sunrise_img = Image.open(imagesPath + 'sunrise.jpg')
fossil_img = Image.open(imagesPath + 'fossil.jpg')

area = (0, 0, fossil_img.width, fossil_img.height)

sunrise_img.paste(fossil_img, area)

sunrise_img.show()
