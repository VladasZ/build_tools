import Git
import Args
import File
import Paths
import Cmake
import Debug

_ignore_build_tools = False

_deps = set()
_deps_map = {}


def all_installed():
    return File.get_files(Paths.deps)


def _safe_to_delete():
    for dep in all_installed():
        if dep == File.folder_name():
            continue
        if _ignore_build_tools and dep == "build_tools":
            continue
        if Git.has_changes(Paths.deps + "/" + dep):
            Debug.info("Dep " + dep + " has changes.")
            return False
    return True


def print_info():
    changes = False
    for dep in all_installed():
        if dep == ".DS_Store":
            continue
        if _has_changes(dep):
            changes = True
            print(dep + " - has changes")
    if not changes:
        print("no changes")


def clean():
    for dep in File.get_files(Paths.deps):
        File.rm(_path_for(dep) + "/dep_build")
        File.rm(_path_for(dep) + "/build")


def make_map(dep):

    _clone(dep)
    _deps.add(dep)

    if not _needs_deps(dep):
        return

    for subdep in _supdeps_for(dep):
        make_map(subdep)
        _add_subdep(dep, subdep)


def set_cmake_vars():
    for dep in _deps:
        _add_to_cmake(dep)
        if dep in _deps_map.keys():
            for sub_dep in _deps_map[dep]:
                _add_sub_dep_to_cmake(dep, sub_dep)


def _path_for(dep):
    return Paths.deps + "/" + dep


def _deps_file_path_for(dep):
    return _path_for(dep) + "/deps.txt"


def _needs_deps(dep):
    return File.exists(_deps_file_path_for(dep))


def _simple_conan_file_for(dep):
    return _path_for(dep) + "/conan.txt"


def _supdeps_for(dep):
    return File.get_lines(_deps_file_path_for(dep))


def _add_subdep(dep, sub_dep):
    if dep not in _deps_map.keys():
        _deps_map[dep] = set()
    _deps_map[dep].add(sub_dep)
    if _needs_deps(sub_dep):
        for sub_sub_dep in _supdeps_for(sub_dep):
            _add_subdep(dep, sub_sub_dep)


def _has_changes(dep):
    return Git.has_changes(_path_for(dep))


def _remote_link(dep):
    return "https://github.com/vladasz/" + dep


def _clone(dep):
    Git.clone(_remote_link(dep), _path_for(dep), recursive=True, ignore_existing=True)


def _add_to_cmake(dep):
    Cmake.add_var(dep + "_PATH", "\"" + _path_for(dep) + "\"")


def _add_sub_dep_to_cmake(dep, sub_dep):
    Cmake.append_var(dep + "_GIT_DEP_PATHS", "\"" + _path_for(sub_dep) + "\"")
    Cmake.append_var(dep + "_GIT_DEPS",      "\"" +           sub_dep  + "\"")
