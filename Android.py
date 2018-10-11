import File
import Shell
import System

_arch = 'arm'
_api  = '21'
_toolchain_name = _arch + '_' + _api + '_toolchain'
_toolchain_path = File.config_path() + '/' + _toolchain_name

__ndk_zip_path = File.config_path() + '/android_NDK.zip'

ndk_path =  File.config_path() + '/android-ndk-r17b'

def NDKLink():
    if System.is_windows:
        return 'https://dl.google.com/android/repository/android-ndk-r17b-windows-x86_64.zip'
    if System.is_mac:
        return 'https://dl.google.com/android/repository/android-ndk-r17b-darwin-x86_64.zip'
    if System.is_linux:
        return 'https://dl.google.com/android/repository/android-ndk-r17b-linux-x86_64.zip'

def downloadNDK():
    if File.exists(__ndk_zip_path):
        print('NDK zip OK')
        return
    File.download(NDKLink(), File.config_path() + '/android_NDK.zip')

def unzipNDK():
    if File.exists(ndk_path):
        print('NDK OK')
        return
    File.unzip(__ndk_zip_path, File.config_path())

def make_toolchain(destination, arch = _arch, api = _api):
    Shell.run([
        System.python_cmd,
        ndk_path + '/build/tools/make_standalone_toolchain.py',
        '--arch=' + arch,
        '--api=' + api,
        '--stl=libc++',
        '--install-dir=' + destination
    ])

def setup():
    if File.exists(_toolchain_path):
        print('android ndk and toolchain OK')
    else:
        downloadNDK()
        unzipNDK()
        make_toolchain(_toolchain_path)
