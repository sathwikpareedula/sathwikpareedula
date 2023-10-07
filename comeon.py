import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 for the default camera, you can change it if you have multiple cameras

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Live Camera Feed', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
