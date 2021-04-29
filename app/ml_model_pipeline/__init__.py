import os
import pickle
import pandas as pd
from .preprocessor import EmailContentPreprocessor
from sklearn.pipeline import Pipeline

VOCABULARY_PATH = os.environ['VOCABULARY_PATH']
MODEL_PATH = os.environ['MODEL']


# 1. Reading required data
vocabulary = pd.read_csv(VOCABULARY_PATH)
model = pickle.load(open(MODEL_PATH, 'rb'))

# 2. Pipeline construction
global pipeline
pipeline = Pipeline([
    ('preprocessor', EmailContentPreprocessor(vocabulary=vocabulary)),
    ('predictor', model)
])
