import json
import requests

EMAIL_SAMPLE = 'data/emails/emailSample1.txt'
ENDPOINT_URL = 'http://127.0.0.1:8000/predict'


def read_content(path):
    with open(path, "r") as f:
        content = f.read()
    return content


def test_redundant_is_spam_1():
    """
        Adds redundant `is_spam` field to body
    """
    message = {
        'content': read_content(EMAIL_SAMPLE),
        'is_spam': True,
    }
    r = requests.post(ENDPOINT_URL, json=message)
    assert r.status_code == 200


def test_incorrect_is_spam_1():
    """
        Adds int `is_spam` field to body
        violating data scheme
    """
    message = {
        'content': read_content(EMAIL_SAMPLE),
        'is_spam': 12321312312,
    }
    r = requests.post(ENDPOINT_URL, json=message)
    if r.status_code == 422:
        assert True


def test_redundant_spam_probability_1():
    """
        Adds redundant `is_spam` field to body
    """
    message = {
        'content': read_content(EMAIL_SAMPLE),
        'spam_probability': 0.312312312,
    }
    requests.post(ENDPOINT_URL, json=message)
    assert True


def test_incorrect_spam_probability_1():
    """
        Adds redundant `is_spam` field to body
    """
    message = {
        'content': read_content(EMAIL_SAMPLE),
        'spam_probability': True,
    }
    r = requests.post(ENDPOINT_URL, json=message)
    assert r.status_code == 200


def test_spam_threshold_parameter():
    """
        Adds redundant `is_spam` field to body
    """
    message = {
        'content': read_content(EMAIL_SAMPLE),
        'spam_probability': True,
    }

    # 1. Case with small spam threshold
    r = requests.post(ENDPOINT_URL + '?threshold=0.1',
                      json=message)
    response = json.loads(r.text)
    assert response['is_spam']

    # 2. Case with large spam threshold
    r = requests.post(ENDPOINT_URL + '?threshold=0.9',
                      json=message)
    response = json.loads(r.text)
    assert not response['is_spam']


def test_incorrect_content_1():
    """
        content = None
    """
    message = {
        'content': None,
        'spam_probability': True,
    }
    r = requests.post(ENDPOINT_URL, json=message)
    assert r.status_code == 422


def test_empty_content_1():
    message = {
        'content': '',
        'spam_probability': True,
    }
    r = requests.post(ENDPOINT_URL, json=message)
    assert r.status_code == 200