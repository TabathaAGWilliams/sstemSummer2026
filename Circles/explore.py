import cv2
import numpy as np 
import matplotlib.pyplot as plt 

#image = cv2.imread("frame.jpeg")


# Define a tiny 2x2 image
width = 2
height = 10
max_val = 255

with open("colors.ppm", "w") as f:
   
    f.write("P3\n")              
    f.write(f"{width} {height}\n") 
    f.write(f"{max_val}\n")
    
    f.write("255 0 0    0 255 0\n")
    f.write("0 0 255    255 255 0\n")
    f.write("255 0 0    0 255 0\n")
    f.write("0 0 255    255 255 0\n")
    f.write("255 0 0    0 255 0\n")
    f.write("0 0 255    255 255 0\n")
    f.write("255 0 0    0 255 0\n")
    f.write("0 0 255    255 255 0\n")
    f.write("255 0 0    0 255 0\n")
    f.write("0 0 255    255 255 0\n")


img = cv2.imread("colors.ppm")


cv2.imshow("My Image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()