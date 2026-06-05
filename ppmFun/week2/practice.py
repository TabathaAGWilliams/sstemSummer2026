import ppmChanges

#using the practice ppm:
#   read the image
#   use methods to brighten, darken, create contrast, and apply a threshold
#   write that to a new ppm file
img, w, h = ppmChanges.read_ppm("practice/practice.ppm")

#brighten
bright = ppmChanges.brightness(img, 50)
ppmChanges.write_ppm("practice/bright.ppm", bright, w, h)

#darken
dark = ppmChanges.brightness(img, -100)
ppmChanges.write_ppm("practice/darken.ppm", dark, w, h)


#contrast
contrast = ppmChanges.contrast(img, 1.5)
ppmChanges.write_ppm("practice/contrast.ppm", contrast, w, h)


#threshold
thresh = ppmChanges.threshold_rgb(img, 128)
ppmChanges.write_ppm("practice/threshold.ppm", thresh, w, h)

#negative
neg = ppmChanges.negative_rgb(img)
ppmChanges.write_ppm("practice/negative.ppm", neg, w, h)


print(img[0][0])        # original
print(bright[0][0])     # after brightness
print(contrast[0][0])
print(thresh[0][0])
