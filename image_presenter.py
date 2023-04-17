import cv2
import sys

if __name__ == '__main__':
    img = cv2.imread(sys.argv[2], cv2.IMREAD_ANYCOLOR)
    cv2.imshow(sys.argv[1], img)
    cv2.waitKey(0)
