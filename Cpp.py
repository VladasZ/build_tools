import Git
import File
import Make
import Time
import Shell
import Debug
import Conan
import Cmake

def project_name(path = "."):
    _path = path
    while not File.is_root(_path):
        if File.parent_folder(_path) == "source":
            return File.folder_name(_path)
        _path = "../" + _path
    Debug.throw("Source directory not found for path: " + File.full_path(path))

root_dir = Git.root_dir()
build_dir = root_dir + "/build"

stamp = Time.stamp()

def prepare():
    File.cd(root_dir)

    Conan.setup()
    Cmake.setup()

    File.mkdir('build')
    File.cd('build')

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
    _project_name = project_name()
    build()
    Shell.run([File.full_path(build_dir) + "/source/" + _project_name + "/" + _project_name])

def clean():
    File.rm(build_dir)
