import ppmChanges
import filtering

img, w, h = ppmChanges.read_ppm_p6("croppedFrame.ppm")

blur = [
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
]


gray = ppmChanges.to_grayscale(img)
blurred = filtering.apply_kernel(gray, blur)



sobel_x = [
    [-1,0,1],
    [-2,0,2],
    [-1,0,1]
]

sobel_y = [
    [-1,-2,-1],
    [0,0,0],
    [1,2,1]
]

gx = filtering.apply_kernel(blurred, sobel_x)
gy = filtering.apply_kernel(blurred, sobel_y)

edges = filtering.combine_sobel(gx, gy)
binary = ppmChanges.threshold(edges, 100)

#pipeline as of now is gray -> blur -> sobel -> threshold
ppmChanges.write_ppm_p6("framegray.ppm", gray, w, h)
ppmChanges.write_ppm_p6("frameblur.ppm", blurred, w, h)
ppmChanges.write_ppm_p6("sobel.ppm", edges, w, h)
ppmChanges.write_ppm_p6("binary.ppm", binary, w, h)

