from flask import Flask
from routes import add_predict, add_fit
# Environment vars
# from pathlib import Path
# from dotenv import load_dotenv
# load_dotenv(dotenv_path=Path('.') / '.env_dev')

# Application endpoints collection
app = Flask(__name__)
app.secret_key = b'\xc2\xee/\x0bg\xe4\x04\x8a\xc3\x1af\xa8\xd6a#\x89'
add_predict(app)
add_fit(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
