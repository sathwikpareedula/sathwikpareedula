pip install opencv-contrib-python
import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 represents the default camera, change if needed

# Capture a frame
ret, frame = cap.read()

# Release the camera
cap.release()

# Save the frame as an image
cv2.imwrite('captured_image.jpg', frame)

# Display a message
print("Image captured and saved as 'captured_image.jpg'")

# Optional: Display the captured image
cv2.imshow('Captured Image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
