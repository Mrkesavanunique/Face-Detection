# Face-Detection
import cv2
import numpy as np
import os

# Set correct paths for the TensorFlow model and config
model_path = "C:/Users/kesav/Downloads/opencv_face_detector_uint8.pb"
config_path = "C:/Users/kesav/Downloads/2opencv_face_detector.pbtxt"

# Check if model files exist
if not os.path.exists(model_path) or not os.path.exists(config_path):
    print("Error: Model files not found. Please make sure the following files are in the same directory as the script:")
    print("- opencv_face_detector_uint8.pb")
    print("- opencv_face_detector.pbtxt")
    exit()

# Load the DNN model
net = cv2.dnn.readNetFromTensorflow(model_path, config_path)

def detect_faces_dnn(image):
    """Detects faces using DNN and displays face count."""
    h, w = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(300, 300), mean=(104, 117, 123), swapRB=True)
    net.setInput(blob)
    detections = net.forward()

    face_count = 0
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:  # Confidence threshold
            face_count += 1
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x, y, x1, y1) = box.astype("int")

            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 3)
            cv2.putText(image, f"{confidence*100:.2f}%", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.putText(image, f"Faces: {face_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return image

def process_image(image_path):
    """Loads an image and detects faces."""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return

    image = detect_faces_dnn(image)
    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def process_webcam():
    """Detects faces in real-time using a webcam and shows the count."""
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot access webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to read frame from webcam.")
            break

        frame = detect_faces_dnn(frame)
        cv2.imshow("Face Detection (Press 'Q' to Exit)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    mode = input("Choose mode - (1) Image (2) Webcam: ")
    if mode == "1":
        image_path = input("Enter image path: ")
        process_image(image_path)
    elif mode == "2":
        process_webcam()
    else:
        print("Invalid choice!")
