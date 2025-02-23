def convert_to_gray(image):
    import cv2
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)