import ppmChanges

img, w, h = ppmChanges.read_ppm("practice01/practice01.ppm")

#brighten
bright = ppmChanges.brightness(img, 50)
ppmChanges.write_ppm("practice01/bright.ppm", bright, w, h)

#darken
dark = ppmChanges.brightness(img, -100)
ppmChanges.write_ppm("practice01/darken.ppm", dark, w, h)


#contrast
contrast = ppmChanges.contrast(img, 1.5)
ppmChanges.write_ppm("practice01/contrast.ppm", contrast, w, h)


#threshold
thresh = ppmChanges.threshold_rgb(img, 128)
ppmChanges.write_ppm("practice01/threshold.ppm", thresh, w, h)

#negative
neg = ppmChanges.negative_rgb(img)
ppmChanges.write_ppm("practice01/negative.ppm", neg, w, h)


print(img[0][0])        # original
print(bright[0][0])     # after brightness
print(contrast[0][0])
print(thresh[0][0])
