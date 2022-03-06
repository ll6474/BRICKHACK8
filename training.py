import cv2
from os.path import exists


class Cartoonizer:
    """Cartoonizer effect
        A class that applies a cartoon effect to an image.
        The class uses a bilateral filter and adaptive thresholding to create
        a cartoon effect.
    """

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


tmp_canvas = Cartoonizer()

run = True
while run:
    file_name = input("Enter a filename or 'q' to quit: ")  # File_name will come here
    # print("Click any button for next image")
    file_exists = exists(file_name)
    if file_exists or file_name == 'q':
        if file_name == 'q':
            cv2.destroyAllWindows()
            run = False
        else:
            res = tmp_canvas.render(file_name)

            cv2.imwrite("Cartoon version.jpg", res)
            cv2.imshow("Cartoon version", res)
            wait_time = 500
            cv2.waitKey(wait_time)
            cv2.destroyAllWindows()
            while cv2.getWindowProperty('Cartoon version', cv2.WND_PROP_VISIBLE) >= 1:
                print(cv2.getWindowProperty("Cartoon version", res))
                cv2.destroyAllWindows()
    else:
        print("File does not exists, Enter another filename")
