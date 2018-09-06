
def throw(error = ''):
    raise Exception(error)

def not_implemented():
    throw('Not implemented for this platform')
