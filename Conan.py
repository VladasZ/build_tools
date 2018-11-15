import os
import Args
import File
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
    
    print("Using: " + compiler.info())
    
    build_info_script_name = "conanbuildinfo.cmake"
    
    if Args.android:
        _run_android()
        return

    command = ['conan', 'install', '..']

    if multi:
        command += ['-g', 'cmake_multi']
        build_info_script_name = "conanbuildinfo_multi.cmake"
        
    File.write("build_info.cmake", "set(BUILD_INFO " + build_info_script_name + ")")
        
    if Args.forceBuild:
        command += ['--build']
    else:
        command += ['--build=missing']

    command += [
          '-scompiler='         + compiler.name
        , '-scompiler.version=' + compiler.conan_version()
    ]

    if not compiler.isVS():
        command += ['-scompiler.libcxx='  + compiler.libcxx]

    if multi:
        Shell.run(command + ['-s', 'build_type=Debug'])
        Shell.run(command + ['-s', 'build_type=Release']) # 
    else:
        Shell.run(command)


def _run_android():
    standalone_toolchain = Android._toolchain_path
    target_host          = 'arm-linux-androideabi'
    cc_compiler          = 'gcc'
    cxx_compiler         = 'g++'

#CONAN_CMAKE_FIND_ROOT_PATH=$standalone_toolchain/sysroot
#PATH=[$standalone_toolchain/bin]
#CHOST=$target_host
#AR=$target_host-ar
#AS=$target_host-as
#RANLIB=$target_host-ranlib
#CC=$target_host-$cc_compiler
#CXX=$target_host-$cxx_compiler
#LD=$target_host-ld
#STRIP=$target_host-strip
#CFLAGS=   -fPIE -fPIC -I$standalone_toolchain/include/c++/4.9.x
#CXXFLAGS= -fPIE -fPIC -I$standalone_toolchain/include/c++/4.9.x
#LDFLAGS= -pie

    os.environ['CONAN_CMAKE_FIND_ROOT_PATH'] = standalone_toolchain + '/sysroot'
    os.environ['PATH']    += standalone_toolchain + '/bin'
    os.environ['CHOST']    = target_host
    os.environ['AR']       = target_host + '-ar'
    os.environ['AS']       = target_host + '-as'
    os.environ['RANLIB']   = target_host + '-ranlib'
    os.environ['CC']       = target_host + '-' + cc_compiler
    os.environ['CXX']      = target_host + '-' + cxx_compiler
    os.environ['LD']       = target_host + '-ld'
    os.environ['STRIP']    = target_host + '-strip'
    os.environ['CFLAGS']   = '-fPIE -fPIC -I' + standalone_toolchain + '/include/c++/4.9.x -D__ANDROID_API__=21'
    os.environ['CXXFLAGS'] = '-fPIE -fPIC -I' + standalone_toolchain + '/include/c++/4.9.x -D__ANDROID_API__=21'
    os.environ['LDFLAGS']  = '-pie'

#    os.environ['CMAKE_C_COMPILER']   = cc_compiler
#    os.environ['CMAKE_CXX_COMPILER'] = cxx_compiler

    Shell.run([
        'conan', 'install', '..',
        '-scompiler=' + cc_compiler,
        '-scompiler.version=8.1',
        '-scompiler.libcxx=libstdc++',
        '-sos=Android',
        '-sos.api_level=21',
        '-sarch=armv7',
        '-sbuild_type=Release',
        '--build=missing'
    ])
