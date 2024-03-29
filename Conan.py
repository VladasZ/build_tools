import os
import Args
import File
import Cmake
import Shell
import Debug
import Paths
import System
import Compiler

subdeps = []


def _conanfile():
    file = "conanfile.txt"
    return "../" + file


def _conan_deps():
    file = "conan.txt"
    return "../" + file


def _needs_conan():
    if Args.no_conan:
        return False
    if subdeps:
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
        "gl"         : "opengl/system",
        "qt"         : "qt/5.14.2@bincrafters/stable",
        "glm"        : "glm/0.9.9.8",
        "date"       : "date/2.4.1",
        "mesa"       : "mesa/20.0.1@bincrafters/stable",
        "glew"       : "glew/2.1.0",
        "glfw"       : "glfw/3.3.2",
        "json"       : "nlohmann_json/3.9.1",
        "poco"       : "poco/1.9.4",
        "boost"      : "boost/1.76.0",
        "openvr"     : "openvr/1.12.5",
        "frozen"     : "frozen/1.0.0",
        "sqlite"     : "sqlitecpp/3.1.1",
        "bullet"     : "bullet3/3.07",
        "box2d"      : "box2d/2.4.0",
        "assimp"     : "assimp/5.0.1",
        "freetype"   : "freetype/2.10.4",
        "magic_enum" : "magic_enum/0.7.2"
    }

    desktop_only = ["glfw", "glew"]

    deps = set()

    if File.exists(_conan_deps()):
        deps.update(File.get_lines(_conan_deps()))

    deps.update(subdeps)

    processed = []

    if Args.no_freetype:
        deps.remove("freetype")

    if Args.no_assimp:
        deps.remove("assimp")

    if Args.no_box2d:
        deps.remove("box2d")

    if Args.no_bull3:
        deps.remove("bullet")

    if Args.no_boost:
        deps.remove("boost")

    if Args.no_date:
        deps.remove("date")
        
    if Args.no_glm:
        deps.remove("glm")

    if Args.no_qt:
        deps.remove("qt")

    if Args.no_menum:
        deps.remove("magic_enum")

    for lib in deps:

        if lib not in versions:
            Debug.throw("Conan library named: \"" + lib + "\" not found.")

        if lib in processed:
            continue

        processed += [lib]

        if Args.mobile:
            if lib in desktop_only:
                continue

        File.append(_conanfile(), versions[lib] + "\n")

    File.append(_conanfile(), "\n[generators]\n")
    File.append(_conanfile(), "cmake\n")

    File.append(_conanfile(), "\n[options]\n")

    if "freetype" in deps:
        File.append(_conanfile(), "freetype:with_png=False\n\n")

    if "mesa" in deps:
        File.append(_conanfile(), "mesa:dri_search_path=/usr/lib/x86_64-linux-gnu/dri\n\n")

    if Args.boost_python:
        File.append(_conanfile(), "boost:without_python=False\n\n")

    if "poco" in deps:
        File.append(_conanfile(), "poco:enable_data_sqlite=False\n")
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

    if "boost" in deps:
        if Args.mobile:
            File.append(_conanfile(), "boost:without_stacktrace=True\n")
            File.append(_conanfile(), "boost:without_locale=True\n")
            File.append(_conanfile(), "boost:without_log=True\n\n")



def add_requires(file_path):
    global subdeps
    deps = File.get_lines(file_path)
    for dep in deps:
        if dep not in subdeps:
            subdeps += [dep]


def setup():

    if Args.no_conan:
        return

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

    if _simple_conanfile() or subdeps:
        _create_conanfile()

    command = ['conan', 'install', '..']

    if Args.multi:
        command += ['-g', 'cmake_multi']
        build_info_script_name = "conanbuildinfo_multi.cmake"

    Cmake.add_var("CONAN_BUILD_INFO", File.full_path(".") + "/" + build_info_script_name)
    Cmake.add_line("include(${CONAN_BUILD_INFO})")

    if not Args.mobile and not System.is_windows:
        command += [
              '-scompiler='         + compiler.conan_name
            , '-scompiler.version=' + ("8" if Args.android else compiler.conan_version)
        ]

    if System.is_windows:
        if Args.vs15:
            command += ["-scompiler.version=14"]
        if Args.vs17:
            command += ["-scompiler.version=15"]
        if Args.vs19:
            command += ["-scompiler.version=16"]


    if Args.pi:
        command += [
            '-sos=Linux'
            , '-sarch=armv7'
        ]

    if Args.mingw:
        command += ['--profile', Paths.deps + '/build_tools/conan_profiles/mingw']

    if Args.msvc:
        command += ['--profile', Paths.deps + '/build_tools/conan_profiles/msvc']

    if Args.cygwin:
        command += ['--profile', Paths.deps + '/build_tools/conan_profiles/cygwin']

    if Args.msys:
        command += ['--profile', Paths.deps + '/build_tools/conan_profiles/msys']

    if Args.ios:
        if Args.device:
            command += ['--profile', Paths.deps + '/build_tools/conan_profiles/ios']
        else:
            command += ['--profile', Paths.deps + '/build_tools/conan_profiles/ios_simulator']

    if Args.android:
        if System.is_linux:
            command += ['--profile', Paths.deps + '/build_tools/conan_profiles/linux_android']
        elif System.is_mac:
            command += ['--profile', Paths.deps + '/build_tools/conan_profiles/mac_android']
        else:
            Debug.throw("No android build support on Windows yet.")

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
