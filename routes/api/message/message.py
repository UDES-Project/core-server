import base64
from flash_flask import route, Utils
from flash_flask.db import MySQL
import hashlib

from src.utils import exception_to_json, new_public_id
from src.errors import Errors

@route(["POST"])
def endpoint():
    
    try:
        action = Utils.get_json_values(["action"])[0]
    except Exception as e:
        return exception_to_json(e)
    
    if action == "create":
        return create()
    elif action == "read":
        return read()


def read():
    
    try:
        public_id = Utils.get_json_values(["public_id"])[0]
        secret = Utils.get_optional_json_values(["secret"], 0).get("secret")
    except Exception as e:
        return exception_to_json(e, str(e) == "Invalid request data")
    
    if not public_id:
        return {
            "error": Errors.SPECIFY("public_id")
        }
    
    try:
        message = MySQL.fetch_one("SELECT * FROM messages WHERE public_id = %s", (public_id,))
    except Exception as e:
        return exception_to_json(e)
        
    if not message:
        return {
            "error": Errors.NOT_FOUND()
        }
    
    if message.get("secret"):
        hashed_secret = hashlib.sha256(secret.encode()).hexdigest()
        if hashed_secret != message.get("secret"):
            return {
                "error": Errors.INVALID_SECRET()
            }
    
    return {
        "content": base64.b64encode(message.get("content")).decode()
    }

def create():    
    try:
        content = Utils.get_json_values(["content"])[0]
        content = base64.b64decode(content.encode())
        
        secret = Utils.get_optional_json_values(["secret"], 0).get("secret")
    except Exception as e:
        return exception_to_json(e)
    
    public_id = new_public_id()
    
    try:
        if secret:
            hashed_secret = hashlib.sha256(secret.encode()).hexdigest()
            MySQL.insert_into("messages", ("public_id", "content", "secret"), (public_id, content, hashed_secret))
        else:
            MySQL.insert_into("messages", ("public_id", "content"), (public_id, content))
    except Exception as e:
        return exception_to_json(e)
    
    return {
        "public_id": public_id
    }