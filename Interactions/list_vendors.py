from models.vendors import Vendor
from app.__init__ import json_encoder
from math import ceil

def get_pagination_data(query, page, page_limit):
    total_count = query.count()
    params = {
      'page': page,
      'total': ceil(total_count/page_limit),
      'total_count': total_count,
      'page_limit': page_limit
    }
    return params

def list_vendors(page, page_limit):
    query = Vendor.select() 
    pagination_data = get_pagination_data(query, page, page_limit)
    query = query.paginate(page, page_limit)
    data = list(query.dicts())

    return {'list': data, 'pagination_data': pagination_data}