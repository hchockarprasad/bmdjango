# Common utility tools

import re


# Function that generates validated string
def gen_val_str(value):

    # Remove all chars except the below REGEX
    result = re.sub('[^a-zA-Z0-9]', '', value)

    # Removes whitespaces between strings
    result = "".join(result.lower().split())

    return result
