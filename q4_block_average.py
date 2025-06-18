# import required libraries
import cv2
import numpy as np

def block_average(image, block_size):
    h, w = image.shape[:2]
    
    # Calculate how much we need to trim from the edges
    new_h = h - (h % block_size)
    new_w = w - (w % block_size)
    
    # Crop the image to make dimensions divisible by block_size
    cropped = image[:new_h, :new_w]
    
    if len(image.shape) == 3:  # Color image
        # Reshape into blocks and average
        blocks = cropped.reshape(
            new_h//block_size, block_size,
            new_w//block_size, block_size,
            3
        )
        averaged = blocks.mean(axis=(1, 3)).astype(np.uint8)
        # Scale up to original block size
        result = np.repeat(np.repeat(averaged, block_size, axis=1), block_size, axis=0)
    else:  # Grayscale image
        blocks = cropped.reshape(
            new_h//block_size, block_size,
            new_w//block_size, block_size
        )
        averaged = blocks.mean(axis=(1, 3)).astype(np.uint8)
        result = np.repeat(np.repeat(averaged, block_size, axis=1), block_size, axis=0)
    
    return result

# Read image
image = cv2.imread('data/image.jpg')

# Process with different block sizes
block_sizes = [3, 5, 7]
processed_images = {size: block_average(image, size) for size in block_sizes}

# Display original image
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original Image', 640, 480)
cv2.imshow('Original Image', image)

# Display processed images
for size, img in processed_images.items():
    window_name = f'Processed {size}x{size} Blocks'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 640, 480)
    cv2.imshow(window_name, img)

cv2.waitKey(0)
cv2.destroyAllWindows()