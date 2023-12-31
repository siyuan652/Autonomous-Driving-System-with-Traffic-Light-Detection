from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('traffic light detection\\models\\TLDv2.pt')

# Run inference on an image
results = model('C:\\Users\\ACER\\OneDrive\\Desktop\\demo images\\demo-img2.jpg')  

# Get the detections for the first image in the batch
detections = results[0]

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