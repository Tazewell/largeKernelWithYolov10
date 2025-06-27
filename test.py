from ultralytics import YOLOv10
import cv2
import time

# Load a pretrained YOLOv8n model
model = YOLOv10.from_pretrained('jameslahm/yolov10n')

# Define path to video file
# source = "/media/wmx/ws1/ai/dataSet/VID_20231217_110830.mp4"

# /dev/video0
source = 0

# Open the video file
cap = cv2.VideoCapture(source)

# Set the desired delay (in milliseconds) between frames
frame_delay = 33  # approximately 30 FPS

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Start time to calculate FPS
    start_time = time.time()

    # Run inference on the frame
    results = model(frame)

    # # Loop through the results and draw the bounding boxes
    # for r in results:
    #     for box in r.boxes:
    #         # Extract the coordinates of the bounding box
    #         x1, y1, x2, y2 = map(int, box.xyxy[0])
    #
    #         # Draw the bounding box on the frame
    #         # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    #
    #         # Extract class id and confidence
    #         class_id = int(box.cls[0])
    #         confidence = box.conf[0]
    #
    #         # Prepare the label with class name and confidence
    #         label = f"class_names{class_id} {confidence:.2f}"
    #
    #         # Draw the bounding box on the frame
    #         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    #
    #         # Draw the label above the bounding box
    #         cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
    #
    annotated_frame = results[0].plot()

    # Calculate FPS
    end_time = time.time()
    fps = 1 / (end_time - start_time)

    # Display FPS on the frame
    cv2.putText(annotated_frame, f'FPS: {fps:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the frame with the bounding boxes and FPS
    cv2.imshow('Detection', annotated_frame)

    # Introduce a delay to control playback speed
    if cv2.waitKey(frame_delay) & 0xFF == ord('q'):
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()

