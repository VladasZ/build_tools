import sys

all = sys.argv

def has(flag_name, short_flag = "zzzzzzzzzz"):
    for arg in all:
        if arg == flag_name or arg == short_flag:
            return True
    return False

def get(index = 1):
    return all[index]

def count():
    return len(all)

def dump():
    print(all)

ios             = has("--ios", "ios")
gcc             = has("--gcc")
run             = has("--run")
ide             = has("--ide", "id")
make            = has("--make")
test            = has("--test")
multi           = has("--multi")
flash           = has("--flash")
build           = has("--build", "b")
clang           = has("--clang")
clean           = has("--clean", "c")
debug           = has("--debug", "db")
release         = has("--release", "rl")
verilog         = has("--verilog")
android         = has("--android")
prepare         = has("--prepare", "p")
rmbuild         = has("--rmbuild")
simulate        = has("--simulate")
deps_info       = has("--deps-info", "i")
force_build     = has("--force-build")
manual_compiler = has("--manual-compiler")

desktop_build = True

if ios:
    desktop_build = False




    
