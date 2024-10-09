class Errors:
    SPECIFY = lambda key: f"Please specify '{key}'"
    NOT_FOUND = lambda *_: "Not found"
    INVALID_TYPE = lambda key, type: f"{key} needs to be {type}"
    INVALID_SECRET = lambda *_: "Invalid secret, this may not come from this author or may come from another extension."