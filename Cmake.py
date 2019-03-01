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
cmake_config_file_name = "build_info.cmake"
cmake_search_default_depth = 3  # 

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
    if Args.debug:
        Shell.run(["cmake", "-G", generator, "-DCMAKE_BUILD_TYPE=Debug", ".."]) 
    elif Args.release:
        Shell.run(["cmake", "-G", generator, "-DCMAKE_BUILD_TYPE=Release", ".."]) 
    else:
        Shell.run(["cmake", "-G", generator, ".."])

def setup(compiler = Compiler.get()):

    if Args.ide and System.is_windows:
        return
    
    os.environ['CC']  = Shell.which(compiler.CC)
    os.environ['CXX'] = Shell.which(compiler.CXX)
    
    Debug.info('CC = '  + os.environ['CC'])
    Debug.info('CXX = ' + os.environ['CXX'])

def _append(value):
    File.append(cmake_config_file_name, value)    
          
def reset_config():
    File.rm(cmake_config_file_name)
    File.append(cmake_config_file_name, "# GENERATED FILE. DO NOT EDIT\n")    

def add_var(name, value):
    _append("set(" + name + " " + File.convert_path(value) + ")\n")  

def add_bool(name, value):
    _append("set(" + name + " " + ("YES" if value else "NO") + ")\n")  

def append_var(name, value):
    _append("set(" + name + " ${" + name + "} " + File.convert_path(value) + ")\n")
    
