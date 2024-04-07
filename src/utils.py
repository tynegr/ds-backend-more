from io import BytesIO
import requests
from PIL import Image, UnidentifiedImageError

def read_number_by_id(model, image_id):
    try:
        image_url = f"http://51.250.83.169:7878/images/{image_id}"
        response = requests.get(image_url)
    except ConnectionError:
        return {'error': 'failed to fetch image'}, 500

    try:
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        gov_number = model.read_text(image)
    except UnidentifiedImageError:
        return {'error': 'invalid image format'}, 400

    return {image_id: gov_number}, 200
