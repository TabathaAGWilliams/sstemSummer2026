import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import math

#image = cv2.imread("frame.jpeg")



# width = 70
# height = 70
# max_val = 255
# with open("tabName.pgm", "w") as f:
#     f.write("P2\n")
#     f.write(f"{width} {height}\n")
#     f.write(f"{max_val}\n")

#     #background is white
#     r = 255
#     g = 255
#     b = 255
# with open("colors.ppm", "w") as f:
   
#     f.write("P3\n")              
#     f.write(f"{width} {height}\n") 
#     f.write(f"{max_val}\n")

#     for i in range(height):
#         for j in range(width):
#             # if i >= 2 and i <=6 and j >=2 and j <=6:
#             #     r = 0
#             #     g = 200
#             #     b = 0
#             # else:
#             #     r = 100
#             #     g = 0 
#             #     b = 150
#             r = 135
#             g = 206
#             b = 230

#             f.write(f"{r} {g} {b}\n")
    


img = cv2.imread("tabName.pgm")
#FUN FACT: THE CIRCLE METHOD, THE COLOR PARAMETER IS BGR!!!!!! NOT RGB
#cv2.circle(img, (7,7), 1, color=(224, 254, 255), thickness=-1)
#img = cv2.resize(img, (500, 500), interpolation=cv2.INTER_NEAREST)
#img=cv2.circle(img, (50,50), 35, color=(224, 254, 255), thickness=-1)
cv2.imshow("My Image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()