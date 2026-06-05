import cv2
import numpy as np 
import matplotlib.pyplot as plt
import math

#image = cv2.imread("frame.jpeg")


# Define a tiny 2x2 image
width = 100
height = 75

def fit(value):
    while value > 1:
        value -= 1
    while value < 0:
        value += 1
    return value


room = [
    [1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [1, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 2, 0, 0, 2, 0, 1, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 2, 0, 0, 2, 0, 1, 3, 0, 0, 2, 0, 3, 3, 3, 3, 3],
    [1, 0, 0, 0, 0, 0, 0, 1, 3, 0, 2, 2, 2, 3, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 2, 2, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0],
]

player = [4.0, 4.0]
FOV = 90
look_angle = 0

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600



canvas = np.zeros((height, width, 3), dtype=np.uint8)

def in_block(pos):
    return room[int(pos[1])][int(pos[0])] != 0

def get_block(pos):
    return room[int(pos[1])][int(pos[0])]

def out_of_range(pos):
    return (
        pos[0] < 0 or pos[1] < 0 or
        pos[0] >= len(room[0]) or
        pos[1] >= len(room)
    )

def frame():
    h, w = canvas.shape[:2]
    canvas[:] = 0

    for x in range(w):
        ray_pos = player.copy()
        theta = ((float(x) / w) - 0.5) * math.radians(FOV)
        theta += look_angle
        ray_dir = [math.cos(theta), math.sin(theta)]

        dist = -1.0
        inc = 0.1
        wall = 0

        while True:
            ray_pos[0] += ray_dir[0] * inc
            ray_pos[1] += ray_dir[1] * inc
            if out_of_range(ray_pos):
                break
            if in_block(ray_pos):
                dist = math.dist(player, ray_pos)
                wall = get_block(ray_pos)
                break

        for y in range(h):
            if dist == -1:
                canvas[y, x] = (0, 0, 0)
            else:
                wall_height = 1.0 / max(dist, 0.001)
                wall_top = 0.5 - wall_height * 0.5
                wall_bot = 0.5 + wall_height * 0.5
                normal = float(y) / h

                if wall_top <= normal <= wall_bot:
                    canvas[y, x] = wall_color(wall, min(wall_height, 1.0))

def wall_color(wall, intensity = 1.0):
    color = [255, 0, 0]
    if wall == 1:
        color = [255, 0, 0]
    elif wall == 2:
        color = [0, 0, 255]
    elif wall == 3:
        color = [0, 255, 0]
    else:
        color = [0, 0, 0]
    color[0] *= intensity
    color[1] *= intensity
    color[2] *= intensity
    return color


def write_frame():
    # image = np.zeros((height, width, 3), dtype=np.uint8)
    # with open("colors.ppm", "w") as f:

    #     # f.write("P3\n")              
    #     # f.write(f"{width} {height}\n") 
    #     # f.write(f"{255}\n")

    #     for y in range(height):
    #         for x in range(width):
    #             cv2.rectangle(image, (x, y), (x, y), canvas[y][x], 1)
                # f.write(str(int(screen[y][x][0])) + " " + str(int(screen[y][x][1])) + " " + str(int(screen[y][x][2])) + "\n")
    # img = cv2.imread("colors.ppm")  

    return canvas

while True:
    frame()
    img = write_frame()
    img = cv2.resize(img, (WINDOW_WIDTH, WINDOW_HEIGHT))
    cv2.imshow("My Image", img)
    
    move_dir = [math.cos(look_angle), math.sin(look_angle)]
    right_dir = [-math.sin(look_angle), math.cos(look_angle)]
    move_speed = 0.25

    key = cv2.waitKeyEx(16);
    if key == ord('w'):
        player[0] += move_dir[0] * move_speed
        player[1] += move_dir[1] * move_speed
    if key == ord('s'):
        player[0] -= move_dir[0] * move_speed
        player[1] -= move_dir[1] * move_speed
    if key == ord('d'):
        player[0] += right_dir[0] * move_speed
        player[1] += right_dir[1] * move_speed
    if key == ord('a'):
        player[0] -= right_dir[0] * move_speed
        player[1] -= right_dir[1] * move_speed

    
    if key == 2424832:
        look_angle -= 0.1
    elif key == 2555904:
        look_angle += 0.1

cv2.destroyAllWindows()
