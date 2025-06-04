import cv2
import numpy as np
from ultralytics import YOLO

# First Load a YOLOv8 model (here small variant for speed, "yolov8s.pt")
model = YOLO("yolov8s.pt")  # or "yolov8n.pt" for nano variant or "yolov8l.pt" for large

# Open the default webcam and capture real-time video input
cap = cv2.VideoCapture(0)   #change '0' to '1' or '2' depending of your secondary camera devices

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Stop if camera feed fails
    # Inference: run YOLOv8 model on the frame
    results = model(frame)  # returns list of Results
    # Process detections in the first (and only) result
    for r in results:
        for box in r.boxes:  # iterating through the detected boxes
            x1, y1, x2, y2 = map(int, box.xyxy[0])     # bounding box coordinates
            conf = float(box.conf[0])                  # confidence score
            cls = int(box.cls[0])                      # class index
            label = model.names[cls]                   # class name (from COCO)
            
            # Drawing bounding box and labeling on the frame
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1-10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
            
            
    # Display the frame with detections
    cv2.imshow("Real-Time Detection", frame)
    if cv2.waitKey(1) == ord('q'):
        break  # press 'q' key to quit
cap.release()
cv2.destroyAllWindows()
