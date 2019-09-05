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
gcc             = has(["--gcc"])
run             = has(["--run"])
ide             = has(["--ide", "ide", "id"])
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
android         = has(["--android", "an", "a"])
prepare         = has(["--prepare", "p"])
rmbuild         = has(["--rmbuild"])
no_conan        = has(["--no-conan", "no-conan", "noconan", "nc"])
simulate        = has(["--simulate"])
simulator       = has(["--simulator", "sim", "sm"])
deps_info       = has(["--deps-info", "i"])
force_build     = has(["--force-build"])
manual_compiler = has(["--manual-compiler"])

desktop_build = True

if ios or android:
    desktop_build = False




    
