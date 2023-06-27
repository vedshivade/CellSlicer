import cv2
import numpy as np

# Load the image and the binary mask
image = cv2.imread('sp.png')
binary_mask = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)

# Generate the edge map from the binary mask
edges = cv2.Canny(binary_mask, 30, 100)

# Find contours in the edge map
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the image
cv2.drawContours(image, contours, -1, (0, 0, 255), 3) # Red color in BGR

# Save the output
cv2.imwrite('vis.png', image)
