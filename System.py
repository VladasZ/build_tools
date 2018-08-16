import platform

def isWindows():
	return platform.system() == 'Windows'

def isMac():
	return platform.system()== 'Darwin'
