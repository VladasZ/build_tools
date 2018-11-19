import Shell
import Regex
import System
from Compilers.CompilerBase import CompilerBase

class Clang(CompilerBase):

    def _get_name(self):
        return "clang"    
    
    def _get_conan_name(self):
        return "apple-clang" if System.is_mac else self.name

    def _libcxx(self):
        return 'libc++'
    
    def _get_conan_version(self):
        if (self.major_version == "10"):
            return self.full_version[:4]
        return self.full_version[:3]
    
    def _is_available(self):
        return Shell.check(["clang", "-dumpversion"])    

    def __str__(self):
        if self._is_available() and System.is_mac:
            return self.conan_name + " " + self.full_version
        return super().__str__()
