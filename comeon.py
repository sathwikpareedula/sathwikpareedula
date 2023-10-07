from PIL import Image
from io import BytesIO
import requests

def capture_image():
    camera_url = 'YOUR_CAMERA_URL'  # Replace with the actual camera URL

    try:
        response = requests.get(camera_url)
        response.raise_for_status()  # Raise an error for bad responses (e.g., 404, 500)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")
        return None

    image_data = BytesIO(response.content)
    image = Image.open(image_data)

    return image

if __name__ == "__main__":
    captured_image = capture_image()

    if captured_image:
        captured_image.show()
