import Git
import Args
import File
import Paths
import Cmake

def _clean_project_name(name):
    return name.replace("-", "_")

def _install(name, update = False):
    path = Paths.deps + "/" + name
    Cmake.append_var("GIT_DEPENDENCIES", "\"" + path + "\"")
    Cmake.add_var(_clean_project_name(name) + "_path", "\"" + path + "\"")
    if update:
        File.rm(path)
    elif File.exists(path):
        return
    Git.clone("https://github.com/vladasz/" + name, path, recursive = True)
    

def install():
    deps = File.get_lines("../deps.txt")
    print("Cloning git dependencies:")
    print(deps)
    for dep in deps:
        if Args.ios and dep == "soil":
            continue
        _install(dep)

def print_info():
    changes = False
    for dep in File.get_files(Paths.deps):
        if dep == ".DS_Store":
            continue
        if Git.has_changes(Paths.deps + "/" + dep):
            changes = True
            print(dep + " - has changes")
    if not changes:
        print("no changes")

def clean():
    for dep in File.get_files(Paths.deps):
        File.rm(Paths.deps + "/" + dep + "/dep_build")
        File.rm(Paths.deps + "/" + dep + "/build")
