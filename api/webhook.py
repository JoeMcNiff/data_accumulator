from flask import Flask, request, jsonify
from insert_data import insert_data
from download_image import download_image
import os

PORT = int(os.environ.get('PORT', 4000))
DEBUG = False
HOST = '0.0.0.0'

app = Flask(__name__)

@app.route("/api/add_image", methods = ['POST'])
def add_image():
    payload = request.json
    print(payload)
    image_data = payload['image_base64']
    image_class = payload['image_class']
    file_name = payload['requestedFilename']
    group = 'train'
    weight = 1

    image_path = download_image(file_name, image_data, "jpg")

    insert_data(image_path, image_class, group, weight)

    return jsonify({"status": "success", "message": f"Processed image"}), 200

if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)


