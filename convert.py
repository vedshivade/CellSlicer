import os
from PIL import Image

def jpg_to_png(jpg_folder, png_folder):
    if not os.path.exists(png_folder):
        os.makedirs(png_folder)

    for filename in os.listdir(jpg_folder):
        if filename.endswith('.jpg'):
            img = Image.open(os.path.join(jpg_folder, filename))
            filename = filename[:-4] + '.png'
            img.save(os.path.join(png_folder, filename))

# Usage
jpg_to_png('/Users/vedshivade/Desktop/BBBC018', '/Users/vedshivade/Desktop/BBBC018')
