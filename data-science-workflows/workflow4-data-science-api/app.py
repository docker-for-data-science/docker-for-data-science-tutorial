# Adapted from http://flask-restful.readthedocs.io/

# Flask Extensions
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

# pydata stack
import numpy as np
from sklearn.externals import joblib


# set up Flask and Flask-Restful
app = Flask(__name__)
api = Api(app)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('sepal_length', type=float)
parser.add_argument('sepal_width', type=float)
parser.add_argument('petal_length', type=float)
parser.add_argument('petal_width', type=float)


class IrisPredict(Resource):
    def get(self):
        # parse arguments
        args = parser.parse_args()
        sepal_length = args['sepal_length']
        sepal_width = args['sepal_width']
        petal_length = args['petal_length']
        petal_width = args['petal_width']

        # create numpy ndarray
        pt_to_predict = np.array([[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]])

        # load model and predict
        knn_from_pkl = joblib.load('iris_knn_model.pkl')
        predicted_class = knn_from_pkl.predict(pt_to_predict)

        # return answer
        prediction = {
            'predicted_class': predicted_class.tolist()
        }
        result = {'data': dict(prediction)}
        return jsonify(result)


# create endpoint
api.add_resource(IrisPredict, '/predict/iris/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port='5000',
    )
