import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 represents the default camera, if you have multiple, it might be 1, 2, etc.

while True:
    # Capture a frame
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Camera Feed', frame)

    # Check for user input to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()

