import os
import numpy as np
import pickle
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from EmailPreprocessor import EmailPreprocessor
load_dotenv(dotenv_path=Path('.') / '.env_dev')


VOCABULARY_PATH = os.environ['VOCABULARY_PATH']
SAMPLE_EMAIL = os.environ['SAMPLE_EMAIL']
MODEL = os.environ['MODEL']


def predict(model, email_content, vocabulary) -> int:
    """
        Note model requires list<list(int)>

        Arguments:
            * model (scikit-learn.GridSearch): model
            * email_content (str): email string
            * vocabulary (pd.DataFrame): vocabulary

        Returns:
            * list<int>: 0 - IS NOT SPAM, 1 - IS SPAM
            example: [0, 0, .. 1]
    """
    email_prep = EmailPreprocessor(vocabulary, email_content)
    X = [email_prep.preprocess_email()]
    return model.predict(X)


if __name__ == "__main__":

    # 1. Reading data
    vocabulary = pd.read_csv(VOCABULARY_PATH)
    with open(SAMPLE_EMAIL) as email:
        email_content = email.read()
    model = pickle.load(open(MODEL, 'rb'))
    
    print(predict(model, email_content, vocabulary))