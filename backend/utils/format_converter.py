import json
import re 

def deleted_underscore(needed_string: str) -> str:
    underscore = re.findall('_[a-zA-Z]+"', needed_string)
    for i in underscore:
        needed_string = needed_string.replace(i, i[1:].capitalize())
    return needed_string


def format_converter(json_from_db: list) -> list:
    return deleted_underscore(json.dumps(json_from_db))
