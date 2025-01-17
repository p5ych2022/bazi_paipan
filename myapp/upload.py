from flask import Flask, request, jsonify
import base64
from flask_cors import CORS # pip install flask-cors

app = Flask(__name__)
CORS(app)

@app.route('/upload-image', methods=['POST'])
def handle_image():
    image_data = request.json['image']
    image_data = image_data.split(",")[1]
    with open("output.png", "wb") as fh:
        fh.write(base64.b64decode(image_data))
    return jsonify({'message': 'Image saved successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50002,debug=True)
