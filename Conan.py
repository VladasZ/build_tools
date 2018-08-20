import os
import Args
import Shell
import System
import Compiler

def setup():

	if System.conan:
		print('conan OK')
	else:
		Shell.run(['pip', 'install', 'conan'])
		System.add_conan_flag()

	if System.conan_setup:
		print('conan setup OK')
	else:
		os.system('conan remote add bincraftes      https://api.bintray.com/conan/bincrafters/public-conan')
		os.system('conan remote add pocoproject     https://api.bintray.com/conan/pocoproject/conan')
		os.system('conan remote add conan-community https://api.bintray.com/conan/conan-community/conan')
		System.add_setup_conan_flag()

def run(compiler = Compiler.get()):

	command = ['conan', 'install', '..']

	if Args.forceBuild:
		command += ['--build']
	else:
		command += ['--build=missing']

	command += [
		  '-scompiler='         + compiler.name
		, '-scompiler.version=' + compiler.version
	]

	if not compiler.isVS():
		command += ['-scompiler.libcxx='  + compiler.libcxx]

	Shell.run(command)
