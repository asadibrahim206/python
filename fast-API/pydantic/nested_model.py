from pydantic import BaseModel , Field
from typing import Optional, List , Annotated

class Address(BaseModel):
    city : str
    state : str
    village : Optional[str] = None

class Patient(BaseModel):
    name : str
    age : int
    allergy : List[str]
    weight : Annotated[float, Field(gt = 0 , lt = 200)]
    address : Address


address_dict = { 'city': 'chitral' ,'state':'kpk', 'village': 'danin'}
address1 = Address(**address_dict)

patient_info = {'name': 'asad', 'age':23, 'weight': 55.4 , 'allergy': ['posicle', 'pollen', 'migrain'], 'address':address1}

patient1 = Patient(**patient_info)

temp = patient1.model_dump()   #it will convert pydantic model to dic t need when we work with apis and when need to export


print(temp)