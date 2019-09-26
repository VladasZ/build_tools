import platform
import File
import Shell
import Debug

is_windows = platform.system() == 'Windows'
is_mac     = platform.system() == 'Darwin'
is_linux   = platform.system() == 'Linux'

platform = platform.system()

python_cmd = 'py'  if is_windows else 'python3'
pip_cmd    = 'pip' if is_windows else 'pip3'


def os():
    if is_linux:
        return "Linux"
    if is_mac:
        return "macOS"
    if is_windows:
        return "Windows"
    Debug.not_implemented()


def installed_packages():
    if is_linux:
        return Shell.get(['dpkg', '--list'])
    if is_mac:
        return Shell.get(['brew', 'list'])
    Debug.not_implemented()


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
