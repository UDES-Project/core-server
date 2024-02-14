from flash_flask import route

# Just for tests, will be updated later
@route()
def endpoint():
    return {
        "server_name": "UMES Core Server"
    }