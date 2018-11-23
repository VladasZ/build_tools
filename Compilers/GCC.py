import sys
sys.path.append("..")

import Shell
import Regex
import Debug

from Compilers.CompilerBase import Compiler

def get():
    
    if not Shell.check(["gcc", "-dumpversion"]):
        return Compiler("gcc")

    name = "gcc"
    
    supported_versions = [7, 8]
    default_version = Shell.get(["gcc", "-dumpversion"])
    default_major_version = Regex.first_number(default_version)

    print(default_major_version)
    print(default_major_version in [7,8])

    if default_major_version in supported_versions:
        return Compiler(name = "gcc",
                        is_available = True,
                        full_version = default_version,
                        major_version = default_major_version,
                        conan_version = default_version[:3],
                        CXX = "g++")

    version = None

    for ver in supported_versions:
        if Shell.check(["gcc-" + str(ver), "-dumpversion"]):
            version = ver
            break

    if not version:
        return Compiler("gcc")

    full_version = Shell.get(["gcc-" + str(version), "-dumpversion"])
    major_version = Regex.first_number(full_version)
    
    return Compiler(name = "gcc",
                    is_available = True,
                    full_version = full_version,
                    major_version = Regex.first_number(full_version),
                    conan_version = full_version[:3],
                    CC = "gcc-" + str(version),
                    CXX = "g++-" + str(version))

