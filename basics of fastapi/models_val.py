from pydantic import BaseModel, Field, StrictInt
from typing import Optional

class Employee(BaseModel): 
    id: int=Field(..., gt=0, title="Employee Id")  # ... means it is mandatry to pass
    name: str=Field(..., min_length=3, max_length=35)
    department: str=Field(..., min_length=3, max_length=40)
    age: Optional[int]=Field(default=None)
    country_code: Optional[StrictInt]=Field(default=91)
      # Int: automaticly type conversion ho jayega if possible eg age='34' -> age=34
      # StrictInt: strictly we have to pass int : no type conversion eg: age='45' >> error
