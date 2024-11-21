import traceback
import uuid

from src.errors import Errors

from flask import request

def new_public_id():
    return str(uuid.uuid4()).replace("-","")

def get_url_args(keys):
    values = []
    for arg in keys:
        
        key = arg
        _type = None
        
        if type(arg) == tuple:
            key = arg[0]
            _type = arg[1]
            
        value = request.args.get(key)
        
        if not value:
            raise Exception(Errors.SPECIFY(key))
        
        if _type and type(value) != _type:
            raise Exception(Errors.INVALID_TYPE(key, _type))
        
        values.append(value)
    return values

def exception_to_json(e, print_traceback = True):
    if print_traceback: traceback.print_exc()
    return {
        "error": str(e)
    }