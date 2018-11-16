import System
from Compilers.CompilerBase import CompilerBase

class VisualStudio(CompilerBase):

    def __init__(self):
        super().__init__()

    def _get_name(self):
        return "Visual Studio"
    
    def _get_full_version(self):
        return "15"

    def _is_available(self):
        return System.is_windows

    def _is_ide(self):
        return True
    
    def __str__(self):
        if self._is_available():
            return self.name + " " + self.version
        return super().__str__()
