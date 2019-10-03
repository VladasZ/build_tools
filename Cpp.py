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
import Android


def _root_dir(path='.'):
    _path = path
    while not File.is_root(_path):
        if File.exists(_path + '/.projectile'):
            return File.full_path(_path)
        _path = _path + "/.."
    Debug.throw("C++ project root directory not found for path: " + File.full_path(path))


root_dir = _root_dir()
project_name = File.folder_name(root_dir)
has_dependencies = File.exists(root_dir + "/deps.txt")
build_dir = root_dir + "/build"

stamp = Time.stamp()


def prepare():
    if Args.ios:
        iOS.setup()

    if Args.android:
        Android.setup()

    File.cd(root_dir)

    Conan.setup()
    Cmake.setup()

    File.mkdir('build')
    File.cd('build')

    Cmake.reset_config()

    if has_dependencies:
        Deps.install()

    Cmake.add_var(project_name.replace("-", "_") + "_path",
                  "\"" + File.full_path("..") + "\"")

    Cmake.add_var("CMAKE_UTILS_PATH", "~/.deps/build_tools/utils.cmake")

    Cmake.add_bool("DESKTOP_BUILD", Args.desktop_build)
    Cmake.add_bool("IOS_BUILD", Args.ios)
    Cmake.add_bool("ANDROID_BUILD", Args.android)
    Cmake.add_bool("NEEDS_SIGNING", Args.device and Args.build)

    Cmake.add_bool("NO_FREETYPE", Args.no_freetype)

    if Args.no_freetype:
        Cmake.add_definition("NO_FREETYPE")


    Conan.run()

    Cmake.run()

    print("Project prepare time: " + Time.duration())


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
