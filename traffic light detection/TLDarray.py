from ultralytics import YOLO
import cv2
import time


model = YOLO('traffic light detection\\models\\TLDv2.pt')

# Define path to the image file
source = 'C:\\Users\\ACER\\OneDrive\\Desktop\\demo images\\demo-img4.jpg'

    # Run YOLOv8 inference on the frame
    # results = model(source, conf=0.7)

# model.predict(source, show=True, classes=0)

# run inference
results = model(source)

# Get the boxes and names
for result in results:
    boxes = result.boxes  # Boxes object for bbox outputs
    # masks = result.masks  # Masks object for segmentation masks outputs
    # keypoints = result.keypoints  # Keypoints object for pose outputs
    # probs = result.probs  # Probs object for classification outputs

    #print the class value cls of object
    classVals=result.boxes.cls 
    for classVal in classVals:
        extractThis=int(classVal.item())
        print(extractThis)