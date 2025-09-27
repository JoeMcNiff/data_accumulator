from flask import Flask, request, jsonify
from data_accumulator.api.insert_data import insert_data
from data_accumulator.api.upload_image import upload_image
import os

PORT = int(os.environ.get('PORT', 4000))
DEBUG = False
HOST = '0.0.0.0'

app = Flask(__name__)

@app.route("/api/add_image", methods = ['POST'])
def add_image():
    payload = request.json
    group = 'TRAIN'
    weight = 1

    image_path = upload_image(payload['requestedFilename'], payload['image_base64'], "jpg")
    insert_data(image_path, payload['image_class'], group, weight)

    return jsonify({"status": "success", "message": f"Processed image"}), 200

if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)


