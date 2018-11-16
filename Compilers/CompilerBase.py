import Shell
import Regex
import Debug

class CompilerBase():

    def __init__(self):
        self.name          = self._get_name         ()
        self.libcxx        = self._libcxx           ()
        self.full_version  = self._get_full_version ()
        self.conan_version = self._get_conan_version()
        self.major_version = self._get_major_version()
        self.CC            = self._CC               ()
        self.CXX           = self._CXX              ()
        self.is_available  = self._is_available     ()
        self.is_ide        = self._is_ide           ()

    def _get_name(self):
        return None

    def _libcxx(self):
        return "libstdc++"

    def _get_full_version(self):
        return Regex.version(Shell.get([self.name, "-v"]))

    def _get_major_version(self):
        return self.full_version

    def _get_conan_version(self):
        if self.full_version:
            return self.full_version[:3]

    def _is_available(self):
        return False

    def _CC(self):
        return self.name

    def _CXX(self):
        return self.name + "++"

    def _is_ide(self):
        return False
    
    def __str__(self):
        if not self._is_available():
            return self.name + " is not available"
        return self.name + "-" + str(self.full_version) + " CC: " + self.CC + " CXX: " + self.CXX

    

    
