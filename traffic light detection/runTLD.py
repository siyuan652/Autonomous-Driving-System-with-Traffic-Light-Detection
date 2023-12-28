from ultralytics import YOLO
import cv2
import time


model = YOLO('traffic light detection\\models\\TLDv2.pt')

# results = model(source=0, show=True, conf=0.2, save=True, stream=True)  # generator of results

# Open the camera
cap = cv2.VideoCapture(0)

# Get the current timestamp
timestamp = int(time.time())

# Create a unique filename using the timestamp
filename = f'traffic light detection/result/results_{timestamp}.txt'

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success: 
        # Run YOLOv8 inference on the frame
        results = model(frame, conf=0.7)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Save the results to the file
        save = results[0].save_txt(filename, save_conf=True)

        array = results[0].numpy()
        
        print("this is the array", array)

        # Display the annotated frame
        cv2.imshow("Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()