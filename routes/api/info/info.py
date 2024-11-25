from flash_flask import route
import json

@route()
def endpoint():
    return json.loads(open("info.json", "r").read())