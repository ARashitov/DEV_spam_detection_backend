from .data_models import Email
from .ml_model_pipeline import pipeline
from typing import Optional


def add_predict_endpoint(app):
    @app.post("/predict/")
    async def predict_spam(email: Email, threshold: Optional[float] = 0.5):

        # 1. Prediction
        probability = pipeline.predict_proba(email.content)[0][1]
        probability = float(probability)

        # 2. Interpretation
        email.spam_probability = probability
        email.is_spam = probability > threshold
        return email
