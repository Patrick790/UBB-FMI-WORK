from PIL import ImageDraw
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from Levenshtein import distance as levenshtein_distance
from sklearn.metrics import jaccard_score
from sklearn.preprocessing import LabelBinarizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances, manhattan_distances, cosine_distances

from array import array
import os
from PIL import Image

import sys
import time

key = "7f85affc604048599fcf958914a04825"
endpoint = "https://lab3ardeleanpatrick.cognitiveservices.azure.com/"

client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))

img = open("ana.jpg", "rb")
read_response = client.read_in_stream(
    image=img,
    mode="Handwritten",
    raw=True
)

# Verifica starea unei operatiuni de citire
operation_id = read_response.headers["Operation-Location"].split("/")[-1]
while True:
    read_result = client.get_read_result(operation_id)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

# Print the detected text, line by line
result = []
if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            print(line.text)
            result.append(line.text)
print(result)

# get/define the ground truth
# groundTruth = ["Google Cloud", "Platform"]
# groundTruth = ["Succes in rezolvarea", "tEMELOR la", "LABORAtoarele de", "Inteligenta Artificiala!"]
groundTruth = ["Ana Are mere,", "pere si prune.", ""]

# compute the performance
noOfCorrectLines = sum(i == j for i, j in zip(result, groundTruth))
print(noOfCorrectLines)

# 1 a
# Calculez distanta Levenshtein la nivel caracter
levenshtein_distance_char = levenshtein_distance(' '.join(groundTruth), ' '.join(result))
print(f"Levenshtein distance at character level: {levenshtein_distance_char}")

# Calculez distanta Levenshtein la nivel de cuvant
levenshtein_distance_word = levenshtein_distance(groundTruth, result)
print(f"Levenshtein distance at word level: {levenshtein_distance_word}")

# 1 b
lb = LabelBinarizer()
lb.fit(groundTruth + result)
groundTruth_bin = lb.transform(groundTruth)
result_bin = lb.transform(result)

# Calculez distanta Jaccard la nivelul cuvant
jaccard_distance_word = 1 - jaccard_score(groundTruth_bin, result_bin, average='samples')
print(f"Jaccard distance at word level: {jaccard_distance_word}")

# Transform the word lists into feature vectors
vectorizer = CountVectorizer().fit_transform([' '.join(groundTruth), ' '.join(result)])
vectors = vectorizer.toarray()

# Distanta euclidiana
euclidean_distance = euclidean_distances(vectors[0].reshape(1, -1), vectors[1].reshape(1, -1))[0][0]
print(f"Euclidean distance: {euclidean_distance}")

# Distanta manhattan
manhattan_distance = manhattan_distances(vectors[0].reshape(1, -1), vectors[1].reshape(1, -1))[0][0]
print(f"Manhattan distance: {manhattan_distance}")

# Distanta cosinus
cosine_distance = cosine_distances(vectors[0].reshape(1, -1), vectors[1].reshape(1, -1))[0][0]
print(f"Cosine distance: {cosine_distance}")

# Print the detected text and its location, line by line
if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            print(f"Text: {line.text}")
            print(f"Location: {line.bounding_box}")

# Initialize the bounding box of the entire text
entire_text_box = [float('inf'), float('inf'), float('-inf'), float('-inf')]

# Update the bounding box with each line of text
if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            bounding_box = line.bounding_box
            entire_text_box[0] = min(entire_text_box[0], bounding_box[0])
            entire_text_box[1] = min(entire_text_box[1], bounding_box[1])
            entire_text_box[2] = max(entire_text_box[2], bounding_box[2])
            entire_text_box[3] = max(entire_text_box[3], bounding_box[3])

print(f"Location of the entire text: {entire_text_box}")

# Draw the bounding box on the image
img = Image.open("test2.jpeg")
draw = ImageDraw.Draw(img)
draw.rectangle(
    (
        (entire_text_box[0], entire_text_box[1]),  # top left corner
        (entire_text_box[2], entire_text_box[3])  # bottom right corner
    ),
    outline="red",  # color of the outline
    width=3  # width of the outline
)
img.save("test2_with_bbox.jpeg")


def calculate_iou(box1, box2):
    """
    Calculate the Intersection over Union (IoU) of two bounding boxes.

    Parameters:
    box1 -- first box, list object with coordinates (x1, y1, x2, y2)
    box2 -- second box, list object with coordinates (x1, y1, x2, y2)
    """

    # Determine the coordinates of the intersection rectangle
    x_left = max(box1[0], box2[0])
    y_top = max(box1[1], box2[1])
    x_right = min(box1[2], box2[2])
    y_bottom = min(box1[3], box2[3])

    # Compute the area of intersection rectangle
    intersection_area = max(0, x_right - x_left + 1) * max(0, y_bottom - y_top + 1)

    # Compute the area of both the prediction and ground-truth rectangles
    box1_area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
    box2_area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)

    # Compute the intersection over union by taking the intersection area and dividing it by the sum of prediction +
    # ground-truth areas - the intersection area
    iou = intersection_area / float(box1_area + box2_area - intersection_area)

    # Return the intersection over union value
    return iou


# Ground truth bounding box
ground_truth_box = [81.0, 314.0, 1450.0, 1151.0]

# Calculate IoU
iou_score = calculate_iou(entire_text_box, ground_truth_box)

print(f"IoU score: {iou_score}")
