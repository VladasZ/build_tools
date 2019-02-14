import Git
import File
import Cmake

_deps_dir = "/.deps"
_storage_dir = File.home_dir + _deps_dir

def _install(name, update = False):
    path = _storage_dir + "/" + name
    local_path = File.full_path("." + _deps_dir + "/" + name)

    Cmake.append_var("GIT_DEPENDENCIES", local_path)
    Cmake.add_var(name + "_path", local_path)
    
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

    File.copy(_storage_dir, File.full_path("." + _deps_dir))

    

