from PIL import Image
import os

dataset_dir = "Indian_Currency_Dataset"

increment = 0
for root, dirs, files in os.walk(dataset_dir):
    for file in files:
        path = os.path.join(root, file)

        try:
            with Image.open(path) as img:
                img = img.convert("RGB")
                img.save(path)
                if increment % 10 == 0:
                    print(increment)
                increment += 1
        except Exception as e:
            print("Removing bad file:", path, e)
            # os.remove(path)