image = [
    [[255, 0, 0], [0, 255, 0]],
    [[0, 0, 255], [255, 255, 255]]
]

height = len(image)
width = len(image[0])

with open("output.ppm", "w") as f:
    f.write("P3\n")
    f.write(f"{width} {height}\n")
    f.write("255\n")

    for row in image:
        for c in row:
            r, g, b = c
            f.write(f"{r} {g} {b}\n")