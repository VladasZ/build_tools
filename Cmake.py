import platform
import Shell

def default_generator():
    if platform.system() == 'Windows':
        return 'Visual Studio 15 2017 Win64'
    if platform.system()== 'Darwin':
        return 'Xcode'
    return 'Unix Makefiles'

def run(generator = default_generator()):
	Shell.run(['cmake', '..', '-G', generator])
