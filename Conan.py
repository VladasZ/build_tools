import os
import Args
import Shell
import Compiler

def setup():
    os.system('conan remote add bincraftes      https://api.bintray.com/conan/bincrafters/public-conan')
    os.system('conan remote add pocoproject     https://api.bintray.com/conan/pocoproject/conan')
    os.system('conan remote add conan-community https://api.bintray.com/conan/conan-community/conan')

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
