import re
import Args
import Shell
import System

_dpkg_list = Shell.get(['dpkg', '--list'])

def _get_version(compiler):
    version = Shell.get([compiler,  "--version"])
    return re.search("[0-9].[0-9].[0-9]", version).group(0)[0:3]

def _get_versions(base_name):

    if base_name == "Visual Studio":
        return ["15"]

    if base_name == "apple-clang":
        return ["9.1"]
    
    two_digits_versions = sorted(list(set(re.findall(base_name + '-[0-9].[0-9]', _dpkg_list))))
    two_digits_versions = [version[-3:] for version in two_digits_versions]
    two_digits_major_versions = [ver[:1] for ver in two_digits_versions]

    one_digit_versions = sorted(list(set(re.findall(base_name + '-[0-9]', _dpkg_list))))
    one_digits_major_versions = [ver[-1:] for ver in one_digit_versions]
    unique_one_digits_major_version = [ver for ver in one_digits_major_versions if ver not in two_digits_major_versions]

    return two_digits_versions + unique_one_digits_major_version
    
class Compiler:

    def __init__(self, name):
        self.base_name = name
        self.versions  = _get_versions(name)
        self.version   = self.versions[-1]
        self.libcxx    = self._libcxx()

    def _cpp_name_prefix(self):
        if self.isGCC():
            return "g++"
        if self.isClang():
            return "clang"
        return self.base_name + "++"

    def CXX(self):
        return self._cpp_name_prefix() + "-" + self.version
        
    def CC(self):
        return self.base_name + "-" + self.version

    def isClang(self):
        return self.base_name == "clang"
    
    def isGCC(self):
        return self.base_name == "gcc"
        
    def isVS(self):
        return self.base_name == "Visual Studio"
    
    def isApple(self):
        return self.base_name == "apple-clang"

    def info(self):
        _info = self.base_name + ":\n"
        for ver in self.versions:
            self.version = ver
            _info += self.CC()  + "\n"
        self.version = self.versions[-1]
        return _info
            
    def _libcxx(self):
        return 'libc++' if self.isApple() else 'libstdc++'

gcc          = Compiler('gcc'          )
clang        = Compiler('clang'        )
appleClang   = Compiler('apple-clang'  )
visualStudio = Compiler('Visual Studio')

def print_info():
    print("Avaliable compilers:")
    print(clang.info())
    print(gcc.info())    
    
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
