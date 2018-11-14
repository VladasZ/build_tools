import sys
sys.path.append("~/.emacs.d/utils")
import System
import Compiler


print("OS: ", end = "")
print(System.os())
print("Available compilers: ")
print(Compiler.get_info(), end = "")
print("Default compiler: ", end = "")
print(Compiler.get().info())
