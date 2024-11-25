from flash_flask import route
import json

@route()
def endpoint():
    return json.loads(open("public.json", "r").read())