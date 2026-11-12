import os
import numpy as np
import pandas as pd
from PIL import Image

dataset_path = r"E:\Dataset"

fruits = {
    "apples": 0,
    "avocados": 1,
    "bananas": 2,
    "grapes": 3,
    "guava": 4
}

image_size = (128, 128)
num_pixels = image_size[0] * image_size[1] * 3
columns = [f"pixel_{i}" for i in range(num_pixels)] + ["label"]

csv_filename = "fruits227.csv"

if os.path.exists(csv_filename):
    os.remove(csv_filename)

total_saved = 0

for fruit_name in os.listdir(dataset_path):
    fruit_folder = os.path.join(dataset_path, fruit_name)

    if not os.path.isdir(fruit_folder):
        continue

    print(f"Processing folder: {fruit_name}...")
    batch_data = []

    for img_file in os.listdir(fruit_folder):
        img_path = os.path.join(fruit_folder, img_file)

        try:
            img = Image.open(img_path).convert('RGB')
            img = img.resize(image_size)
            img_array = np.array(img)
            flattened = img_array.flatten()

            row = list(flattened) + [fruits[fruit_name]]
            batch_data.append(row)

            if len(batch_data) >= 100:
                df_batch = pd.DataFrame(batch_data, columns=columns)
                df_batch.to_csv(csv_filename, mode='a', header=not os.path.exists(csv_filename), index=False)
                total_saved += len(batch_data)
                batch_data = []  # RAM clear
        except Exception as e:
            print(f"Skip {img_path}: {e}")

    if len(batch_data) > 0:
        df_batch = pd.DataFrame(batch_data, columns=columns)
        df_batch.to_csv(csv_filename, mode='a', header=not os.path.exists(csv_filename), index=False)
        total_saved += len(batch_data)

print(f"CSV File Done! Total safely saved images: {total_saved}")