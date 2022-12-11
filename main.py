from typing import Union
from joblib import load
from fastapi import FastAPI

app = FastAPI()

vector = load("count_vectorizer.joblib")
model = load("model.joblib")


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/prediction")
def get_prediction(review:str):
    text = [review]
    input = vector.transform(text)
    prediction = model.predict(input)
    prediction = int(prediction)
    if prediction > 0: 
        prediction = "Positive"
    else:
        prediction = "Negative"
    return {'sentence':review,'prediction':prediction}

