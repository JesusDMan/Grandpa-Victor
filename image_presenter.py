import cv2
from sys import argv

if __name__ == '__main__':
    cv2.namedWindow(argv[1], cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(argv[1], cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    img = cv2.imread(argv[2], cv2.IMREAD_ANYCOLOR)
    cv2.imshow(argv[1], img)
    cv2.waitKey(0)
