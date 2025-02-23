import cv2
import numpy as np
from utils.image_processing import convert_to_gray

def test_convert_to_gray():
    # Create a dummy RGB image (3x3 pixels)
    rgb_image = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                          [[255, 255, 0], [0, 255, 255], [255, 0, 255]],
                          [[255, 255, 255], [128, 128, 128], [0, 0, 0]]], dtype=np.uint8)

    # Convert the dummy image to grayscale
    gray_image = convert_to_gray(rgb_image)

    # Check if the output is a 2D array
    assert len(gray_image.shape) == 2, "Output is not a grayscale image"

    # Check if the output has the same width and height as the input
    assert gray_image.shape[0] == rgb_image.shape[0] and gray_image.shape[1] == rgb_image.shape[1], "Output dimensions do not match input dimensions"

    print("All tests passed.")

if __name__ == "__main__":
    test_convert_to_gray()
