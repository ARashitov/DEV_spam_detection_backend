import os
from flask import Flask
from flask_restful import Api
# Environment vars
# from pathlib import Path
# from dotenv import load_dotenv
# load_dotenv(dotenv_path=Path('/home/atmos/Hobby/FlaskExploration/Docker/') / '.env_dev')
from Resources import Predict, Fit

ACTIVATE_FIT = os.environ['ACTIVATE_FIT'] == 'True'

# Application endpoints collection
app = Flask(__name__)
api = Api(app)
app.secret_key = b'\xc2\xee/\x0bg\xe4\x04\x8a\xc3\x1af\xa8\xd6a#\x89'
api.add_resource(Predict, '/predict')
if ACTIVATE_FIT:
    api.add_resource(Fit, '/fit')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
