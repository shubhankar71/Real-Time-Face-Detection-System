import cv2

# Load Haar Cascade Classifier

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open Webcam
cap = cv2.VideoCapture(0)  # 0 = default webcam
 
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("=" * 45)
print("   REAL-TIME FACE DETECTOR USING OPENCV")
print("=" * 45)
print("  Webcam started successfully!")
print("  Press 'Q' to quit the program.")
print("=" * 45)

# Real-Time Face Detection Loop
while True:

    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame.")
        break
    # Convert frame to grayscale (Haar Cascade works on grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,    # How much image size is reduced at each scale
        minNeighbors=5,     # How many neighbors each rectangle should have
        minSize=(30, 30)    # Minimum face size to detect
    )

    # Create a rectangle around each detected face
    for (x, y, w, h) in faces:
        # Draw green rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Add "Face" label above the rectangle
        cv2.putText(frame, "Face", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Show face count on screen
    face_count = len(faces)
    cv2.putText(frame, f"Faces Detected: {face_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Show the frame in a window
    cv2.imshow("Real-Time Face Detector", frame)

    # Press 'Q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("\nProgram Ended")
        break


cap.release()
cv2.destroyAllWindows()

