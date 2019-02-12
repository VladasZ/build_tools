import Git
import File
import Cmake

def install():
    deps = File.get_lines("../dependencies.txt")
    print("Cloning git dependencies:")
    print(deps)
    for dep in deps:
        Git.clone("https://github.com/vladasz/" + dep, "deps/" + dep)
        Cmake.append_var("GIT_DEPENDENCIES", File.full_path("deps/" + dep))
        Cmake.add_var(dep + "_path", File.full_path("deps/" + dep))
