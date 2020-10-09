import iOS
import Git
import File
import Make
import Time
import Args
import Deps
import File
import Shell
import Debug
import Conan
import Cmake


def _root_dir(path='.'):
    _path = path
    while not File.is_root(_path):
        if File.exists(_path + '/.projectile'):
            return File.full_path(_path)
        else:
            return ""
        _path = _path + "/.."


root_dir = _root_dir()
project_name = File.folder_name(root_dir)
build_dir = root_dir + "/build"

stamp = Time.stamp()


def prepare():

    if Args.ios:
        iOS.setup()

    File.cd(root_dir)

    Cmake.reset_config()

    Conan.setup()
    Cmake.setup()

    File.mkdir('build')
    File.cd('build')

    root_project = Deps.string_to_dep(project_name)
    root_project.custom_path = root_dir + "/.."
    root_project.add_to_cmake()

    Cmake.setup_variables()

    Conan.run()

    if Args.build or Args.ide:
        Cmake.run()

    print("Project prepare time: " + Time.duration())

    if not Args.android:
        File.cat("./build_tools_generated.cmake")


def build():
    if not File.exists(build_dir):
        prepare()
    File.cd(build_dir)
    if Args.ios:
        Cmake.build()
    else:
        Make.run()
    print("Project build time: " + Time.duration())


def run():
    _project_name = "sand" if File.exists(build_dir + "/../source/sand") else project_name
    build()
    bin_dir = File.full_path(build_dir) + "/"

    if File.exists(bin_dir + "bin"):
        bin_dir += "bin/"

    Shell.run([bin_dir + _project_name])


def clean():
    File.rm(build_dir)
    Deps.clean()
