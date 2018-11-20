from Compilers.CompilerBase import CompilerBase

class GCC(CompilerBase):

    def name(self):
        return "gcc"

    def is_available(self):
        return True

    def conan_version(self):
        return self.major_version()
    
    def CXX(self):
        return "g++"
    
