image = [
    [[255, 0, 0], [0, 255, 0]],
    [[0, 0, 255], [255, 255, 255]]
]

def read_ppm(filename):
    with open(filename, "r") as file:
        data = file.read().split()
        magic_num = data[0]
        w = int(data[1])
        h = int(data[2])
        max_value = int(data[3])
        pixels = [int(x) for x in data[4:]]
        
        rgb_pixels = []
        for i in range(0, len(pixels), 3):
            rgb_pixels.append([
                pixels[i],
                pixels[i+1],
                pixels[i+2]
            ])
    return rgb_pixels

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

img = read_ppm("practice.ppm")
print(img[0])


