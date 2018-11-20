import Shell
import Regex
import Debug

class CompilerBase():

    def name(self):
        return None

    def conan_name(self):
        return self.name()
    
    def libcxx(self):
        return "libstdc++"

    def full_version(self):
        return Regex.version(Shell.get([self.name(), "-v"]))

    def major_version(self):
        return Regex.first_number(self.full_version())

    def conan_version(self):
        if self.full_version():
            return self.full_version()[:3]
        
    def is_available(self):
        return False

    def CC(self):
        return self.name()

    def CXX(self):
        return self.name() + "++"

    def is_ide(self):
        return False
    
    def __str__(self):
        if not self.is_available():
            return self.name() + " is not available"
        return self.name() + "-" + str(self.full_version())

    

    
