import platform
import Args
import Shell
import System

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
	Shell.run(['cmake', '-G', generator, 
		'-D', 'CMAKE_C_COMPILER=clang', 
		'-D', 'CMAKE_CXX_COMPILER=clang++', 
		'..'])


#	-D CMAKE_CXX_COMPILER_ID=Clang',
