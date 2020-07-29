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
import Conan

_ignore_build_tools = False

_ready: Set[Dep] = set()
_addedSubdirs: Set[Dep] = set()


def string_to_dep(string: str) -> Dep:
    return Dep(string)


class Dep:
    def __init__(self, name: str):
        self.name: str = name
        self.needs_linking = False

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

    def setup_conan(self):
        if File.exists(self.simple_conan_file()):
            Conan.add_requires(self.simple_conan_file())

    def deps(self) -> Set[Dep]:
        if not self.needs_deps():
            return set()
        result = set(map(string_to_dep, File.get_lines(self.deps_file_path())))
        for dep in result:
            dep.clone()
        return result

    def subdeps(self) -> Set[Dep]:
        result: Set[Dep] = set()
        for sub in self.deps():
            result |= sub.deps()
            result |= sub.subdeps()
        return result

    def all_deps(self) -> Set[Dep]:
        return self.deps().union(self.subdeps())

    def has_changes(self) -> bool:
        return Git.has_changes(self.path())

    def remote_link(self) -> str:
        return "https://github.com/vladasz/" + self.name

    def clone(self):
        if self.is_cloned():
            return
        Git.clone(self.remote_link(), self.path(), recursive=True, ignore_existing=True)

    def is_cloned(self):
        return File.exists(self.path())

    def add_to_cmake(self):

        global _ready

        if self in _ready:
            return

        self.setup_conan()
        _ready.add(self)

        Cmake.add_var(self.name + "_PATH", self.path())

        for dep in self.deps():
            self.include_in_cmake(dep)
            self.link_in_cmake(dep)

        for dep in self.subdeps():
            self.include_in_cmake(dep)

        for dep in self.all_deps():
            dep.add_to_cmake()

    def include_in_cmake(self, dep: Dep):
        Cmake.append_var(self.name + "_PATHS_TO_INCLUDE", "\"" + dep.path() + "\"")

    def link_in_cmake(self, dep: Dep):
        Cmake.append_var(self.name + "_LIBS_TO_LINK", "\"" + dep.name  + "\"")

        global _addedSubdirs

        if dep in _addedSubdirs:
            return

        _addedSubdirs.add(dep)

        Cmake.append_var(self.name + "_PROJECTS_TO_ADD", "\"" + dep.path()  + "\"")

    def clean(self):
        File.rm(self.path() + "/dep_build")
        File.rm(self.path() + "/build")


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
    for dep in File.get_files(Paths.deps):
        Dep(dep).clean()


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
