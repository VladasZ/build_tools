import sys

all = sys.argv

def has(flags):
    for arg in all:
        for flag in flags:
            if arg == flag:
                return True
    return False

def get(index = 1):
    return all[index]

def count():
    return len(all)

def dump():
    print(all)

ios             = has(["--ios", "ios"])
gcc             = has(["--gcc", "gcc"])
run             = has(["--run"])
ide             = has(["--ide", "ide", "id"])
vs19            = has(["--vs10", "vs19"])
make            = has(["--make"])
hand            = has(["--hand"])
test            = has(["--test"])
multi           = has(["--multi"])
flash           = has(["--flash"])
build           = has(["--build", "b"])
clang           = has(["--clang"])
clean           = has(["--clean", "c"])
debug           = has(["--debug", "d"])
device          = has(["--device", "dev"])
release         = has(["--release", "r"])
verilog         = has(["--verilog"])
android         = has(["--android", "android", "an", "a"])
prepare         = has(["--prepare", "p"])
rmbuild         = has(["--rmbuild"])
simulate        = has(["--simulate"])
simulator       = has(["--simulator", "sim", "sm"])
deps_info       = has(["--deps-info", "i"])
update_deps     = has(["--update-deps", "update-deps", "ud"])
force_build     = has(["--force-build"])
compilers_info  = has(["--compilers-info", "ci"])
manual_compiler = has(["--manual-compiler"])

no_conan        = has(["--no-conan", "no-conan", "noconan", "nc"])

no_soil         = has(["--no-soil", "nosoil", "ns"])
no_box2d        = has(["--no-box2d", "no-box2d", "nobox", "nb"])
no_assimp       = has(["--no-assimp", "no-assimp", "noassimp", "na"])
no_freetype     = has(["--no-freetyoe", "no-freetype", "noft", "nf"])

mobile = android or ios

if no_conan:
    no_soil     = True
    no_box2d    = True
    no_assimp   = True
    no_freetype = True

desktop_build = not (ios or android)

needs_signing = (device and build) or android
