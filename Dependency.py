import Git
import File
import Cmake

def install():
    deps = File.get_lines("../dependencies.txt")

    project_name = File.folder_name(File.full_path(".."))
    
    print("Cloning git dependencies:")
    print(deps)
    
    for dep in deps:
        Git.clone("https://github.com/vladasz/" + dep, "deps/" + dep)
        Cmake.append_var("GIT_DEPENDENCIES", File.full_path("deps/" + dep))
        Cmake.add_var(dep + "_path", File.full_path("deps/" + dep))

    Cmake.add_var(project_name + "_path", File.full_path(".."))

