from pydantic import BaseModel
from typing import Optional

class BMIBase(BaseModel):
    weight: float  # в кг
    height: float  # в см

class BMICalculate(BMIBase):
    pass

class BMIResult(BaseModel):
    bmi: float
    category: str
    description: str
    recommendations: str

class BMICategoryBase(BaseModel):
    name: str
    min_value: float
    max_value: float
    description: str
    recommendations: str

class BMICategoryCreate(BMICategoryBase):
    pass

class BMICategoryUpdate(BMICategoryBase):
    pass

class BMICategoryInDBBase(BMICategoryBase):
    id: int

    class Config:
        orm_mode = True

class BMICategory(BMICategoryInDBBase):
    pass

class BMICategoryInDB(BMICategoryInDBBase):
    pass
