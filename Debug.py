import os
from inspect import getframeinfo, stack

def info(message = ""):
    caller = getframeinfo(stack()[1][0])
    print("[" + os.path.basename(caller.filename) + " - " + str(caller.lineno) + "]" + " : " + str(message))

def throw(error = ''):
    raise Exception(error)

def not_implemented():
    throw('Not implemented for this platform')
