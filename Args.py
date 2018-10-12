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

gcc        = has('--gcc')
run        = has('--run')
make       = has('--make')
test       = has('--test')
flash      = has('--flash')
build      = has('--build')
clang      = has('--clang')
verilog    = has('--verilog')
android    = has('--android')
rmbuild    = has('--rmbuild')
simulate   = has('--simulate')
forceBuild = has('--forcebuild')

all = sys.argv
    
