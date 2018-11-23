
class Compiler():

    def __init__(self,
                 name,
                 is_available  = False,
                 libcxx        = "libstdc++",
                 conan_name    = None,
                 full_version  = "",
                 major_version = 0,
                 conan_version = None,
                 CC            = None,
                 CXX           = None,
                 _str          = None):

        self.name          = name
        self.is_available  = is_available
        self.libcxx        = libcxx

        if conan_name:
            self.conan_name = conan_name
        else:
            self.conan_name = name
            
        self.full_version  = full_version
        self.major_version = major_version

        if conan_version:
            self.conan_version = conan_version
        else:
            self.conan_version = full_version

        if CC:
            self.CC = CC
        else:
            self.CC = name

        if CXX:
            self.CXX = CXX
        else:
            self.CXX = name + "++"
            
        if _str:
            self._str = _str
        else:
            if is_available:
                self._str = self.name + " " + self.full_version
            else:
                self._str = self.name + " - not avalilable"
            
    def __str__(self):
        return self._str

