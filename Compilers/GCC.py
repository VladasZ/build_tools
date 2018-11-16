
from Compilers.CompilerBase import CompilerBase

class GCC(CompilerBase):

    def __init__(self):
        super().__init__()

    def _get_name(self):
        return "gcc"

    def _libcxx(self):
        return "libstdc++"
    
    def _get_version(self):
        return "7"

    def _get_full_version(self):
        return "7.3.0"

    def _get_conan_version(self):
        return "7.3"

    def _is_available(self):
        return True

    def _CC(self):
        return "gcc"

    def _CXX(self):
        return "g++"
    
