import json
import Core
from flask import request, jsonify


def add_predict(app):
    """
        Represents all available products
    """
    @app.route('/predict', methods=['POST'])
    def api_predict():

        # Parsing argument
        X = json.loads(request.get_data())
        email_content = X['email_content']

        # Prediction
        y = Core.predict(Core.model, email_content, Core.vocabulary)

        # Response return
        return jsonify(json.dumps({
            **X,
            'is_spam': 'True' if y[0] == 1 else 'False'}))


def add_fit(app):
    @app.route('/fit', methods=['GET'])
    def api_fit():
        Core.fit(Core.TRAIN_DATA, Core.TEST_DATA,
                 Core.MODEL_PATH, Core.MODEL_REPORT)
        return jsonify(json.dumps({
            'msg': 'model has been updated'
        }))
