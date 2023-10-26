from pydantic import BaseModel

class VendorCreate(BaseModel):
    vendor_name:str
    status:str="active"
    
