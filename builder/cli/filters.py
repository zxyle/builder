import random
import re
import string

CAMELCASE_INVALID_CHARS = re.compile(r'[^a-zA-Z\d]')


def string_camelcase(value):
    return CAMELCASE_INVALID_CHARS.sub('', value.title())


def sanitize(module_name):
    """Sanitize the given module name, by replacing dashes and points
    with underscores and prefixing it with a letter if it doesn't start
    with one
    """
    return CAMELCASE_INVALID_CHARS.sub('', module_name)


def underscore(value):
    return CAMELCASE_INVALID_CHARS.sub('_', value)


def passphrase(length=32, punctuation=False, digits=True):
    characters = string.ascii_letters
    if digits:
        characters += string.digits

    if punctuation:
        punctuations = string.punctuation.replace('"', "").replace('\\', "")
        characters += punctuations

    password = ''.join(random.sample(characters, length))
    return password
