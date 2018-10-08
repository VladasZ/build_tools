import sys

def has(flag_name):
    for arg in sys.argv:
        if arg == flag_name:
            return True
    return False

def get(index = 1):
    return sys.argv[index]

def count():
    return len(sys.argv)

make       = has('--make')
rmbuild    = has('--rmbuild')
gcc        = has('--gcc')
clang      = has('--clang')
forceBuild = has('--forcebuild')
android    = has('--android')
run        = has('--run')

all = sys.argv
    
