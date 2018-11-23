import Args
import System

import Compilers.GCC          
import Compilers.Clang        
import Compilers.VisualStudio 

gcc           = Compilers.GCC.get()
#clang         = Clang()
#visual_studio = VisualStudio()

def get_ide():
    return gcc
    if System.is_windows:
        return visual_studio
    if System.is_mac:
        return clang
    return gcc

def get():
    return gcc
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






