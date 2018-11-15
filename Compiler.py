import re
import Args
import Shell
import Debug
import System


class Compiler:

    def __init__(self, name):
        self.name         = name
        self.libcxx       = self._libcxx()
        self.version      = self._find_version()
        self.full_version = self._get_full_version()
        self._is_apple()
        
    def _is_apple(self):
        return False
        if not self.isClang():
            return False
        info = Shell.run(["clang", "-v"], simple = False)
        return "Apple" in info

    def _get_apple_version(self):
        version = re.search("[0-9]{1,2}[.][0-9][.][0-9]", Shell.run(["clang", "-v"], simple = False)).group()[0]
        return version
        
    def _check_version(self, version):
        return (Shell.check([self.name               + "-" + version, "-dumpversion"]) and
                Shell.check([self._cpp_name_prefix() + "-" + version, "-dumpversion"])    )
        
    def _find_version(self, supported_versions = ["8", "7"]):
        if self._is_apple():
            return _get_apple_version()
        for version in supported_versions:
            if self._check_version(version):
                return version
        return ""

    def _get_full_version(self):
        if not self.available():
            return ""
        return Shell.get([self.CC(), "-dumpversion"]).strip()
    
    def _cpp_name_prefix(self):
        if self.isGCC():
            return "g++"
        if self.isClang():
            return "clang"
        return self.name + "++"

    def available(self):
        return len(self.version) != 0  
    
    def CXX(self):
        return self._cpp_name_prefix() + "-" + self.version
    
    def CC(self):
        return self.name + "-" + self.version

    def isClang(self):
        return self.name == "clang"
    
    def isGCC(self):
        return self.name == "gcc"
    
    def isVS(self):
        return self.name == "Visual Studio"
    
    def isApple(self):
        return self.name == "apple-clang"

    def info(self):
        if not self.available():
            return self.name + " - not available"
        return self.name + "-" + self.full_version
    
    def _libcxx(self):
        return 'libc++' if self.isApple() else 'libstdc++'

gcc   = Compiler('gcc')
clang = Compiler('clang')

def default():
    return gcc

def get():
    return default()

def get_info():
    return gcc.info() + "\n" + clang.info()
