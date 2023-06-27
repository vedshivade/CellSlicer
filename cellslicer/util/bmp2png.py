from PIL import Image

# Open the BMP image
img = Image.open('sp.bmp')

# Save the image in PNG format
img.save('sp.png')
