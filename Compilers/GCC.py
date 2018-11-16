from Compilers.CompilerBase import CompilerBase

class GCC(CompilerBase):

    def _get_name(self):
        return "gcc"

    def _is_available(self):
        return True

    def _CXX(self):
        return "g++"
    
