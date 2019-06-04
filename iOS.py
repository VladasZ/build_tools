import Git
import File

toolchain_path = File.deps_path + "/toolchains/iOS/"
toolchain_file = toolchain_path + "ios.toolchain.cmake"

def toolchain_ready():
    return File.exists(toolchain_file)

def clone_toolchain():
    if not toolchain_ready():
        Git.clone("https://github.com/leetal/ios-cmake", toolchain_path, True)

clone_toolchain()
