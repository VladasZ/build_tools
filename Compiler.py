import Args
import Shell
import System

class Compiler(object):
	def __init__(self, name = '', cppname = '', version = '', libcxx = 'libstdc++'):
		self.name        = name
		self.cppname     = cppname
		self.version     = version
		self.libcxx      = libcxx

	def isVS(self):
		return self.name == 'Visual Studio'

	def isApple(self):
		return self.name == 'apple-clang'

gcc_version = Shell.get(['gcc', '-dumpversion'])[:3]

visualStudio = Compiler('Visual Studio', '15'                   )
gcc          = Compiler('gcc',           'g++',      gcc_version)
clang        = Compiler('clang',         'clang++',  '6.0'      )
appleClang   = Compiler('apple-clang',   'clang++',  '9.1'      )

def default():
	if System.isWindows:
		if Args.make:
			return gcc
		return visualStudio
	if System.isMac:
		return appleClang
	if System.isLinux:
		return gcc

def get():
	if Args.clang:
		if System.isMac:
			return appleClang
		return clang
	if Args.gcc:
		return gcc
	return default()
