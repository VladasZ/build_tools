import sys
sys.path.append("..")

import System

from Compilers.CompilerBase import Compiler

def get():

    if not System.is_windows:
        return Compiler("Visual Studio")

    return Compiler(name = "Visual Studio",
                    is_available = True,
                    full_version = "15")
                    
    

print(get())

#     def name(self):
#         return "Visual Studio"
    
#     def full_version(self):
#         return "15"

#     def is_ide(self):
#         return True    
#     def __str__(self):
#         if self.is_available():
#             return self.name() + " " + self.full_version()
#         return super().__str__()
