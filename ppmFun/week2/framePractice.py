import ppmChanges
import filtering

img, w, h = ppmChanges.read_ppm_p6("croppedFrame.ppm")

blur = [
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
]

blurred_img = filtering.apply_kernel(img, blur)
ppmChanges.write_ppm_p6("frameblur.ppm", blurred_img, w, h)