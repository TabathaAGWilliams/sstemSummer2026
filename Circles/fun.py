import cv2
import numpy as np 
import matplotlib.pyplot as plt
import math

img = cv2.imread("luke.png")
img = cv2.resize(img, (400, 400))

cv2.imshow("My Image", img)
cv2.waitKey(0)

cv2.destroyAllWindows()