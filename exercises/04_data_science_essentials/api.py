from model import prediction
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def predict():
    predicted_talks = prediction()
    return jsonify(predicted_talks), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
