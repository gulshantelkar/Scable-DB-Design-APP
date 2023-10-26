from models.vendors import Vendor  
from fastapi import HTTPException
def update_vendors(vendor_id,request):    
    try:
        vendor_obj = Vendor.get(Vendor.id == vendor_id)
    except Vendor.DoesNotExist:
        raise HTTPException(status_code=404, detail="Vendor not found")

    vendor_obj.vendor_name = request.vendor_name
    vendor_obj.active = request.active
    vendor_obj.save()

    return vendor_obj