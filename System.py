import platform
import File

isWindows = platform.system() == 'Windows'
isMac     = platform.system() == 'Darwin'
isLinux   = platform.system() == 'Linux'

python_cmd = 'py' if isWindows else 'python3'

def add_flag(flag):
	File.make(File.config_path() + '/' + flag)

def has_flag(flag):
	return File.exists(File.config_path() + '/' + flag)

def add_conan_flag():
	add_flag('.conan')
conan = has_flag('.conan')

def add_setup_conan_flag():
	add_flag('.conan_setup')
conan_setup = has_flag('.conan_setup')

android_ndk = File.exists(File.config_path() + '/android-ndk-r17b')
