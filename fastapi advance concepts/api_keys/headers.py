from fastapi import FastAPI, Depends, HTTPException, Header

app = FastAPI()

API_KEY = 'my-secret-key'


def get_api_key(api_key: str = Header(...)):  # “Take this value from the HTTP request header, not from the body or query params.”
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail='Unauthorized')
    return api_key


@app.get('/get-data')
def get_data(api_key: str = Depends(get_api_key)):
    return {'output': 'Access Granted!'}