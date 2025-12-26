from pydantic import BaseModel, EmailStr

class EmployeeBase(BaseModel): 
    name: str
    email: EmailStr

class EmployeeCreate(EmployeeBase): 
    pass

class EmployeeUpdate(EmployeeBase): 
    pass

class EmployeeOut(EmployeeBase): 
    id: int  # also add id

    class Config: 
        orm_mode=True



# This code:
# ✔ Validates input data
# ✔ Separates create / update / response schemas
# ✔ Works smoothly with SQLAlchemy ORM
# ✔ Protects database from invalid data


#dataflow: 
# Client Request
#    ↓
# Pydantic Schema (validation)
#    ↓
# SQLAlchemy Model (database)
#    ↓
# Pydantic Response (JSON)


# #Summary (short & simple)
# This code defines Pydantic schemas for employee data.
# EmployeeBase holds common fields.
# EmployeeCreate & EmployeeUpdate are used for input validation.
# EmployeeOut is used for API responses.
# orm_mode=True allows SQLAlchemy models to be returned as JSON.
