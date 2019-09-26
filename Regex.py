import re


def _get(string, regex):
    result = re.search(regex, string)
    if result:
        return result.group()


def first_number(string):
    return int(_get(string, "^(\D*)(\d+)"))


def version(string):
    return _get(string, "[0-9]{1,2}[.][0-9][.][0-9]")
