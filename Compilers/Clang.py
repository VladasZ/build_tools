import Args
import Shell
import Regex
import System

from Compilers.CompilerBase import Compiler


def get():

    if not Shell.check(["clang", "-dumpversion"]):
        return Compiler("clang")

    supported_versions = []

    if System.is_mac:
        supported_versions = [9, 10, 11, 12]
    else:
        supported_versions = [6]

    version_output = Shell.get(["clang", "-v"])
    full_version  = Regex.version(version_output)

    major_version = Regex.first_number(full_version)

    if not major_version in supported_versions:
        return Compiler("clang")

    conan_version = full_version[:3]

    if System.is_mac and major_version > 9:
        conan_version = full_version[:4]

    name = "clang"

    if System.is_mac and not Args.android:
        name = "apple-clang"
        
    return Compiler(name          = "clang",
                    is_available  = True,
                    libcxx        = "libc++",
                    conan_name    = name,
                    full_version  = full_version,
                    major_version = major_version,
                    conan_version = conan_version,
                    CC            = "clang",
                    CXX           = "clang++")
