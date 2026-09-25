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








address_dict = {'city': 'chitral' , 'state':'kpk', 'village': 'danin'}
address = Address(**address_dict)

