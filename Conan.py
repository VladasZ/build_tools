import os
import Args
import File
import Cmake
import Shell
import Debug
import System
import Android
import Compiler

def root_dir(path = '.'):
    _path = path
    while not File.is_root(_path):
        if File.exists(_path + '/conanfile.txt'):
            return File.full_path(_path)
        _path = _path + "/.."
    Debug.throw("Conan root directory not found for path: " + File.full_path(path))

def setup():

    if Args.no_conan:
        return

    if System.conan:
        print('conan OK')
    else:
        Shell.run([System.pip_cmd, 'install', 'conan'])
        System.add_conan_flag()

    if System.conan_setup and False: #FIX THIS
        print('conan remotes OK')
    else:
        os.system('conan remote add bincraftes      https://api.bintray.com/conan/bincrafters/public-conan')
        os.system('conan remote add pocoproject     https://api.bintray.com/conan/pocoproject/conan')
        os.system('conan remote add conan-community https://api.bintray.com/conan/conan-community/conan')
        System.add_setup_conan_flag()

def run(compiler = Compiler.get(), multi = Args.multi):

    build_info_script_name = "conanbuildinfo.cmake"

    if Args.no_conan:
        Cmake.add_var("BUILD_INFO", build_info_script_name)
        return
    
    print("Using: " + str(compiler))

    conanfile_name = "../conanfile.txt"
    mobile_name = "../conanfile_mobile.txt"
    desktop_name = "../conanfile_desktop.txt"

    has_conanfile = File.exists(conanfile_name)
    has_platforms = File.exists(mobile_name) or File.exists(desktop_name)

    needed = has_conanfile or has_platforms

    if not needed:
        return

    if has_platforms:
        File.rm(conanfile_name)
        target_name = desktop_name if Args.desktop_build else mobile_name
        File.copy(target_name, "./" + conanfile_name)
        
    command = ['conan', 'install', '..']

    if multi:
        command += ['-g', 'cmake_multi']
        build_info_script_name = "conanbuildinfo_multi.cmake"

    Cmake.add_var("BUILD_INFO", build_info_script_name)
    
    if Args.ios:
        arch = 'armv8' if Args.device else 'x86_64'
        command += [
              '-sos=iOS'
            , '-sos.version=9.0'
            , '-sarch=' + arch
        ]
    else:
        command += [
              '-scompiler='         + compiler.conan_name
            , '-scompiler.version=' + compiler.conan_version
        ]
        
        if not (Args.ide and System.is_windows):
            command += ['-scompiler.libcxx='  + compiler.libcxx]

    command += ['--build=missing']

    if Args.ios:
        Shell.run(command)
        return
            
    if multi:
        Shell.run(command + ['-s', 'build_type=Debug'])
        Shell.run(command + ['-s', 'build_type=Release'])
    elif Args.debug:
        Shell.run(command + ['-s', 'build_type=Debug'])
    elif Args.release:
        Shell.run(command + ['-s', 'build_type=Release'])
    else:
        Shell.run(command)
