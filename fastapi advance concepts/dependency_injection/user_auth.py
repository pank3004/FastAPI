from fastapi import FastAPI, Depends, HTTPException, Form, status
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@app.post('/token')
def login(username: str = Form(...), password: str = Form(...)):
    if username == 'pankaj' and password == 'pass123':             # hardcode for demo here(in real it matched in databases)
        return {'access_token': 'valid_token', 'token_type': 'bearer'}    # hardcode here for demo
    raise HTTPException(status_code=400, detail='Invalid Credentials')


def decode_token(token: str):
    if token == 'valid_token':
        return {'name': 'pankaj'}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid Authentication Credentials'
    )

def get_current_user(token: str = Depends(oauth2_scheme)):
    return decode_token(token)


@app.get('/profile')
def get_profile(user=Depends(get_current_user)):
    return {'username': user['name']}


