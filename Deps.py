import Git
import File
import Paths
import Cmake
import Debug


_deps_file = "deps.txt"
_project_name = File.folder_name()


def all_installed():
    return File.get_files(Paths.deps)


def safe_to_delete():
    for dep in all_installed():
        if dep == _project_name:
            continue
        if Git.has_changes(Paths.deps + "/" + dep):
            Debug.info("Dep " + dep + " has changes.")
            return True
    return False


def install():
    deps = File.get_lines(_deps_file)
    print("Cloning git dependencies:")
    print(deps)
    for dep in deps:
        _install(dep)
    _install("build_tools")


def print_info():
    changes = False
    for dep in all_installed():
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


def _clean_project_name(name):
    return name.replace("-", "_")


def _install(name, update=True):
    if name == _project_name:
        return
    if update and safe_to_delete():
        Debug.throw("Commit deps changes before updating.")
    path = Paths.deps + "/" + name
    Cmake.append_var("GIT_DEPENDENCIES", "\"" + path + "\"")
    Cmake.add_var(_clean_project_name(name) + "_path", "\"" + path + "\"")
    Git.clone("https://github.com/vladasz/" + name, path, delete_existing=update, recursive=True)
