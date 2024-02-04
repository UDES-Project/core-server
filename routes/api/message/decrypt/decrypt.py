from flash_flask import route

from src.utils import get_url_args

import base64

@route()
def endpoint():
    try:
        content, key = get_url_args([("content", str), ("key", str)])
        content, key = base64.b64decode(content.encode()), key.encode()
    except Exception as e:
        return {
            "error": str(e)
        }
    
    result = "".join([chr(char ^ key[i % len(key)]) for i, char in enumerate(content)])
    
    return {
        "result": result
    }