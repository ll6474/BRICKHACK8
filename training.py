import cv2
from os.path import exists


class Cartoonizer:
    """Cartoonizer effect
        A class that applies a cartoon effect to an image.
        The class uses a bilateral filter and adaptive thresholding to create
        a cartoon effect.
    """
    def __init__(self):
        pass

    def render(self, img_rgb):
        img_rgb = cv2.imread(img_rgb)
        numDownSamples = 1  # number of downscaling steps
        numBilateralFilters = 50 # number of bilateral filtering steps

        img_color = img_rgb
        for i in range(numDownSamples):
            img_color = cv2.pyrDown(img_color)

        for j in range(numBilateralFilters):
            img_color = cv2.bilateralFilter(img_color, 11, 11, 7)

        for k in range(numDownSamples):
            img_color = cv2.pyrUp(img_color)

        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        img_blur = cv2.medianBlur(img_gray, 3)

        img_edge = cv2.adaptiveThreshold(img_blur, 300,
                                         cv2.ADAPTIVE_THRESH_MEAN_C,
                                         cv2.THRESH_BINARY,5, 6)

        (x, y, z) = img_color.shape
        img_edge = cv2.resize(img_edge, (y, x))
        img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
        cv2.imwrite("edge.png", img_edge)
        return cv2.bitwise_and(img_color, img_edge)
