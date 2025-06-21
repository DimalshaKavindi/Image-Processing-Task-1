# import required libraries
import cv2
import numpy as np
import os

os.makedirs('results', exist_ok=True)

# Read the image
image = cv2.imread('data/image.jpg', cv2.IMREAD_GRAYSCALE)

# Define a window to display the image
window_name = 'Intensity Level Reduction'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 640, 480)

def update_intensity(value):
    # Calculate number of intensity levels (2^value)
    levels = 2 ** value
    # Calculate step size
    step = 256 / levels
    # Quantize the image
    img_reduced = np.floor(image / step) * step
    # Convert back to uint8
    img_reduced = np.uint8(img_reduced)
    cv2.imshow(window_name, img_reduced)
    # Save image when spacebar is pressed
    if cv2.waitKey(1) == 32:  # 32 is spacebar
        cv2.imwrite(f'results/intensity_levels_{levels}.jpg', img_reduced)

# Create trackbar (values 1-8 representing 2^1 to 2^8 levels)
cv2.createTrackbar('Levels', window_name, 8, 8, update_intensity)

# Display initial image (256 levels)
update_intensity(8)

cv2.waitKey(0)
cv2.destroyAllWindows()