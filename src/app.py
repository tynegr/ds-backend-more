import logging
from flask import Flask, request
from models.plate_reader import PlateReader
from utils import read_number_by_id

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return '<h1><center>Hello!</center></h1>'

@app.route('/read-number')
def read_number():
    image_id = request.args.get('id')
    result = read_number_by_id(reader, image_id)
    return result

@app.route('/read-multiple-numbers')
def read_multiple_numbers():
    image_id_list = request.args.getlist('id')
    response = {}
    for image_id in image_id_list:
        model_response, status_code = read_number_by_id(reader, image_id)
        if status_code != 200:
            return model_response
        response[image_id] = model_response[image_id]
    return response

if __name__ == '__main__':
    logging.basicConfig(
        format='[%(levelname)s] [%(asctime)s] %(message)s',
        level=logging.INFO,
    )

    reader = PlateReader().load_from_file(
        "./model_weights/plate_reader_model.pth")

    app.run(host='0.0.0.0', port=8080, debug=True)
