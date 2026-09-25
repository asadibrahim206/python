from pydantic import BaseModel , EmailStr, Field, field_validator, model_validator,computed_field
from typing import List , Dict,Optional, Annotated


class Patient(BaseModel):
    name :Annotated[str ,  Field(max_length = 50, title = "PATIENT NAME", description = "give the patient name", examples = ['asad', 'owais'])]
    age : int = Field(gt = 0 , lt = 120)
    email : EmailStr
    weight : Annotated[float, Field(gt = 0, strict = True)]
    height : Annotated[float, Field]
    married : Annotated[bool, Field(default = None , description = "if the patient is married")]
    allergies : Annotated[Optional[List[str]],  Field(default = None , max_length = 5)]
    contact_details : Dict[str,str]


    @field_validator('email')               #field validator should alway be used with @field_validator (decorator) and @classmethod
    @classmethod
    def email_validator (cls, value):
    
        domain = ['hbl.com', 'askari.com' , 'jsb.com']
        domain_name = value.split('@')[-1]

        if domain_name not in domain:
            raise ValueError("DOMAIN INCORRECT :")
        return value

    @model_validator(mode = 'after')
    def validator(self):
        contact = self.contact_details or {}
        if self.age > 60 and 'Emergency' not in contact:
            raise ValueError('this is not allowed:')
        return self

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
def insert_patient(patient :Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.calculate_bmi)
#by default all fields are required


patient_info = {'name': 'asad', 'age':33, 'email': 'asad.denin@jsb.com','weight': 53.5, 'height':1.76784, 'married': True , 'allergies':['pollen','migrain','insane','pain'], 
                'contact_details':{'contact_no': '+923215109122', 'Emergency': '032244555666'}}
patient1 = Patient(**patient_info)
 
insert_patient(patient1)