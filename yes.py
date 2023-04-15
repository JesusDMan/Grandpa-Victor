import sys # to access the system
import cv2
img = cv2.imread("yes.png", cv2.IMREAD_ANYCOLOR)
 

cv2.imshow("Yes", img)
cv2.waitKey(0)
