import sys

all = sys.argv

def has(flag_name):
    for arg in all:
        if arg == flag_name:
            return True
    return False

def get(index = 1):
    return all[index]

def count():
    return len(all)

def dump():
    print(all)

ios             = has("--ios")
gcc             = has("--gcc")
run             = has("--run")
ide             = has("--ide")
make            = has("--make")
test            = has("--test")
multi           = has("--multi")
flash           = has("--flash")
build           = has("--build")
clang           = has("--clang")
clean           = has("--clean")
debug           = has("--debug")
release         = has("--release")
verilog         = has("--verilog")
android         = has("--android")
prepare         = has("--prepare")
rmbuild         = has("--rmbuild")
simulate        = has("--simulate")
deps_info       = has("--deps-info")
force_build     = has("--force-build")
manual_compiler = has("--manual-compiler")

desktop_build = True

if ios:
	desktop_build = False




    
