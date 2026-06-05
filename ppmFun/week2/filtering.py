import ppmChanges

kernel = [
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],    #size of kernel: 3x3
    [1/9, 1/9, 1/9]     # center is kernel[1][1]
]

def apply_kernel(image, kernel):
    height = len(image)
    width = len(image[0])

    k_size = len(kernel)
    offset = k_size // 2

    output = [[[0,0,0] for _ in range(width)] for _ in range(height)]

    for row in range(offset, height - offset):
            for col in range(offset, width - offset):
                sum_r = 0
                sum_g = 0
                sum_b = 0
    
                for i in range(k_size):
                    for j in range(k_size):
                        r, g, b = image[row + i - offset][col + j - offset]
                        weight = kernel[i][j]

                        sum_r += r * weight
                        sum_g += g * weight
                        sum_b += b * weight

                output[row][col] = [
                    ppmChanges.clip(int(sum_r)),
                    ppmChanges.clip(int(sum_g)),
                    ppmChanges.clip(int(sum_b))
                ]
    return output
