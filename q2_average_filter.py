# import required libraries
import cv2
import numpy as np

# Read the image
image = cv2.imread('data/image.jpg')

# Define initial variables
image_windows = 'Original Image', '3x3 Average', '10x10 Average', '20x20 Average'
for window in image_windows:
    cv2.namedWindow(window, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window, 640, 480)
processed_image = np.copy(image)

# Define function for 3x3 spatial averaging
def average_3x3():
    global processed_image
    processed_image = cv2.blur(image, (3, 3))
    cv2.imshow(image_windows[1], processed_image)

# Define function for 10x10 spatial averaging
def average_10x10():
    global processed_image
    processed_image = cv2.blur(image, (10, 10))
    cv2.imshow(image_windows[2], processed_image)

# Define function for 20x20 spatial averaging
def average_20x20():
    global processed_image
    processed_image = cv2.blur(image, (20, 20))
    cv2.imshow(image_windows[3], processed_image)

# Display the images
cv2.imshow(image_windows[0], image)
average_3x3()
average_10x10()
average_20x20()

cv2.waitKey(0)
cv2.destroyAllWindows()