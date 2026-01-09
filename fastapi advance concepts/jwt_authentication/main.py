from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth import create_access_token, verify_token
from models import UserInDB
from utils import get_user, verify_password

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token') #Read the Bearer token from the request’s Authorization header


@app.post('/token')
def login(form_data: OAuth2PasswordRequestForm = Depends()):  # no depends
    user_dict = get_user(form_data.username)
    if not user_dict:
        raise HTTPException(400, detail='Invalid Username')
    if not verify_password(form_data.password, user_dict['hashed_password']):
        raise HTTPException(400, detail='Invalid Password')
    
    access_token = create_access_token(data={'sub': form_data.username})
    return {'access_token': access_token, 'token_type': 'bearer'}


@app.get('/users')
def read_users(token: str = Depends(oauth2_scheme)):  # extract the token from the authorization header and injects it into the token parameter
    username = verify_token(token)   # decodes and validates the jwt
    return {'username': username}   # returns the username encoded in the token