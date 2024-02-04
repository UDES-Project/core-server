import base64
from flash_flask import route, Utils
from flash_flask.db import MySQL
from flask import request

from src.utils import new_public_id
from src.errors import Errors

@route(["GET", "POST"])
def endpoint():
    if request.method == "GET":
        return GET()
    else:
        return POST()
    
def GET():
    
    public_id = request.args.get('public_id')
    
    if not public_id:
        return {
            "error": Errors.SPECIFY("public_id")
        }
    
    try:
        row = MySQL.fetch_one("SELECT * FROM files WHERE public_id = %s", (public_id,))
    except Exception as e:
        return {
            "error": str(e)
        }
        
    if not row:
        return {
            "error": Errors.NOT_FOUND()
        }
    
    return {
        "key": MySQL.get_row_col(row, "files", "key"),
        "filename": MySQL.get_row_col(row, "files", "filename")
    }

def POST():    
    try:
        key, filename = Utils.get_json_values(["key", "filename"])
    except Exception as e:
        return {
            "error": str(e)
        }
    
    public_id = new_public_id()
    
    try:
        MySQL.insert_into("files", ("public_id", "key", "filename"), (public_id, key, filename))
    except Exception as e:
        return {
            "error": str(e)
        }
    
    return {
        "public_id": public_id
    }