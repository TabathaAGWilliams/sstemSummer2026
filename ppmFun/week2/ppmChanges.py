#function read_ppm takes a file name
#   reads the data into a 2d array and outputs the array, width and height
#   @param filename is the input file name
def read_ppm(filename):
    with open(filename, "r") as file:
        data = file.read().split()
    magic_num = data[0]
    w = int(data[1])
    h = int(data[2])
    max_value = int(data[3])
    pixels = [int(x) for x in data[4:]]
        
    img = []
    index = 0
    for row in range(h):
        curr_row = []

        for col in range(w):

            curr_row.append([
            pixels[index],
            pixels[index+1],
            pixels[index+2]
            ])
            index += 3
            
        img.append(curr_row)
    return img, w, h

# function read_ppm_p6 works for p6 files
def read_ppm_p6(filename):
    with open(filename, "rb") as f:
        magic = f.readline().strip()

        if magic != b'P6':
            raise ValueError("Not a P6 file")

        line = f.readline()
        while line.startswith(b'#'):
            line = f.readline()

        parts = line.split()
        w = int(parts[0])
        h = int(parts[1])
        max_val = int(f.readline())
        pixel_data = f.read()
    img = []
    index = 0

    for row in range(h):
        curr_row = []
        for col in range(w):
            r = pixel_data[index]
            g = pixel_data[index + 1]
            b = pixel_data[index + 2]

            curr_row.append([r, g, b])
            index += 3
        img.append(curr_row)

    return img, w, h


#function write_ppm creates a new ppm file
#   @param filename is the output file name
#   @param img is the array to read
#   @param w is the number of columns
#   @param h is the number of rows 
def write_ppm(filename, img, w, h):
    with open(filename, "w") as f:
        f.write("P3\n")
        f.write(f"{w} {h}\n")
        f.write("255\n")

        for row in range(h):
            for col in range(w):
                r, g, b = img[row][col]
                f.write(f"{r} {g} {b}\n")



# func write_ppm_p6 will output p6
def write_ppm_p6(filename, img, w, h):
    with open(filename, "wb") as f:
        f.write(b"P6\n")
        f.write(f"{w} {h}\n".encode())
        f.write(b"255\n")

        for row in range(h):
            for col in range(w):
                r, g, b = img[row][col]
                f.write(bytes([r, g, b]))



# func clip is a validation method 
#   ensures that values do not go out of bounds
#   @param val is the value being validated
def clip(val):
    if val < 0:
        return 0
    elif val > 255:
        return 255
    return val


# func negative_rgb returns a negative image of input
#   @param image is the input array
def negative_rgb(image):
    height = len(image)
    width = len(image[0])

    output = [[0] * width for _ in range(height)]

    for row in range(height):
        for col in range(width):
            r, g, b = image[row][col]
            output[row][col] = [255 - r, 255 - g, 255 - b]

    return output


# func brightness works to increase or decrease the brightness by an int value
#   @param image is the array to work with
#   @param k is the value to brighten by 
def brightness(image, k):
    #formula: s = r + k where k > 0 (brighter) k < 0 (darker)

    height = len(image)
    width = len(image[0])
    
    output = [[[0,0,0] for _ in range(width)] for _ in range(height)]

    for row in range(height):
        for col in range(width):
            r, g, b = image[row][col]

            r = clip(r + k)
            g = clip(g + k)
            b = clip(b + k)

            output[row][col] = [r, g, b]

    return output



# func contrast scales the contrast level up or down
#   @param image is the input array
#   @param a is the scalar for contrast 
def contrast(image, a):
    #formula: s = a * r where a>1 -> increase contrast and 0 < a < 1 -> decrease contrast

    height = len(image)
    width = len(image[0])

    output = [[[0,0,0] for _ in range(width)] for _ in range(height)]

    for row in range(height):
        for col in range(width):
            r, g, b = image[row][col]

            r = clip(a * r)
            g = clip(a * g)
            b = clip(a * b)

            output[row][col] = [r, g, b]

    return output


# func threshold_rgb works to apply a threshold to the image
#   works by converting rgb to grayscale and then applying the threshold
#   @param image is the input array
#   @param T is the threshold level 
def threshold_rgb(image, T):
    #convert to gray = 0.299R + 0.587G + 0.114B
    #formula for threshold: s = 255 if gray >= T else 0
    height = len(image)

    width = len(image[0])

    output = [[[0,0,0] for _ in range(width)] for _ in range(height)]

    for row in range(height):
        for col in range(width):
            r, g, b = image[row][col]

            gray = int(0.299*r + 0.587*g + 0.114*b)

            if gray >= T:
                val = 255
            else:
                val = 0

            output[row][col] = [val, val, val]

    return output



def crop(image, row_start, row_end, col_start, col_end):
    cropped = []

    for row in range(row_start, row_end):
        curr_row = []

        for col in range(col_start, col_end):
            curr_row.append(image[row][col])

        cropped.append(curr_row)

    return cropped





