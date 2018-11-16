
class CompilerBase():

    def __init__(self):
        self.name          = self._get_name         ()
        self.libcxx        = self._libcxx           ()
        self.version       = self._get_version      ()
        self.full_version  = self._get_full_version ()
        self.conan_version = self._get_conan_version()
        self.CC            = self._CC               ()
        self.CXX           = self._CXX              ()
        self.is_available  = self._is_available     ()

    def _get_name(self):
        return ""

    def _libcxx(self):
        return "libstdc++"
    
    def _get_version(self):
        return ""

    def _get_full_version(self):
        return ""

    def _get_conan_version(self):
        return ""

    def _is_available(self):
        return False

    def _CC(self):
        return ""

    def _CXX(self):
        return ""
    
    def __str__(self):
        return self.name + "-" + self.version + " CC: " + self.CC + " CXX: " + self.CXX

    

    
