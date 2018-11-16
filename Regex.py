import re

def version(string):
    result = re.search("[0-9]{1,2}[.][0-9][.][0-9]", string)
    if result:
        return result.group()


    
