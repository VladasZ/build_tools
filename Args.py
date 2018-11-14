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
ide        = has('--ide')
make       = has('--make')
test       = has('--test')
multi      = has('--multi')
flash      = has('--flash')
build      = has('--build')
clang      = has('--clang')
clean      = has('--clean')
verilog    = has('--verilog')
android    = has('--android')
prepare    = has('--prepare')
rmbuild    = has('--rmbuild')
simulate   = has('--simulate')
forceBuild = has('--forcebuild')

all = sys.argv
    
