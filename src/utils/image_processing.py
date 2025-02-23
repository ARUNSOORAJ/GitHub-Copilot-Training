def convert_to_gray(image):
    """
    Convert an RGB image to grayscale.

    Args:
        image (numpy.ndarray): The input RGB image.

    Returns:
        numpy.ndarray: The converted grayscale image.
    """
    import cv2
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)