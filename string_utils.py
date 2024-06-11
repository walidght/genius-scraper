import re


def clean_title(input_string):
    # Use regular expression to keep only alphanumeric characters and hyphen
    alphanumeric_string = re.sub(r'[^a-zA-Z0-9-]', '', input_string)
    # Convert the string to lowercase
    lowercase_alphanumeric_string = alphanumeric_string.lower()
    return lowercase_alphanumeric_string
