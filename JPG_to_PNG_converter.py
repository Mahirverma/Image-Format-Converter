import sys
import os
from PIL import Image

# grab first and second argument from terminal

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if folder exists. If not, make a new folder

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through all images

for file in os.listdir(image_folder):
    image = Image.open(f'{image_folder}{file}')
    # seperate image name with the extension
    clean_name = os.path.splitext(file)[0]
    # convert images to png
    # save images to new folder
    image.save(f'{output_folder}{clean_name}.png', 'png')
    print(f"Image {clean_name} saved.")
