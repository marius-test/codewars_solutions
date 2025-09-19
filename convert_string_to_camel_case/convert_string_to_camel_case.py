import re


def to_camel_case(text):
    words = re.split("[-_]", text)
    result = [words[0]]
    for w in words[1:]:
        result.append(w.capitalize())
    camel = "".join(result)
        
    return camel
