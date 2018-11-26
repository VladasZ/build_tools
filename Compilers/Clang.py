import sys
sys.path.append("..")

import Shell
import Regex
import Debug
import System

from Compilers.CompilerBase import Compiler


def get():

    if not Shell.check(["clang", "-dumpversion"]) or not System.is_mac:
        return Compiler("clang")

    supported_versions = [9, 10]

    version_output = Shell.get(["clang", "-v"])
    full_version  = Regex.version(version_output)

    major_version = Regex.first_number(full_version)

    if not major_version in supported_versions:
        return Compiler("clang")

    conan_version = full_version[:3]

    if major_version > 9:
        conan_version = full_version[:4]
    
    return Compiler(name          = "clang",
                    is_available  = True,
                    libcxx        = "libc++",
                    conan_name    = "apple-clang",
                    full_version  = full_version,
                    major_version = major_version,
                    conan_version = conan_version,
                    CC            = "clang",
                    CXX           = "clang++")
