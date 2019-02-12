import Git
import File
import Make
import Time
import Args
import File
import Shell
import Debug
import Conan
import Cmake

def _root_dir(path = '.'):
    _path = path
    while not File.is_root(_path):
        if File.exists(_path + '/.projectile'):
            return File.full_path(_path)
        _path = _path + "/.."
    Debug.throw("C++ project root directory not found for path: " + File.full_path(path))

root_dir = _root_dir()
project_name     = File.folder_name(root_dir)
needs_conan      = File.exists(root_dir + "/conanfile.txt")
has_dependencies = File.exists(root_dir + "/dependencies.txt")
build_dir = root_dir + "/build"

stamp = Time.stamp()

def prepare():
    File.cd(root_dir)

    if needs_conan:
        Conan.setup()
    Cmake.setup()

    File.mkdir('build')
    File.cd('build')

    build_script_path = "build_tools/utils.cmake"

    Cmake.reset_config()
    Cmake.add_var("BUILD_SCRIPT_PATH", build_script_path)
        
    if needs_conan:
        Conan.run()
    Cmake.run()
    print("Project prepare time: " + Time.duration())
    
def build():
    if not File.exists(build_dir):
        prepare()
    File.cd(build_dir)
    Make.run()    
    print("Project build time: " + Time.duration())

def run():
    _project_name = "sand" if Args.test else project_name
    build()
    bin_dir = File.full_path(build_dir) + "/"

    if File.exists(bin_dir + "bin"):
        bin_dir += "bin/"
    
    Shell.run([bin_dir + _project_name])

def clean():
    File.rm(build_dir)

print(File.exists("~/"))
