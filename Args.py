import sys

def has(flag_name):
    for arg in sys.argv:
        if arg == flag_name:
            return True
    return False

def get(index):
    return sys.argv[index]

def count():
    return len(sys.argv)
    