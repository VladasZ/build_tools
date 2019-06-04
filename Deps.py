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
    Git.clone("https://github.com/vladasz/" + name, path)
    

def install():
    deps = File.get_lines("../deps.txt")
    project_name = File.folder_name(File.full_path(".."))
    print("Cloning git dependencies:")
    print(deps)
    for dep in deps:
        if Args.ios and dep == "soil":
            continue
        _install(dep)
    Cmake.add_var(_clean_project_name(project_name) + "_path", "\"" + File.full_path("..") + "\"")

def print_info():
    changes = False
    for dep in File.get_files(directory):
        if dep == ".DS_Store":
            continue
        if Git.has_changes(directory + "/" + dep):
            changes = True
            print(dep + " - has changes")
    if not changes:
        print("no changes")

