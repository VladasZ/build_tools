import File
import Debug

def root_dir(path = '.'):
    _path = path
    while not File.is_root(_path):
        if File.exists(_path + '/.git'):
            return File.full_path(_path)
        _path = _path + "/.."
    Debug.throw("Conan root directory not found for path: " + File.full_path(path))
