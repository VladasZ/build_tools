import Git
import File
import Paths

toolchain_path = Paths.deps + "/toolchains/iOS/"
toolchain_file = toolchain_path + "ios.toolchain.cmake"

def toolchain_ready():
    return File.exists(toolchain_file)

def setup():
    if not toolchain_ready():
        Git.clone("https://github.com/leetal/ios-cmake", toolchain_path, True)
