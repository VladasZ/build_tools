import re
import Args
import Shell
import System

def get_version(compiler):
    version = Shell.get([compiler,  "--version"])
    return re.search("[0-9].[0-9].[0-9]", version).group(0)[0:3]

class Compiler:

    def __init__(self, name = '', version = ''):
        self.name        = name
        self.cppname     = self._cpp_name()
        self.version     = version if self.isVS() or self.isApple() else get_version(name)
        self.libcxx      = self._libcxx()

    def _cpp_name(self):
        if self.isGCC():
            return "g++"
        return self.name + "++"

    def isGCC(self):
        return self.name == "gcc"
        
    def isVS(self):
        return self.name == 'Visual Studio'

    def isApple(self):
        return self.name == 'apple-clang'
        
    def _libcxx(self):
        return 'libc++' if self.isApple() else 'libstdc++'

gcc           = Compiler('gcc'                 )
clang         = Compiler('clang'               )
visualStudio  = Compiler('Visual Studio', '15' )
appleClang    = Compiler('apple-clang'  , '9.1')

def print_info():
    print(gcc.name   + " " + gcc.version)
    print(clang.name + " " + clang.version)
    
def default():
    if System.is_windows:
        if Args.ide:
            return visualStudio
        return gcc
    if System.is_mac:
        return appleClang
    if System.is_linux:
        return gcc

def get():
    if Args.clang:
        if System.is_mac:
            return appleClang
        return clang
    if Args.gcc:
        return gcc
    return default()
