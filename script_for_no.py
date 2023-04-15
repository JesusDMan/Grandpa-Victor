import sys # to access the system
import cv2
img = cv2.imread("no.png", cv2.IMREAD_ANYCOLOR)
 

cv2.imshow("No", img)
cv2.waitKey(0)
