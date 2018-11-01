import os
import platform
import File
import Args
import Debug
import Shell
import System
import Compiler

make = 'Unix Makefiles'

cmake_file_name = "CMakeLists.txt"
cmake_search_default_depth = 3

def has_cmake_file(path = "."):
    return cmake_file_name in File.get_files(path)

def has_parent_cmake_files(path = ".", depth = cmake_search_default_depth):
    _path = path + "/.."
    for i in range(0, depth):
        if has_cmake_file(_path):
            return True
        _path += "/.."
    return False

def root_dir(path = '.'):
    _path = path
    print(_path)
    while not File.is_root(_path):
        if has_cmake_file(_path):
            if not has_parent_cmake_files(_path):
                return File.full_path(_path)
        _path += "/.."
    Debug.throw("CMake root directory not found for path: " + File.full_path(path))


    
def default_generator():
    if not Args.ide:
        return make
    if System.is_windows:
        return 'Visual Studio 15 2017 Win64'
    if System.is_mac:
        return 'Xcode'
    if System.is_linux:
        return 'CodeBlocks - Unix Makefiles'

def run(generator = default_generator()):
    Shell.run(['cmake', '-G', generator, '..'])

def setup(compiler = Compiler.get()):

    if compiler.isVS():
        return
    
    os.environ['CC']  = Shell.which(compiler.name)
    os.environ['CXX'] = Shell.which(compiler.cppname)
    
    if compiler.isApple():
        os.environ['CC']  = 'clang'

    print('CC = '  + os.environ['CC'])
    print('CXX = ' + os.environ['CXX'])
