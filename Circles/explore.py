import cv2
import numpy as np 
import matplotlib.pyplot as plt
import math

#image = cv2.imread("frame.jpeg")


# Define a tiny 2x2 image
width = 16
height = 16
max_val = 255

def fit(value):
    while value > 1:
        value -= 1
    while value < 0:
        value += 1
    return value

def background():
    with open("colors.ppm", "w") as f:

        f.write("P3\n")              
        f.write(f"{width} {height}\n") 
        f.write(f"{max_val}\n")

        for x in range(width):
            for y in range(height):
                r = (math.cos(math.sin(y) / height)) + float(y / height) * 10.0
                g = (math.sin(x*y))
                b = ((math.tan(x / width)) * 0.5) + math.atan(y * 2 + x * 10)

                r -= (x * y) / (width * height)
                
                r = fit(r)
                g = fit(g)
                b = fit(b)
                
                print(str(r) + " " + str(b) + " " + str(g) + "\n")
                f.write(str(int(255 * r)) + " " + str(int(255 * g)) + " " + str(int(255 * b)) + "\n")
    img = cv2.imread("colors.ppm")
    img = cv2.resize(img, (width * 32, height * 32))

    img = cv2.GaussianBlur(img, (15, 15), 0)
    img = cv2.GaussianBlur(img, (15, 15), 0)
    img = cv2.GaussianBlur(img, (15, 15), 0)
    img = cv2.GaussianBlur(img, (15, 15), 0)
    return img

def panel1():
    img = background()
    img = cv2.ellipse(img, (150, 100), (60, 90), 0, 0, 360, (255, 0, 0), 125)
    img = cv2.putText(img, "Its a me it,. Blue circle how are you?", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 0), 2)
    img = cv2.ellipse(img, (350, 325), (80, 45), 0, 0, 360, (0, 255, 0), 100)
    img = cv2.putText(img, "Hello im mr green circle I'm great", (225, 325), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    return img

def panel2():
    img = background()
    img = cv2.ellipse(img, (150, 100), (60, 90), 0, 0, 360, (255, 0, 0), 125)
    img = cv2.putText(img, "Mr green I have question", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 0), 2)
    img = cv2.ellipse(img, (350, 325), (80, 45), 0, 0, 360, (0, 255, 0), 100)
    img = cv2.putText(img, "yes mr. blue c ircle?", (225, 325), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    return img

def panel3():
    img = background()
    img = cv2.ellipse(img, (150, 100), (60, 90), 0, 0, 360, (255, 0, 0), 125)
    img = cv2.putText(img, "Why so fat?", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 0), 2)
    img = cv2.ellipse(img, (350, 325), (80, 45), 0, 0, 360, (0, 255, 0), 100)
    # img = cv2.putText(img, "yes mr. blue c ircle?", (225, 325), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    return img

def panel4():
    img = background()
    img = cv2.ellipse(img, (150, 100), (60, 90), 0, 0, 360, (255, 0, 0), 125)
    img = cv2.putText(img, "LOL!", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 0), 2)
    img = cv2.ellipse(img, (350, 325), (80, 45), 0, 0, 360, (0, 255, 0), 100)
    # img = cv2.putText(img, "yes mr. blue c ircle?", (225, 325), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    return img

def panel5():
    img = background()
    img = cv2.ellipse(img, (150, 100), (60, 90), 0, 0, 360, (255, 0, 0), 125)
    img = cv2.putText(img, "Wait. no mr green. whats that?", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 0), 2)
    img = cv2.ellipse(img, (350, 325), (80, 45), 0, 0, 360, (0, 255, 0), 100)
    img = cv2.rectangle(img, (200, 350), (275, 375), (0, 0, 0), -1)
    img = cv2.rectangle(img, (260, 350), (275, 400), (0, 0, 0), -1)
    return img

def panel6():
    img = background()
    img = cv2.ellipse(img, (150, 100), (60, 90), 0, 0, 360, (255, 0, 0), 125)
    img = cv2.putText(img, "Pleaes. I didn't mean it i swear!", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 0), 2)
    img = cv2.ellipse(img, (350, 325), (80, 45), 0, 0, 360, (0, 255, 0), 100)
    img = cv2.rectangle(img, (200, 350), (275, 375), (0, 0, 0), -1)
    img = cv2.rectangle(img, (260, 350), (275, 400), (0, 0, 0), -1)
    return img

def panel7():
    img = background()
    img = cv2.ellipse(img, (256, 256), (200, 200), 0, 0, 360, (0, 0, 255), -1)
    img = cv2.ellipse(img, (256, 256), (150, 150), 0, 0, 360, (0, 255, 255), -1)
    img = cv2.putText(img, "BANG!!!", (125, 250), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 255), 2)
    return img

def panel8():
    img = background()
    img = cv2.ellipse(img, (150, 100), (60, 90), 0, 0, 360, (160, 140, 140), 125)
    # img = cv2.putText(img, "Pleaes. I didn't mean it i swear!", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 0), 2)
    img = cv2.ellipse(img, (350, 325), (80, 45), 0, 0, 360, (0, 255, 0), 100)
    img = cv2.rectangle(img, (200, 350), (275, 375), (0, 0, 0), -1)
    img = cv2.rectangle(img, (260, 350), (275, 400), (0, 0, 0), -1)
    img = cv2.putText(img, "let this be a. Lesson", (225, 325), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    img = cv2.putText(img, "DONT mess with mr green!!", (225, 360), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    return img

def panel9():
    img = background()
    img = cv2.ellipse(img, (256, 256), (200, 200), 0, 0, 360, (255, 0, 0), -1)
    img = cv2.ellipse(img, (256, 256), (150, 150), 0, 0, 360, (255, 255, 0), -1)
    img = cv2.putText(img, "The. End", (125, 250), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 255), 2)
    return img

panels = [panel1, panel2, panel3, panel4, panel5, panel6, panel7, panel8, panel9]
panel_number = 0

while panel_number < len(panels):
    img = panels[panel_number]()
    cv2.imshow("My Image", img)
    cv2.waitKey(0)
    panel_number += 1

cv2.destroyAllWindows()