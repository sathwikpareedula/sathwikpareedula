from PIL import Image
from io import BytesIO
import requests

def capture_image():
    # Assuming you have a camera accessible via a URL
    # Replace 'CAMERA_URL' with the actual URL of your camera
    camera_url = 'CAMERA_URL'

    # Capture the image from the camera
    response = requests.get(camera_url)
    image_data = BytesIO(response.content)

    # Open the image using Pillow
    image = Image.open(image_data)

    return image

if __name__ == "__main__":
    # Capture an image
    captured_image = capture_image()

    # Display the image
    captured_image.show()
