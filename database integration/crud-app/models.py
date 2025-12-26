from sqlalchemy import Column, Integer, String
from database import Base

class Employee(Base): 
    __tablename__='employees'
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, index=True)
    email=Column(String, unique=True, index=True)



# Simple Summary: 

# This code creates an employees table in the database using SQLAlchemy ORM.
# The Employee class represents the table.
# Each class variable represents a column in the table:
# id → unique employee ID (primary key)
# name → employee name
# email → employee email (must be unique)
# Base connects this class to SQLAlchemy so it can be converted into a real database table.
# SQLAlchemy lets you define database tables using Python code instead of SQL.