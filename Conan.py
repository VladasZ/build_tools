import os
import Shell
import Compiler

def setup():
    os.system('conan remote add bincraftes      https://api.bintray.com/conan/bincrafters/public-conan')
    os.system('conan remote add pocoproject     https://api.bintray.com/conan/pocoproject/conan')
    os.system('conan remote add conan-community https://api.bintray.com/conan/conan-community/conan')


#	Shell.run([
#	'conan', 'install', '..', 
#	'-scompiler=gcc', 
#	'-scompiler.version=6.3gdf', 
#	'-scompiler.libcxx=libstdc++', 
#	'-bmissing'
#	])	

def run(compiler = Compiler.default()):
	command = [
		'conan', 'install', '..', '--build=missing', 
		'-scompiler='         + compiler.name,
		'-scompiler.version=' + compiler.version
		]

	if compiler.needsLibcxx:
		command += ['-scompiler.libcxx='  + compiler.libcxx]

	Shell.run(command)
