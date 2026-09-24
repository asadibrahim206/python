from pydantic import BaseModel , EmailStr, Field
from typing import List , Dict,Optional, Annotated
class Patient(BaseModel):
    name :Annotated[str ,  Field(max_length = 50, title = "PATIENT NAME", description = "give the patient name", examples = ['asad', 'owais'])]
    age : int = Field(gt = 0 , lt = 120)
    email : EmailStr
    weight : Annotated[float, Field(gt = 0, strict = True)]
    married : Annotated[bool, Field(default = None , description = "if the patient is married")]
    allergies : Annotated[Optional[List[str]],  Field(default = None , max_length = 5)]
    contact_details : Dict[str,str]


def insert_patient(patient :Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
#by default all fields are required

patient_info = {'name': 'asad', 'age':20, 'email': 'asad.denin@gmail.com','weight': 54.5, 'married': True , 'allergies':['pollen','migrain','insane','pain'], 
                'contact_details':{'contact_no': '+923215109122'}}
patient1 = Patient(**patient_info)

insert_patient(patient1)