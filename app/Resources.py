import Core
from flask_restful import Resource, reqparse, abort


PREDICT_ARG_PARSER = reqparse.RequestParser()
PREDICT_ARG_PARSER.add_argument('email_content', type=str, required=True,
                                help='Please provide email_content field')


class Predict(Resource):

    def predict(self, email_content):
        try:
            y = Core.predict(Core.model, email_content, Core.vocabulary)
            print(y)
            return True if y[0] == 1 else False
        except Exception as exc:
            abort(500, message=f"(Model prediction error): {exc}")

    def post(self):
        email_content = PREDICT_ARG_PARSER.parse_args()['email_content']
        return {'email_content': email_content,
                'is_spam': self.predict(email_content)}, 200


class Fit(Resource):

    def fit(self):
        try:
            Core.fit(Core.TRAIN_DATA, Core.TEST_DATA,
                     Core.MODEL_PATH, Core.MODEL_REPORT)
        except Exception as exc:
            abort(500, message=f'(Model training error): {exc}')

    def get(self):
        self.fit()
        return {'message': 'Spam detection model has been updated!'}, 202
