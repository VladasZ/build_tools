import Shell
import Regex
import Debug
import System
from Compilers.CompilerBase import CompilerBase

class Clang(CompilerBase):

    def name(self):
        return "clang"    
    
    def conan_name(self):
        return "apple-clang" if System.is_mac else self.name()

    def libcxx(self):
        return 'libc++'
    
    def conan_version(self):
        Debug.info(self.major_version())
        if (self.major_version() == "10"):
            return self.full_version()[:4]
        return self.full_version()[:3]
    
    def is_available(self):
        return Shell.check(["clang", "-dumpversion"])    

    def __str__(self):
        if self.is_available() and System.is_mac:
            return self.conan_name() + " " + self.full_version()
        return super().__str__()
