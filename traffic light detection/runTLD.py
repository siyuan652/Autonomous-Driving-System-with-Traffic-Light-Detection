from ultralytics import YOLO
import cv2

model = YOLO('traffic light detection\\models\\TLDv2.pt')

# results = model(source=0, show=True, conf=0.2, save=True, stream=True)  # generator of results

# Open the camera
cap = cv2.VideoCapture(0)

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
        save = results[0].save_txt('results.txt')

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