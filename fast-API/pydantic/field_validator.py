from pydantic import BaseModel , EmailStr, Field, field_validator
from typing import List , Dict,Optional, Annotated
class Patient(BaseModel):
    name :Annotated[str ,  Field(max_length = 50, title = "PATIENT NAME", description = "give the patient name", examples = ['asad', 'owais'])]
    age : int = Field(gt = 0 , lt = 120)
    email : EmailStr
    weight : Annotated[float, Field(gt = 0, strict = True)]
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


    @field_validator('name')
    @classmethod
    def name(cls,value):
        return value.upper()

    @field_validator('age', mode  = 'before') 
    @classmethod
    def insert_age(cls,value): 
        if  0 > value  < 100:              
            return value
        raise ValueError ("age is in incorrect")    

    
def insert_patient(patient :Patient):
     
    print(patient.name)
    print(patient.age)
    print(patient.email)
#by default all fields are required

patient_info = {'name': 'asad', 'age':23, 'email': 'asad.denin@jsb.com','weight': 54.5, 'married': True , 'allergies':['pollen','migrain','insane','pain'], 
                'contact_details':{'contact_no': '+923215109122'}}
patient1 = Patient(**patient_info)

insert_patient(patient1)