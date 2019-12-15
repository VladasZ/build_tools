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



x32             = has(["--x32", "x32", "32"])    
ios             = has(["--ios", "ios"])
gcc             = has(["--gcc", "gcc"])
run             = has(["--run"])
ide             = has(["--ide", "ide"])
ios6            = has(["--ios6", "ios6", "i6"])
ios7            = has(["--ios7", "ios7", "i7"])
ios8            = has(["--ios8", "ios8", "i8"])
ios9            = has(["--ios9", "ios9", "i9"])
vs19            = has(["--vs19", "vs19"])
make            = has(["--make"])
hand            = has(["--hand"])
test            = has(["--test"])
cpp11           = has(["--cpp11", "cpp11", "11"])
cpp14           = has(["--cpp14", "cpp14", "14"])
multi           = has(["--multi"])
flash           = has(["--flash"])
build           = has(["--build", "b"])
clang           = has(["--clang", "clang"])
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

_3gs = has(["--3gs", "3gs"])
_4s  = has(["--4s", "4s"])

if _3gs:
    clean    = True
    prepare  = True
    debug    = True
    ide      = True
    ios      = True
    device   = True
    no_conan = True
    ios6     = True
    x32      = True

if _4s:
    clean    = True
    prepare  = True
    debug    = True
    ide      = True
    ios      = True
    device   = True
    no_conan = True
    ios7     = True
    x32      = True

ios_version = "9.0"

if ios6:
    ios_version = "6.0"

if ios7:
    ios_version = "7.0"

if ios8:
    ios_version = "8.0"

cpp_standart = 17
cpp17 = True

if cpp11:
    cpp_standart = 11
    cpp11 = True
    cpp14 = False
    cpp17 = False
elif cpp14:
    cpp_standart = 14
    cpp11 = True
    cpp14 = True
    cpp17 = False
else:
    cpp_standart = 17
    cpp11 = True
    cpp14 = True
    cpp17 = True

mobile = android or ios
desktop_build = not mobile

if no_conan:
    no_soil     = True
    no_box2d    = True
    no_assimp   = True
    no_freetype = True

needs_signing = (device and build) or android
