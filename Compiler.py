import Args
import System

from Compilers.GCC          import GCC
from Compilers.Clang        import Clang
from Compilers.VisualStudio import VisualStudio

gcc           = GCC()
clang         = Clang()
visual_studio = VisualStudio()

def get_ide():
    if System.is_windows:
        return visual_studio
    if System.is_mac:
        return clang
    return gcc

def get():
    if Args.ide:
        return get_ide()
    if Args.clang:
        return clang
    if Args.gcc:
        return gcc
    if System.is_mac:
        return clang
    return gcc

print(gcc)
print(clang)
print(visual_studio)




