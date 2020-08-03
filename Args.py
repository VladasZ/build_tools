import sys
import platform
import Debug


all_in_flags = sys.argv

all_known = []


def has(flags):
    for flag in flags:
        global all_known
        if flag in all_known:
            Debug.info("Dupicated flag: " + flag)
            Debug.throw()
    for arg in all_in_flags:
        for flag in flags:
            if arg == flag:
                all_in_flags.remove(arg)
                return True
    return False


def get(index = 1):
    return all_in_flags[index]


def count():
    return len(all_in_flags)


def dump():
    print(all_in_flags)


def empty():
    return count() == 1


pi              = has(["--pi", "pi"])
x32             = has(["--x32", "x32", "32"])
ios             = has(["--ios", "ios"])
gcc             = has(["--gcc", "gcc"])
run             = has(["--run"])
ide             = has(["--ide", "ide"])
ios6            = has(["--ios6", "ios6", "i6"])
ios7            = has(["--ios7", "ios7", "i7"])
ios8            = has(["--ios8", "ios8", "i8"])
ios9            = has(["--ios9", "ios9", "i9"])
vs15            = has(["--vs15", "vs15"])
vs17            = has(["--vs17", "vs17"])
vs19            = has(["--vs19", "vs19"])
make            = has(["--make"])
msvc            = has(["--msvc", "msvc"])
hand            = has(["--hand"])
test            = has(["--test"])
multi           = has(["--multi"])
mingw           = has(["--mingw", "mingw", "mgw"])
flash           = has(["--flash"])
build           = has(["--build", "b"])
unity           = has(["--unity", "unity", "un", "u"])
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
no_bitcode      = has(["--no-bitcode", "no-bitcode", "no-bit"])
no_ios_exe      = has(["--no-ios-exe", "no-ios-exe", "nie"])
update_deps     = has(["--update-deps", "update-deps", "ud"])
force_build     = has(["--force-build", "force-build", "fb"])
compilers_info  = has(["--compilers-info", "ci"])
manual_compiler = has(["--manual-compiler"])

no_conan        = has(["--no-conan", "no-conan", "noconan", "nc"])

no_qt           = has(["--no-qt",       "noqt",       "nqt",      "nq"])
no_glm          = has(["--no-glm",      "noglm",                  "ng"])
no_soil         = has(["--no-soil",     "nosoil",                 "ns"])
no_boost        = has(["--no-boost",    "noboost",    "nbo",      "nb"])
no_box2d        = has(["--no-box2d",    "nobox2d",    "nobox",    "nb2"])
no_bull3        = has(["--no-bullet3",  "nobullet3",  "nobullet", "nb3"])
no_assimp       = has(["--no-assimp",   "noassimp",   "noassimp", "na"])
no_freetype     = has(["--no-freetype", "nofreetype", "noft",     "nf"])

_3gs = has(["--3gs", "3gs"])
_4s  = has(["--4s", "4s"])

if _3gs:
    clean    = True
    prepare  = True
    ide      = True
    ios      = True
    device   = True
    ios6     = True
    x32      = True

if _4s:
    clean    = True
    prepare  = True
    ide      = True
    ios      = True
    device   = True
    ios7     = True
    x32      = True

ios_version = "9.0"

if ios6:
    ios_version = "6.0"

if ios7:
    ios_version = "7.0"

if ios8:
    ios_version = "8.0"

mobile = android or ios
desktop_build = not mobile

if no_conan:
    no_qt       = True
    no_glm      = True
    no_soil     = True
    no_box2d    = True
    no_boost    = True
    no_bull3    = True
    no_assimp   = True
    no_freetype = True


if len(all_in_flags) != 1:
    Debug.info("Unknown parameter:")
    Debug.info(all_in_flags[1:])
    Debug.throw()
