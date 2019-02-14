import Git
import File
import Cmake

_deps_dir = "/.deps"
_storage_dir = File.home_dir + _deps_dir

def _install(name, update = False):
    path = _storage_dir + "/" + name
    local_path = File.full_path("." + _deps_dir + "/" + name)
    Cmake.append_var("GIT_DEPENDENCIES", path)
    Cmake.add_var(name + "_path", path)
    if update:
        File.rm(path)
    elif File.exists(path):
        return
    Git.clone("https://github.com/vladasz/" + name, path)
    

def install():
    deps = File.get_lines("../deps.txt")
    project_name = File.folder_name(File.full_path(".."))
    print("Cloning git dependencies:")
    print(deps)
    for dep in deps:
        _install(dep)
    Cmake.add_var(project_name + "_path", File.full_path(".."))

def print_info():
    changes = False
    for dep in File.get_files(_storage_dir):
        if Git.has_changes(_storage_dir + "/" + dep):
            changes = True
            print(dep + " - has changes")
    if not changes:
        print("no changes")

