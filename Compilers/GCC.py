from Compilers.CompilerBase import CompilerBase

class GCC(CompilerBase):

    def __init__(self):
        super().__init__()

    def _get_name(self):
        return "gcc"
    
    def _get_version(self):
        return "8.1"

    def _is_available(self):
        return True

    def _CXX(self):
        return "g++"
    
