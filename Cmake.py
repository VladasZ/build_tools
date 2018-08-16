import platform
import Shell
import System

def default_generator():
    if System.isWindows:
        return 'Visual Studio 15 2017 Win64'
    if System.isMac:
        return 'Xcode'
    if System.isLinux:
    	return 'CodeBlocks - Unix Makefiles'

make = 'Unix Makefiles'

def run(generator = default_generator()):
	Shell.run(['cmake', '-G', generator, '..'])
