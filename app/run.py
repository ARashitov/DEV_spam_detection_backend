from fastapi import FastAPI
from .endpoints import add_predict_endpoint

app = FastAPI()
add_predict_endpoint(app)
