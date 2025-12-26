from sqlalchemy.orm import Session
import models, schemas

#SELECT * FROM employees;
def get_employees(db:Session): 
    return db.query(models.Employee).all()

# SELECT * FROM employees WHERE id = emp_id LIMIT 1;
def get_employee(db:Session, emp_id: int): 
    return (db.query(models.Employee)
            .filter(models.Employee.id==emp_id)
            .first()
            )

# INSERT INTO employees (name, email) VALUES (...);
def create_employee(db:Session, employee: schemas.EmployeeCreate): 
    db_employee=models.Employee(name=employee.name, email=employee.email)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)  # to create id automatically
    return db_employee


# UPDATE employees SET name=?, email=? WHERE id=emp_id;
def update_employee(db:Session, emp_id: int, employee:schemas.EmployeeUpdate): 
    db_employee=db.query(models.Employee).filter(models.Employee.id==emp_id).first()
    if db_employee: 
        db_employee.name=employee.name
        db_employee.email=employee.email
        db.commit()
        db.refresh(db_employee)
    return db_employee


#DELETE FROM employees WHERE id = emp_id;
def delete_employee(db:Session, emp_id:int): 
    db_employee=db.query(models.Employee).filter(models.Employee.id==emp_id).first()
    if db_employee: 
        db.delete(db_employee)
        db.commit()
    return db_employee




# This code file acts as the CRUD service layer for the Employee module.
# It uses SQLAlchemy sessions to interact with the database.

# It connects:
            # Pydantic schemas → for validated input data
            # SQLAlchemy models → for database tables

# What each function does (at a glance):
            # get_employees → fetches all employees
            # get_employee → fetches one employee by ID
            # create_employee → adds a new employee to the database
            # update_employee → updates an existing employee’s details
            # delete_employee → removes an employee from the database

# Why this design is good:
            # Keeps database logic separate from API routes
            # Makes code clean, reusable, and easy to maintain
            # Follows real-world backend and FastAPI best pratices

# One-line interview answer:
# This module implements all CRUD operations for employees using SQLAlchemy sessions, acting as a clean service layer between FastAPI routes and the database.