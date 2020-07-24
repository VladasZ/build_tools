import os
import Args
import File
import Cmake
import Shell
import Debug
import Paths
import System
import Compiler

requires = []


def _conanfile():
    file = "conanfile.txt"
    return "../" + file


def _conan_deps():
    file = "conan.txt"
    return "../" + file


def _needs_conan():
    if Args.no_conan:
        return False
    if requires:
        return True
    return File.exists(_conan_deps()) or File.exists(_conanfile())


def _simple_conanfile():
    return File.exists(_conan_deps())


def _create_conanfile():

    File.rm(_conanfile())

    File.append(_conanfile(), "# GENERATED FILE. DO NOT EDIT\n")
    File.append(_conanfile(), "# Edit conan.txt instead\n")
    File.append(_conanfile(), "\n[requires]\n")

    versions = {
        "gl"       : "opengl/system",
        "qt"       : "qt/5.14.2@bincrafters/stable",
        "glm"      : "glm/0.9.9.8",
        "date"     : "date/2.4.1",
        "mesa"     : "mesa/20.0.1@bincrafters/stable",
        "glew"     : "glew/2.1.0@bincrafters/stable",
        "glfw"     : "glfw/3.3.2@bincrafters/stable",
        "soil"     : "soil2/1.11@bincrafters/stable",
        "json"     : "nlohmann_json/3.8.0",
        "poco"     : "poco/1.10.1",
        "boost"    : "boost/1.73.0",
        "sqlite"   : "sqlitecpp/2.5.0",
        "bullet"   : "bullet3/2.89",
        "box2d"    : "box2d/2.3.1",
        "assimp"   : "assimp/5.0.1",
        "freetype" : "freetype/2.10.2",
    }

    desktop_only = ["glfw", "glew"]

    deps = []

    if File.exists(_conan_deps()):
        deps += File.get_lines(_conan_deps())

    deps += requires

    processed = []

    if System.is_mac:
        File.append(_conanfile(), "libiconv/1.16\n")

    if System.is_linux and "glew" in deps:
        deps += ["gl"]
        deps += ["mesa"]

    for lib in deps:

        if not lib in versions:
            Debug.throw("Conan library named: \"" + lib + "\" not found.")

        if lib in processed:
            continue

        processed += [lib]

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

        if Args.no_bull3 and lib == "bullet":
            continue

        if Args.no_qt and lib == "qt":
            continue

        File.append(_conanfile(), versions[lib] + "\n")

    File.append(_conanfile(), "\n[generators]\n")
    File.append(_conanfile(), "cmake\n")

    File.append(_conanfile(), "\n[options]\n")

    if "mesa" in deps:
        File.append(_conanfile(), "mesa:dri_search_path=/usr/lib/x86_64-linux-gnu/dri\n\n")

    # if "boost" in deps:
    #     File.append(_conanfile(), "boost:without_python=False\n\n")

    if "poco" in deps:
        File.append(_conanfile(), "poco:enable_data_sqlite=False\n")
        File.append(_conanfile(), "poco:cxx_14=True\n")
        File.append(_conanfile(), "poco:enable_mongodb=False\n\n")

    if "qt" in deps:

        File.append(_conanfile(), "qt:with_sqlite3=False\n")
        File.append(_conanfile(), "qt:with_mysql=False\n")
        File.append(_conanfile(), "qt:with_glib=False\n")
        File.append(_conanfile(), "qt:with_freetype=False\n")
        File.append(_conanfile(), "qt:with_fontconfig=False\n")
        File.append(_conanfile(), "qt:with_harfbuzz=False\n")
        File.append(_conanfile(), "qt:opengl=no\n")
        File.append(_conanfile(), "qt:shared=False\n\n")

        File.append(_conanfile(), "qt:qtsensors=True\n")
        File.append(_conanfile(), "qt:qtserialbus=True\n")
        File.append(_conanfile(), "qt:qtserialport=True\n\n")

        File.append(_conanfile(), "qt:qtconnectivity=True\n\n")


def add_requires(file_path):
    global requires
    deps = File.get_lines(file_path)
    requires += deps


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

    if _simple_conanfile() or requires:
        _create_conanfile()

    command = ['conan', 'install', '..']

    if Args.multi:
        command += ['-g', 'cmake_multi']
        build_info_script_name = "conanbuildinfo_multi.cmake"

    Cmake.add_var("CONAN_BUILD_INFO", "build/" + build_info_script_name)
    Cmake.add_line("include(${CONAN_BUILD_INFO})")

    if not Args.mobile and not System.is_windows:
        command += [
            '-scompiler='         + compiler.conan_name
            , '-scompiler.version=' + ("8" if Args.android else compiler.conan_version)
        ]


    if Args.pi:
        command += [
            '-sos=Linux'
            , '-sarch=armv7'
        ]

    if Args.mingw:
        command += ['--profile', Paths.deps + '/build_tools/conan_profiles/mingw']

    if Args.ios:
        command += ['--profile', Paths.deps + '/build_tools/conan_profiles/ios']

    if Args.android:
        command += ['--profile', Paths.deps + '/build_tools/conan_profiles/android']

    if System.is_mac and not Args.mobile:
        command += ['-scompiler.libcxx=' + compiler.libcxx]

    if Args.force_build:
        command += ['--build']
    else:
        command += ['--build=missing']

    if Args.ios:
        Shell.run(command)
        return

    if Args.multi:
        Shell.run(command + ['-s', 'build_type=Debug'])
        Shell.run(command + ['-s', 'build_type=Release'])
    elif Args.release:
        Shell.run(command + ['-s', 'build_type=Release'])
    elif Args.debug:
        Shell.run(command + ['-s', 'build_type=Debug'])
    else:
        Shell.run(command)
