import Args
import Shell
import System

class Compiler:

    def __init__(self, name = '', cppname = '', version = ''):
        self.name        = name
        self.cppname     = cppname
        self.version     = version
        self.libcxx      = self._libcxx()

    def isVS(self):
        return self.name == 'Visual Studio'

    def isApple(self):
        return self.name == 'apple-clang'
        
    def _libcxx(self):
        return 'libc++' if self.isApple() else 'libstdc++'



gcc_version = Shell.get(['gcc', '-dumpversion'])[:3]

visualStudio  = Compiler('Visual Studio', version = '15'        )
gcc           = Compiler('gcc',          'g++',      gcc_version)
clang         = Compiler('clang',        'clang++',  '6.0'      )
appleClang    = Compiler('apple-clang',  'clang++',  '9.1'      )

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
