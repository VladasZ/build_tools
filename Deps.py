from __future__ import annotations
from typing import Set
from typing import List
from typing import Dict

import Git
import Args
import File
import Paths
import Cmake
import Debug

_ignore_build_tools = False

_deps: Set[Dep] = set()


def string_to_dep(string: str) -> Dep:
    return Dep(string)


class Dep:
    def __init__(self, name: str):
        self.name: str = name

    def __eq__(self, other: Dep):
        return self.name == other.name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def path(self) -> str:
        return Paths.deps + "/" + self.name

    def deps_file_path(self) -> str:
        return self.path() + "/deps.txt"

    def needs_deps(self) -> float:
        return File.exists(self.deps_file_path())

    def simple_conan_file(self) -> str:
        return self.path() + "/conan.txt"

    def subdeps(self) -> Set[Dep]:
        if not self.needs_deps():
            return set()
        my_supdeps: Set[Dep] = set(map(string_to_dep, File.get_lines(self.deps_file_path())))
        subsubdeps: List[Set[Dep]] = list()
        for subdep in my_supdeps:
            subsubdeps += [subdep.subdeps()]
        for sub in subsubdeps:
            my_supdeps |= sub
        return my_supdeps

    def has_changes(self) -> bool:
        return Git.has_changes(self.path())

    def remote_link(self) -> str:
        return "https://github.com/vladasz/" + self.name

    def clone(self):
        Git.clone(self.remote_link(), self.path(), recursive=True, ignore_existing=True)

    def add_to_cmake(self):
        if self not in _deps:
            Cmake.add_var(self.name + "_PATH", "\"" + self.path() + "\"")
            _deps.add(self)

        for sub in self.subdeps():
            self.add_sub_dep_to_cmake(sub)
            sub.add_to_cmake()

    def add_sub_dep_to_cmake(self, sub_dep):
        Cmake.append_var(self.name + "_PATHS_TO_INCLUDE", "\"" + sub_dep.path() + "\"")
        Cmake.append_var(self.name + "_LIBS_TO_LINK",     "\"" + sub_dep.name  + "\"")


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


def clean():
    return
    # for dep in File.get_files(Paths.deps):
    #     File.rm(_path_for(dep) + "/dep_build")
    #     File.rm(_path_for(dep) + "/build")


def print_info():
    changes = False
    for dep in all_installed():
        if dep == ".DS_Store":
            continue
        if Dep(dep).has_changes():
            changes = True
            print(dep + " - has changes")
    if not changes:
        print("no changes")
