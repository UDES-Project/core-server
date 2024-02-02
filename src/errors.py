class Errors:
    SPECIFY = lambda key: f"Please specify '{key}'"
    NOT_FOUND = lambda *_: "Not found"
    INVALID_TYPE = lambda key, type: f"{key} needs to be {type}"