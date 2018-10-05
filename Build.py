import File
import Debug

cmake_file_name = "CMakeLists.txt"
cmake_search_default_depth = 3

def has_cmake_file(path = "."):
    return cmake_file_name in File.get_files(path)

def has_parent_cmake_files(depth = cmake_search_default_depth):
    path = "./.."
    for i in range(0, depth):
        if has_cmake_file(path):
            return True
        path += "/.."
    return False

def root_cmake_dir(path = '.'):
    _path = path
    while not File.is_root(_path):
        if has_parent_cmake_files(_path):
            _path += "/.."
        else:
            if has_cmake_file(_path):
                return _path
            else:
                Debug.throw("CMake root file not found")
    Debug.throw("CMake root file not found")
        
        
files = File.get_files()

print(has_cmake_file(File.home + '/dev/projects/smon'))


ports = '../../../../../../../..'

print('spesogon')

print(File.full_path(ports))

print(File.is_root(ports))

print("corogon")
print("corogon")
print("corogon")
print("corogon")
print("corogon")
