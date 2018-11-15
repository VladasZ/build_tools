
class Compiler():

    def __init__(self):
        self.name          = self._get_name         ()
        self.libcxx        = self._libcxx           ()
        self.version       = self._get_version      ()
        self.full_version  = self._get_full_version ()
        self.conan_version = self._get_conan_version()
        self.CC            = self._CC               ()
        self.CXX           = self._CXX              ()
        self.is_available  = self._is_available     ()

    def _get_name():
        return ""

    def _libcxx():
        return "libstdc++"
    
    def _get_version():
        return ""

    def _get_full_version():
        return ""

    def _is_available():
        return False



    

    
