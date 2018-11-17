from Compilers.CompilerBase import CompilerBase

class GCC(CompilerBase):

    def _get_name(self):
        return "gcc"

    def _is_available(self):
        return True

    def _get_conan_version(self):
        return self.major_version
    
    def _CXX(self):
        return "g++"
    
