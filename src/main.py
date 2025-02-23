# File: /opencv-pipeline/opencv-pipeline/src/main.py

import cv2
from utils.image_processing import convert_to_gray

def main():
    # Load the RGB image
    image_path = 'path/to/your/image.jpg'  # Update with your image path
    rgb_image = cv2.imread(image_path)

    if rgb_image is None:
        print("Error: Could not load image.")
        return

    # Convert the image to grayscale
    gray_image = convert_to_gray(rgb_image)

    # Save or display the resulting image
    cv2.imwrite('path/to/save/gray_image.jpg', gray_image)  # Update with your save path
    cv2.imshow('Grayscale Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()