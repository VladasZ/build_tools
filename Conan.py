import os
import Shell

def setup():
    os.system('conan remote add bincraftes      https://api.bintray.com/conan/bincrafters/public-conan')
    os.system('conan remote add pocoproject     https://api.bintray.com/conan/pocoproject/conan')
    os.system('conan remote add conan-community https://api.bintray.com/conan/conan-community/conan')

def run():
	Shell.run(['conan', 'install', '..'])
