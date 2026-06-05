import cv2
width = 30
height = 30
max_val = 255

def create_pgm(filename, height, width): 
    with open(filename, 'w') as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write(f"{max_val}\n")

        for i in range(height):
            for j in range(width):
                while i >= 10 and i <=20:
                    if j == 5:
                        f.write(f"0\n")
                f.write(f"255\n")

create_pgm("tabName.pgm", 300, 300)



img = cv2.imread("tabName.pgm")

cv2.imshow("My Image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()