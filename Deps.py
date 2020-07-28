import Git
import Args
import File
import Paths
import Cmake
import Debug
import Conan

_ignore_build_tools = False

_installed_deps = []
_known_path = []


def all_installed():
    return File.get_files(Paths.deps)


def safe_to_delete():
    for dep in all_installed():
        if dep == File.folder_name():
            continue
        if _ignore_build_tools and dep == "build_tools":
            continue
        if Git.has_changes(Paths.deps + "/" + dep):
            Debug.info("Dep " + dep + " has changes.")
            return True
    return False


def install(project_name, deps_file):

    global _installed_deps

    if project_name in _installed_deps:
        return

    _installed_deps += [project_name]

    deps = File.get_lines(deps_file)
    Debug.info("=========================================")
    Debug.info(_clean_project_name(project_name))
    Debug.info(deps)
    for dep in deps:
        _install(project_name, dep)
    if not _ignore_build_tools:
        _install(project_name, "build_tools")


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


def _install(project_name, dep_name):

    if dep_name == "soil":
        Debug.throw("Soil dep is no logner supported. Use conan package.")

    path = Paths.deps + "/" + dep_name

    global _known_path

    if dep_name not in _known_path:
        _known_path += [dep_name]
        Cmake.add_var(_clean_project_name(dep_name) + "_PATH", "\"" + Paths.deps + "/" + dep_name + "\"")

    if dep_name != "build_tools":
        Cmake.append_var(_clean_project_name(project_name) + "_GIT_DEPENDENCIES_PATHS", "\"" + path + "\"")
        Cmake.append_var(_clean_project_name(project_name) + "_GIT_DEPENDENCIES", _clean_project_name(dep_name))

    Git.clone("https://github.com/vladasz/" + dep_name, path, recursive=True, ignore_existing=True)

    deps_file = path + "/deps.txt"
    simple_conan_file = path + "/conan.txt"

    if File.exists(deps_file):
        install(dep_name, deps_file)

    if File.exists(simple_conan_file):
        Conan.add_requires(simple_conan_file)
