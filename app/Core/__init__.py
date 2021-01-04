import os
import pickle
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from .AutoML import fit, predict
load_dotenv(dotenv_path=Path('.') / '.env_dev')


VOCABULARY_PATH = os.environ['VOCABULARY_PATH']
SAMPLE_EMAIL = os.environ['SAMPLE_EMAIL']
MODEL_PATH = os.environ['MODEL']
MODEL_REPORT = str(MODEL_PATH.replace('.pkl', '_report.csv'))
TRAIN_DATA = os.environ['TRAIN_DATA']
TEST_DATA = os.environ['TEST_DATA']


# 1. Reading data
global vocabulary
global email_content
global model

vocabulary = pd.read_csv(VOCABULARY_PATH)
with open(SAMPLE_EMAIL) as email:
    email_content = email.read()
model = pickle.load(open(MODEL_PATH, 'rb'))
