# File: /opencv-pipeline/opencv-pipeline/src/main.py

import cv2
from utils.image_processing import convert_to_gray
import os

def main():
    # Load the RGB image
    image_path = 'data/tiger.jpg'  # Updated with your image path
    rgb_image = cv2.imread(image_path)

    if rgb_image is None:
        print("Error: Could not load image.")
        return

    # Convert the image to grayscale
    gray_image = convert_to_gray(rgb_image)

    # Save or display the resulting image
    # Create output directory if it does not exist
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the grayscale image to the output directory
    output_path = os.path.join(output_dir, 'gray_tiger.jpg')
    cv2.imwrite(output_path, gray_image)
    print(f"Grayscale image saved to {output_path}")

if __name__ == "__main__":
    main()