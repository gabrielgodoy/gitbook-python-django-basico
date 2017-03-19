import os

# PIL Python Imaging Library
from PIL import Image

currentDirectory = os.path.dirname(__file__)
imagesPath = os.path.join(currentDirectory, 'images/')

ball_img = Image.open(imagesPath + 'ball_200x200.jpg')
img1_r, img1_g, img1_b = ball_img.split()

tree_img = Image.open(imagesPath + 'tree_200x200.jpg')
img2_r, img2_g, img2_b = tree_img.split()

# To merge images must have the same size
new_img = Image.merge('RGB', (img1_r, img2_g, img1_b))

new_img.show()
