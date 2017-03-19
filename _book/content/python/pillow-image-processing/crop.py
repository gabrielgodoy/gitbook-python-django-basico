import os

# PIL Python Imaging Library
from PIL import Image

currentDirectory = os.path.dirname(__file__)
imagesPath = os.path.join(currentDirectory, 'images/')

# Convert image to a pillow object
img = Image.open(imagesPath + 'dino.jpg')

area = (100, 100, 300, 350)

cropped_image = img.crop(area) # Stores the cropped image in a variable

cropped_image.show() # Previews cropped image

