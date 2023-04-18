import cv2
import sys

if __name__ == '__main__':
    cv2.namedWindow(sys.argv[1], cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(sys.argv[1], cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    img = cv2.imread(sys.argv[2], cv2.IMREAD_ANYCOLOR)
    cv2.imshow(sys.argv[1], img)
    cv2.waitKey(0)
