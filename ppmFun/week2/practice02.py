import ppmChanges
import filtering

#applying different kernels 
#basic, blur, sharpen, edge
kernel = [
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],    #size of kernel: 3x3
    [1/9, 1/9, 1/9]     # center is kernel[1][1]
]

blur = [
    [1/4, 1/4, 1/4],
    [1/4, 1/4, 1/4],
    [1/4, 1/4, 1/4]
]


sharpen = [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
]


edge = [
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
]



img, w, h = ppmChanges.read_ppm("practice01/practice01.ppm")

kernelFilter = filtering.apply_kernel(img, kernel)
ppmChanges.write_ppm("practice02/kernelfilter.ppm", kernelFilter, w, h)

blurred = filtering.apply_kernel(img, blur)
ppmChanges.write_ppm("practice02/blur.ppm", blurred, w, h)

sharpenned = filtering.apply_kernel(img, sharpen)
ppmChanges.write_ppm("practice02/sharpenned.ppm", sharpenned, w, h)

laplacian = filtering.apply_kernel(img, edge)
ppmChanges.write_ppm("practice02/laplacian.ppm", laplacian, w, h)