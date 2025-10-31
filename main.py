from fastapi import FastAPI,Path,HTTPException, Query
import json

app=FastAPI()

def load_data(): 
    with open('patients.json', 'r') as f:
        data=json.load(f) 
        return data

@app.get("/")
def hello(): 
    return {'message': 'welcome to patient doctor app'}

@app.get('/about')
def about(): 
    return {'message': 'it is the api where we can store and retrive data of the patients'}

@app.get('/view')
def view(): 
    data=load_data()
    return data

# @app.get('/patient/{patient_id}')
# def view_specific_patient(patient_id: str=Path(..., description='id of the patient in db', example='P003')): 
#     data=load_data()
#     if patient_id in data: 
#         return data[patient_id]
#     raise HTTPException(status_code=404, detail='patient not found')

# @app.get('/sort')
# def sort_patient(sort_by:str=Query(..., description="sort by weight, height, bmi"),  
#                  order:str=Query('asc', description='order by asc(default), desc')): 
#                 # sort_by is required and order by optional because by default is asc
#     data=load_data()
#     safe_fields=['height', 'weight', 'bmi']
#     safe_order=['asc', 'desc']

#     if sort_by not in safe_fields: 
#         raise HTTPException(status_code=400, detail=f'invalid field select from {safe_fields}')
#     if order not in safe_order: 
#         raise HTTPException(status_code=400, detail=f'invalid order select from {safe_order}')
    
#     orderr=True if order=='desc' else False
#     sort_data=sorted(data.values(), key=lambda x:x.get(sort_by, 0), reverse=orderr)

#     return sort_data
