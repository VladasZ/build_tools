from Compilers.Manual import Manual
from Compilers.GCC    import GCC


manual = Manual()
gcc    = GCC()


def get():
    return gcc

print(gcc)



