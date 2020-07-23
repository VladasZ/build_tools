import os
import iOS
import File
import Args
import Debug
import Shell
import System
import Compiler
from inspect import getframeinfo, stack
from pprint import pprint

cmake_file_name = "CMakeLists.txt"
cmake_search_default_depth = 3


def cmake_config_file_name():
    name = "build_tools_generated.cmake"
    if Args.android:
        return "../android/app/src/main/cpp/" + name
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

    args += ["-DCMAKE_BUILD_TYPE=Release" if Args.release else "-DCMAKE_BUILD_TYPE=Debug"]

    if Args.ios:
        platform = "OS64COMBINED"

        if Args.device:
            platform = "OS64"

        args += ["-DCMAKE_TOOLCHAIN_FILE=" + iOS.toolchain_file]
        args += ["-DPLATFORM=" + platform]
        args += ["-DDEPLOYMENT_TARGET=" + Args.ios_version]

        if Args.no_bitcode:
            args += ["-DENABLE_BITCODE=FALSE"]

    Shell.run(args)


def setup(compiler=Compiler.get()):

    if Args.ide:
        return

    Debug.info(compiler)
    Debug.info(compiler.CXX)
    #
    # if Args.android:
    #     os.environ['CC']  = "/Users/vladas/Library/Android/sdk/ndk/20.1.5948944/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang"
    #     os.environ['CXX'] = "/Users/vladas/Library/Android/sdk/ndk/20.1.5948944/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang++"
    # else if not System.is:
    #     os.environ['CC']  = Shell.which(compiler.CC)
    #     os.environ['CXX'] = Shell.which(compiler.CXX)
    #
    # Debug.info('CC = ' + os.environ['CC'])
    # Debug.info('CXX = ' + os.environ['CXX'])


def build():
    Shell.run(["cmake", "--build", "."])


def _append(value):
    File.append(cmake_config_file_name(), value)


def reset_config():
    File.rm(cmake_config_file_name())
    File.append(cmake_config_file_name(), "# GENERATED FILE.\n# DO NOT EDIT\n")


def add_var(name, value):
    caller = getframeinfo(stack()[1][0])
    _append("set(" + name + " " + File.convert_path(value) + ")" +
            " #[" + os.path.basename(caller.filename) + " - " + str(caller.lineno) + "]\n")


def add_bool(name, value):
    caller = getframeinfo(stack()[1][0])
    _append("set(" + name + " " + ("YES" if value else "NO") + ")" +
            " #[" + os.path.basename(caller.filename) + " - " + str(caller.lineno) + "]\n")


def append_var(name, value):
    caller = getframeinfo(stack()[1][0])
    _append("set(" + name + " ${" + name + "} " + File.convert_path(value) + ")" +
            " #[" + os.path.basename(caller.filename) + " - " + str(caller.lineno) + "]\n")


def add_definition(definition):
    caller = getframeinfo(stack()[1][0])
    _append("add_definitions(-D" + definition + ")" +
            " #[" + os.path.basename(caller.filename) + " - " + str(caller.lineno) + "]\n")


def add_def_and_bool(definition, value):
    # caller = getframeinfo(stack()[1][0])
    # _append("#[" + os.path.basename(caller.filename) + " - " + str(caller.lineno) + "]\n")
    add_bool(definition, value)
    if value:
        add_definition(definition)


def add_line(line):
    caller = getframeinfo(stack()[1][0])
    _append(line + "" +
        " #[" + os.path.basename(caller.filename) + " - " + str(caller.lineno) + "]\n")


def setup_variables():

    project_name = File.folder_name("..")

    add_var(project_name+ "_PATH", File.full_path(".."))

    add_def_and_bool("RASPBERRY_BUILD",   Args.pi)
    add_def_and_bool("UNITY_BUILD",       Args.unity)
    add_def_and_bool("DESKTOP_BUILD",     Args.desktop_build)
    add_def_and_bool("IOS_BUILD",         Args.ios)
    add_def_and_bool("ANDROID_BUILD",     Args.android)
    add_def_and_bool("NO_IOS_EXE",        Args.no_ios_exe)
    add_def_and_bool("NEEDS_IOS_EXE", not Args.no_ios_exe)

    add_def_and_bool("MAC_BUILD",     System.is_mac     and Args.desktop_build)
    add_def_and_bool("WINDOWS_BUILD", System.is_windows and Args.desktop_build)
    add_def_and_bool("LINUX_BUILD",   System.is_linux   and Args.desktop_build)

    if not Args.mobile:
        add_def_and_bool("IPHONE_4S_BUILD",  Args._4s)
        add_def_and_bool("IPHONE_3GS_BUILD", Args._3gs)

    add_def_and_bool("USING_FREETYPE", not Args.no_freetype)
    add_def_and_bool("USING_ASSIMP",   not Args.no_assimp)
    add_def_and_bool("USING_BOX2D",    not Args.no_box2d)
    add_def_and_bool("USING_BULLET3D", not Args.no_bull3)
    add_def_and_bool("USING_SOIL",     not Args.no_soil)
    add_def_and_bool("USING_GLM",      not Args.no_glm)
    add_def_and_bool("USING_QT",       not Args.no_qt)

    add_def_and_bool("DEBUG", Args.debug)

    add_line("include(~/.deps/build_tools/utils.cmake)")
