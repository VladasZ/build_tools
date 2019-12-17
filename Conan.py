import os
import Args
import File
import Cmake
import Shell
import Debug
import System
import Android
import Compiler


def _conanfile():
    file = "conanfile.txt"
    return "../" + file


def _conan_deps():
    file = "conan.txt"
    return "../" + file


def _needs_conan():
    if Args.no_conan:
        return False
    return File.exists(_conan_deps())


def _create_conanfile():

    File.rm(_conanfile())

    File.append(_conanfile(), "# GENERATED FILE. DO NOT EDIT\n")
    File.append(_conanfile(), "# Edit conan.txt instead\n")
    File.append(_conanfile(), "\n[requires]\n")

    versions = {
        "poco"     : "Poco/1.9.0@pocoproject/stable",
        "sqlite"   : "sqlite3/3.29.0@bincrafters/stable",
        "glfw"     : "glfw/3.2.1.20180327@bincrafters/stable",
        "glew"     : "glew/2.1.0@bincrafters/stable",
        "freetype" : "freetype/2.10.0@bincrafters/stable",
        "assimp"   : "Assimp/4.1.0@jacmoe/stable",
        "box2d"    : "box2d/2.3.1@conan/stable",
        "glm"      : "glm/0.9.9.5@g-truc/stable",
        "soil"     : "soil2/1.11@bincrafters/stable"
    }

    desktop_only = ["glfw", "glew"]

    darwin = "darwin-toolchain/1.0.5@theodelrieu/stable"
    ndk = "android_ndk_installer/r20@bincrafters/stable"

    for lib in File.get_lines(_conan_deps()):
        
        if Args.mobile:
            if lib in desktop_only:
                continue

        if Args.no_freetype and lib == "freetype":
            continue

        if Args.no_assimp and lib == "assimp":
            continue

        if Args.no_box2d and lib == "box2d":
            continue

        if Args.no_soil and lib == "soil":
            continue

        File.append(_conanfile(), versions[lib] + "\n")

    if Args.ios:
        File.append(_conanfile(), darwin + "\n")

    if Args.android:
        File.append(_conanfile(), ndk + "\n")

    File.append(_conanfile(), "\n[generators]\n")
    File.append(_conanfile(), "cmake")


def setup():

    if Args.no_conan:
        return

    if System.conan:
        print('conan OK')
    else:
        Shell.run([System.pip_cmd, 'install', 'conan'])
        System.add_conan_flag()

    if System.conan_setup and False:  # FIX THIS
        print('conan remotes OK')
    else:
        os.system('conan remote add bincraftes      https://api.bintray.com/conan/bincrafters/public-conan')
        os.system('conan remote add pocoproject     https://api.bintray.com/conan/pocoproject/conan')
        os.system('conan remote add conan-community https://api.bintray.com/conan/conan-community/conan')
        System.add_setup_conan_flag()


def run(compiler=Compiler.get()):

    build_info_script_name = "conanbuildinfo.cmake"

    if not _needs_conan():
        Cmake.add_var("BUILD_INFO", build_info_script_name)
        Cmake.add_bool("NEEDS_CONAN", False)
        return

    Cmake.add_bool("NEEDS_CONAN", True)

    _create_conanfile()

    command = ['conan', 'install', '..']

    if Args.multi:
        command += ['-g', 'cmake_multi']
        build_info_script_name = "conanbuildinfo_multi.cmake"

    Cmake.add_var("CONAN_BUILD_INFO", "build/" + build_info_script_name)
    Cmake.add_line("include(${CONAN_BUILD_INFO})")

    command += [
          '-scompiler='         + compiler.conan_name
        , '-scompiler.version=' + "8" if Args.android else compiler.conan_version
    ]

    if Args.ios:
        arch = 'armv8' if Args.device else 'x86_64'
        command += [
              '-sos=iOS'
            , '-sos.version=' + Args.ios_version
            , '-sarch=' + arch
            , '-o', 'darwin-toolchain:bitcode=False'
        ]
    elif Args.android:
        command += [
              '-sos=Android'
            , '-sos.api_level=21'
        ]

    if not (Args.ide and System.is_windows):
        command += ['-scompiler.libcxx=' + compiler.libcxx]

    command += ['--build=missing']

    if Args.ios:
        Shell.run(command)
        return

    if Args.multi:
        Shell.run(command + ['-s', 'build_type=Debug'])
        Shell.run(command + ['-s', 'build_type=Release'])
    elif Args.debug:
        Shell.run(command + ['-s', 'build_type=Debug'])
    elif Args.release:
        Shell.run(command + ['-s', 'build_type=Release'])
    else:
        Shell.run(command)
