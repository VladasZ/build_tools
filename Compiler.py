import Args
import System

from Compilers.GCC          import GCC
from Compilers.VisualStudio import VisualStudio

gcc           = GCC()
visual_studio = VisualStudio()

def get_ide():
    if System.is_windows:
        return visual_studio
    return gcc

def get():
    if Args.ide:
        return get_ide()
    return gcc

print(gcc)
print(visual_studio)



