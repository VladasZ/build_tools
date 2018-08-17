import Args
import System

class Compiler(object):
	def __init__(self, name = '', version = '', libcxx = '', needsLibcxx = True, auto = False):
		self.name        = name
		self.version     = version
		self.libcxx      = libcxx
		self.needsLibcxx = needsLibcxx
		self.auto        = auto
		

visualStudio = Compiler('Visual Studio', '15',   needsLibcxx = False) 
gcc          = Compiler('gcc',           '7.3', 'libstdc++') 
clang        = Compiler('clang',         '6.0', 'libstdc++') 
appleClang   = Compiler('apple-clang',   '9.1', 'libstdc++') 
auto         = Compiler(auto = True)

def default():
	if System.isWindows:
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
