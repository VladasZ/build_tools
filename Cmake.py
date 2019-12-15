import os
import iOS
import File
import Args
import Debug
import Shell
import System
import Compiler

cmake_file_name = "CMakeLists.txt"
cmake_search_default_depth = 3

def cmake_config_file_name():
    name = "build_tools_generated.cmake"
    if Args.android:
        return "android/app/src/main/cpp/" + name
    return name


def has_cmake_file(path="."):
    return cmake_file_name in File.get_files(path)


def has_parent_cmake_files(path=".", depth=cmake_search_default_depth):
    _path = path + "/.."
    for i in range(0, depth):
        if has_cmake_file(_path):
            return True
        _path += "/.."
    return False


def root_dir(path='.'):
    _path = path
    print(_path)
    while not File.is_root(_path):
        if has_cmake_file(_path):
            if not has_parent_cmake_files(_path):
                return File.full_path(_path)
        _path += "/.."
    Debug.throw("CMake root directory not found for path: " + File.full_path(path))


def default_generator():
    if Args.ios:
        return 'Xcode'
    if not Args.ide:
        if System.is_windows:
            return 'MinGW Makefiles'
        return 'Unix Makefiles'
    if System.is_windows:
        if Args.vs19:
            return 'Visual Studio 16 2019'
        else:    
            return 'Visual Studio 15 2017 Win64'
    if System.is_mac:
        return 'Xcode'
    if System.is_linux:
        return 'CodeBlocks - Unix Makefiles'


def run(generator=default_generator()):

    if Args.android:
        return

    args = ["cmake", "..", "-G", generator]

    args += ["-DCMAKE_BUILD_TYPE=Debug" if Args.debug else "-DCMAKE_BUILD_TYPE=Release"]

    if Args.ios:
        platform = "SIMULATOR64"

        if Args.device:
            if Args.x32:
                platform = "OS"
            else:
                platform = "OS64"

        args += ["-DCMAKE_TOOLCHAIN_FILE=" + iOS.toolchain_file]
        args += ["-DPLATFORM=" + platform]
        args += ["-DDEPLOYMENT_TARGET=" + Args.ios_version] 

    Shell.run(args)


def setup(compiler=Compiler.get()):

    if Args.ide or Args.android:
        return

    Debug.info(compiler)
    Debug.info(compiler.CXX)

    os.environ['CC'] = Shell.which(compiler.CC)
    os.environ['CXX'] = Shell.which(compiler.CXX)

    Debug.info('CC = ' + os.environ['CC'])
    Debug.info('CXX = ' + os.environ['CXX'])


def build():
    Shell.run(["cmake", "--build", "."])


def _append(value):
    File.append(cmake_config_file_name(), value)


def reset_config():
    File.rm(cmake_config_file_name())
    File.append(cmake_config_file_name(), "# GENERATED FILE. DO NOT EDIT\n")


def add_var(name, value):
    _append("set(" + name + " " + File.convert_path(value) + ")\n")


def add_bool(name, value):
    _append("set(" + name + " " + ("YES" if value else "NO") + ")\n")


def append_var(name, value):
    _append("set(" + name + " ${" + name + "} " + File.convert_path(value) + ")\n")


def add_definition(definition):
    _append("add_definitions(-D" + definition + ")\n")

def add_def_and_bool(definition, value):
    add_bool(definition, value)
    if value:
        add_definition(definition)

def add_line(line):
    _append(line + "\n")

def setup_variables():

    add_var("CMAKE_UTILS_PATH", "~/.deps/build_tools/utils.cmake")

    add_var("CMAKE_CXX_STANDARD", str(Args.cpp_standart))

    add_def_and_bool("DESKTOP_BUILD", Args.desktop_build)
    add_def_and_bool("IOS_BUILD",     Args.ios)
    add_def_and_bool("ANDROID_BUILD", Args.android)
    add_def_and_bool("NEEDS_SIGNING", Args.needs_signing)
    add_def_and_bool("CPP11_BUILD",   Args.cpp11)
    add_def_and_bool("CPP14_BUILD",   Args.cpp14)
    add_def_and_bool("CPP17_BUILD",   Args.cpp17)

    if Args.desktop_build:
        add_def_and_bool("MAC_BUILD",     System.is_mac)
        add_def_and_bool("WINDOWS_BUILD", System.is_windows)
        add_def_and_bool("LINUX_BUILD",   System.is_linux)
    else:
        add_def_and_bool("IPHONE_4S_BUILD",  Args._4s)
        add_def_and_bool("IPHONE_3GS_BUILD", Args._3gs)

    if Args.no_freetype:
        add_definition("NO_FREETYPE")

    if Args.no_assimp:
        add_definition("NO_ASSIMP")

    if Args.no_box2d:
        add_definition("NO_BOX2D")

    if Args.no_soil:
        add_definition("NO_SOIL")

    if Args.debug:
        add_definition("DEBUG")

    add_line("include(${CMAKE_UTILS_PATH})")
