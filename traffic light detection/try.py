from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('traffic light detection\\models\\TLDv2.pt')

# Run inference on an image
results = model('C:\\Users\\ACER\\OneDrive\\Desktop\\demo images\\demo-img2.jpg')  

# Get the detections for the first image in the batch
detections = results[0]

# Print the class names of the detected objects
# Print the detections
# Get the boxes and names
for result in results:
    boxes = result.boxes  # Boxes object for bbox outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs

    #print the class value cls of object
    classVal=result.boxes.cls 
    print("class value:", classVal)

    classID=result.boxes.id 
    print("class ID:", classID)

# # Print the class names of the detected objects
# for detection in detections:
#     cls = detection[5].item()  # Get the class index
#     class_name = results.names[int(cls)]  # Get the class name
#     print(class_name)

# # Check if the 'probs' attribute is available
# if hasattr(results[0], 'probs'):
#     print("The model was trained with class probabilities.")
#     print("Class probabilities:", results[0].probs)
# else:
#     print("The model was not trained with class probabilities.")