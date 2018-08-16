import System

class Compiler(object):
	def __init__(self, name, version, libcxx = '', needsLibcxx = True):
		self.name        = name
		self.version     = version
		self.libcxx      = libcxx
		self.needsLibcxx = needsLibcxx
		

visualStudio = Compiler('Visual Studio', '15',       needsLibcxx = False)
gcc          = Compiler('gcc',           '8.1',     'libstdc++')
clang        = Compiler('clang',         '6.0',     'libstdc++')
appleClang   = Compiler('apple-clang',   'ospokol', 'spialgok')

def default():
	if System.isWindows:
		return visualStudio
	if System.isMac:
		return appleClang
	if System.isLinux:
		return clang
