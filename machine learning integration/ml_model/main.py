from fastapi import FastAPI
from schemas import InputSchema, OutputSchema
from predict import make_prediction, batch_prediction
from typing import List

app=FastAPI()


@app.get('/')
def index(): 
    return {'message':'Welcome to the Ml prediction app'}


@app.post('/prediction', response_model=OutputSchema)
def prediction(user_input:InputSchema): # bydefault user_input will be json in fastapi
    prediction=make_prediction(user_input.model_dump())     # json to dict convert 
    return OutputSchema(predicted_price=round(prediction,2))


@app.post('/batch_prediction', response_model=List[OutputSchema])
def prediction(user_inputs: List[InputSchema]): 
    predictions=batch_prediction([ui.model_dump() for ui in user_inputs])
    return [OutputSchema(predicted_price=round(prediction,2)) for prediction in predictions]
