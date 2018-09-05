import os
import platform
import Args
import Shell
import System
import Compiler

make = 'Unix Makefiles'

def default_generator():
    if Args.make:
        return make
    if System.isWindows:
        return 'Visual Studio 15 2017 Win64'
    if System.isMac:
        return 'Xcode'
    if System.isLinux:
        return 'CodeBlocks - Unix Makefiles'

def run(generator = default_generator()):
    Shell.run(['cmake', '-G', generator, '..'])

def setup(compiler = Compiler.get()):

    os.environ['CC']  = compiler.name
    os.environ['CXX'] = compiler.cppname

    if compiler.isApple():
        os.environ['CC']  = 'clang'

    print('CC = '  + os.environ['CC'])
    print('CXX = ' + os.environ['CXX'])
