import requests

class PlateReaderClient:
    def __init__(self, host):
        self.host = host

    def read_number(self, image_id):
        print(f'Reading single number for image id: {image_id}')
        response = requests.get(f'{self.host}/read-number?id={image_id}')
        return response.json()

    def read_multiple_numbers(self, image_id_list):
        print("Reading several numbers...")
        response = requests.get(f'{self.host}/read-several-numbers', params={'id': image_id_list})
        return response.json()

if __name__ == "__main__":
    plate_reader_client = PlateReaderClient('http://0.0.0.0:8080')

    print("Testing reading single number:")
    valid_ids = [10022, 9965]
    for img_id in valid_ids:
        print(f"Image ID: {img_id}, Result: {plate_reader_client.read_number(img_id)}")

    print("Testing reading multiple numbers:")
    print(f"Image IDs: {valid_ids}, Result: {plate_reader_client.read_multiple_numbers(valid_ids)}")
