from fastapi import FastAPI, HTTPException
from models_val import Employee
from typing import List

Employee_db:List[Employee] = []

app=FastAPI()


# 1 read all the employees
@app.get('/employees', response_model=List[Employee])
def get_employees(): 
    return Employee_db

# 2 read spcific employee
@app.get('/employee/{emp_id}', response_model=Employee)
def get_employee(emp_id:int): 
    for index, employee in enumerate(Employee_db): 
        if (employee.id==emp_id): 
            return Employee_db[index]
        
    raise HTTPException(status_code=404, detail="Employee not found")

# 3 add an employee
@app.post('/add_employee', response_model=Employee)
def add_employee(new_emp:Employee): 
    for employee in Employee_db: 
        if (employee.id==new_emp.id): 
            raise HTTPException(status_code=400, detail="Employee alread exist")

    Employee_db.append(new_emp)
    return new_emp

# 4update an employee
@app.put('/update_employee/{emp_id}', response_model=Employee)
def update_employee(emp_id: int, updated_employee: Employee): 
    for index, employee in enumerate(Employee_db): 
        if (employee.id==emp_id): 
            Employee_db[index]=updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")


# 5 delete an employee
@app.delete('/delete_employee/{emp_id}')
def delete_employee(emp_id: int): 
    for index, employee in enumerate(Employee_db): 
        if(employee.id==emp_id):
            del Employee_db[index]
            return {'message': 'employee deleted succesfully'}
        
    raise HTTPException(status_code=404, detail="Employee not found")