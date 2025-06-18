# import required libraries
import cv2
import numpy as np

# Read the original image
image = cv2.imread('data/image.jpg')

# Function to rotate image without cropping
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    # Calculate new bounding dimensions
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))
    
    # Adjust the rotation matrix
    M[0, 2] += (new_w / 2) - center[0]
    M[1, 2] += (new_h / 2) - center[1]
    
    return cv2.warpAffine(image, M, (new_w, new_h))

# Rotate images
rotated_45 = rotate_image(image, 45)
rotated_90 = rotate_image(image, 90)

# Create windows with fixed size
windows = [
    ('Original Image', image),
    ('Rotated 45 Degrees', rotated_45),
    ('Rotated 90 Degrees', rotated_90)
]

for name, img in windows:
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 640, 480)  # Fixed size as in your original code
    cv2.imshow(name, img)

cv2.waitKey(0)
cv2.destroyAllWindows()