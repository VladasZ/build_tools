import System

from Compilers.CompilerBase import Compiler

def get():

    if not System.is_windows:
        return Compiler("Visual Studio")

    return Compiler(name = "Visual Studio",
                    is_available = True,
                    full_version = "15")
                    
