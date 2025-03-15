import os
import cv2
import numpy as np
import pandas as pd


def imagini():
    def load_images_from_folder(folder):
        image_files = []
        labels = []
        for filename in os.listdir(folder):
            img_path = os.path.join(folder, filename)
            img = cv2.imread(img_path)
            if img is not None:
                image_files.append(img_path)
                # Determinam daca imaginea are sau nu efectul sepia
                if has_sepia_effect(img):
                    labels.append(1)
                else:
                    labels.append(0)
        return image_files, labels

    def has_sepia_effect(img):
        # Pentru a detecta efectul sepia, putem verifica valoarea medie a pixelilor din imagine
        # Daca valoarea medie a pixelilor este mai mare decat un anumit prag, consideram ca are efectul sepia
        # Acest prag trebuie sa fie determinat experimental
        threshold = 150
        avg_pixel_value = np.mean(img)
        return avg_pixel_value > threshold

    folder = 'images'

    # Incarcarea imaginilor si etichetarea lor
    image_files, labels = load_images_from_folder(folder)

    # Crearea unui DataFrame pentru gestionarea datelor
    data = {"Image_Path": image_files, "Labels": labels}
    df = pd.DataFrame(data)

    # Salvarea bazei de date intr-un fișier CSV
    df.to_csv("baza_de_date.csv", index=False)


imagini()
