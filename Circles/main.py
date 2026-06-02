import cv2
import numpy as np

image = cv2.imread("frame.jpeg")

if image is None:
    print("Could not load image.")
    exit()

image = cv2.resize(image, (1200, 900))


# Count
cv2.imshow("Original", image)


cv2.waitKey(0)
cv2.destroyAllWindows()