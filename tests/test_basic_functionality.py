import json
import requests


EMAIL_SAMPLE = 'data/emails/emailSample1.txt'
ENDPOINT_URL = 'http://127.0.0.1:8000/predict'


def read_content(path):
    with open(path, "r") as f:
        content = f.read()
    return content


def test_first_connection():
    message = {
        'content': read_content(EMAIL_SAMPLE)
    }
    r = requests.post(ENDPOINT_URL, json=message)
    assert r.status_code == 200


def test_api_response_completeness():
    """
        Ensures that all required fields are present
    """
    message = {
        'content': read_content(EMAIL_SAMPLE)
    }
    r = requests.post(ENDPOINT_URL, json=message)
    response = json.loads(r.text)
    assert 'content' in response.keys()
    assert 'is_spam' in response.keys()
    assert 'spam_probability' in response.keys()


def test_api_response_datatype():
    """
        Ensures that returned datatype are correct
    """
    message = {
        'content': read_content(EMAIL_SAMPLE)
    }
    r = requests.post(ENDPOINT_URL, json=message)
    response = json.loads(r.text)
    assert type(response['content']) == str
    assert type(response['is_spam']) == bool
    assert type(response['spam_probability']) == float


def test_message_content_correctness():
    """
        Tests if message content is the same at input & output
    """
    message = {
        'content': read_content(EMAIL_SAMPLE)
    }
    r = requests.post(ENDPOINT_URL, json=message)
    response = json.loads(r.text)
    assert response['content'] == message['content']
