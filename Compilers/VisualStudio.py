import Args
import System

from Compilers.CompilerBase import Compiler

def get():

    if not System.is_windows:
        return Compiler("Visual Studio")

    full_version = "15"

    if Args.vs19:
    	full_version = "16"
    	
    return Compiler(name = "Visual Studio",
                    is_available = True,
                    full_version = full_version)
                    
