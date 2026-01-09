from fastapi import FastAPI, Depends

app=FastAPI()


class Setting: 
    def __init__(self): 
        self.api_key='my_dummy_api_key'
        self.debug=True

def get_settings(): 
    return Setting()


@app.get('/config')
def get_config(settings:Setting=Depends(get_settings)): 
    return {'api_key': settings.api_key, 'debug': settings.debug}