from flask import Flask, request, jsonify
from insert_data import insert_data
import os

PORT = int(os.environ.get('PORT', 4000))
DEBUG = False
HOST = '0.0.0.0'

app = Flask(__name__)

@app.route("/api/add_image", methods = ['POST'])
def add_image():
    payload = request.json
    image_path = payload['image_path']
    image_class = payload['image_class']
    group = 'train'
    weight = 1

    insert_data(image_path, image_class, group, weight)

    return jsonify({"status": "success", "message": f"Processed image"}), 200

if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)


