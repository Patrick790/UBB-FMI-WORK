from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes

from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from keras.preprocessing import image

from msrest.authentication import CognitiveServicesCredentials

import os
from PIL import Image
import sys
import matplotlib.pyplot as plt
import numpy as np

key = "7f85affc604048599fcf958914a04825"
endpoint = "https://lab3ardeleanpatrick.cognitiveservices.azure.com/"

client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))

im = plt.imread("images\\bike02.jpg")
fig, ax = plt.subplots()
im = ax.imshow(im, extent=[0, 300, 0, 300])
plt.show()

img = open("images\\bike02.jpg", "rb")
result = client.analyze_image_in_stream(img, visual_features=[VisualFeatureTypes.tags])

for tag in result.tags:
    print(tag)
    if (tag.name == "bicycle") or (tag.name == "bike"):
        print("Bicycle detected", tag.confidence)
print("objects")
if result.objects is not None:
    for ob in result.objects:
        print(ob.object_property, ob.rectangle)
else:
    print("No objects found in the image.")

im = plt.imread("images\\bike02.jpg")
fig = plt.imshow(im)
plt.show()

bike_bb = [17.0, 80.0, 363, 250]
im = plt.imread("images\\bike02.jpg")
fig = plt.imshow(im)
fig.axes.add_patch(
    plt.Rectangle((bike_bb[0], bike_bb[1]), bike_bb[2], bike_bb[3], linewidth=1, edgecolor='r', facecolor='none'))
plt.show()

img = open("images\\bike02.jpg", "rb")
result = client.analyze_image_in_stream(img, visual_features=[VisualFeatureTypes.objects])
for ob in result.objects:
    if ob.object_property == "bike":
        bike_bb = [ob.rectangle.x, ob.rectangle.y, ob.rectangle.w, ob.rectangle.h]

image_dir = "images"
output_dir = "output"

# Iterate over all images in the directory
for image_name in os.listdir(image_dir):
    image_path = os.path.join(image_dir, image_name)
    with open(image_path, "rb") as img:
        # Analyze the image
        result = client.analyze_image_in_stream(img, visual_features=[VisualFeatureTypes.objects])
        # Check if a bike is detected
        for ob in result.objects:
            if ob.object_property == "bike" or ob.object_property == "bicycle" or ob.object_property == "cycle" or ob.object_property == "wheel":
                # Load the image using matplotlib
                im = plt.imread(image_path)
                fig, ax = plt.subplots()
                ax.imshow(im)
                # Draw a rectangle around the bike
                bike_bb = [ob.rectangle.x, ob.rectangle.y, ob.rectangle.w, ob.rectangle.h]
                ax.add_patch(plt.Rectangle((bike_bb[0], bike_bb[1]), bike_bb[2], bike_bb[3], linewidth=1, edgecolor='r',
                                           facecolor='none'))
                # Save the image to the output directory
                output_path = os.path.join(output_dir, image_name)
                plt.savefig(output_path)
                plt.close(fig)

# 1

# Load the ResNet50 model
model = ResNet50(weights='imagenet')

# Directory containing the images
image_dir = "images"

# List to store all the predictions
predictions = []

# Iterate over all images in the directory
for image_name in os.listdir(image_dir):
    image_path = os.path.join(image_dir, image_name)
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Make a prediction
    preds = model.predict(x)
    # Decode the prediction
    decoded_preds = decode_predictions(preds, top=1)[0][0]
    # Check if the bike is detected
    if decoded_preds[1] == "bicycle" or decoded_preds[1] == "bike" or decoded_preds[1] == "cycle":
        predictions.append(1)
    else:
        predictions.append(0)

# True labels
true_labels = [0, 1, 1, 1, 1, 1]

# Calculate the performance of the model
accuracy = sum(np.array(predictions) == np.array(true_labels)) / len(true_labels)
print(f"Accuracy: {accuracy}")


# b

bike_bb2 = [54, 50, 302, 295]
im = plt.imread("images\\bike05.jpg")
fig = plt.imshow(im)
fig.axes.add_patch(
    plt.Rectangle((bike_bb2[0], bike_bb2[1]), bike_bb2[2], bike_bb2[3], linewidth=1, edgecolor='r', facecolor='none'))
plt.show()

bike_bb3 = [102, 880, 250, 180]
im = plt.imread("images\\binClass.png")
fig = plt.imshow(im)
fig.axes.add_patch(
    plt.Rectangle((bike_bb3[0], bike_bb3[1]), bike_bb3[2], bike_bb3[3], linewidth=1, edgecolor='r', facecolor='none'))
plt.show()
