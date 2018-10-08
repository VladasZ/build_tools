import File
import Args
import Cmake
import Conan
import Shell    

root_dir = Cmake.root_dir()

File.cd(root_dir)

my_build = File.exists("config/utils/Build.py")
tesla_build = File.exists("configuration/build.py")
build_exists = File.exists("build")



print(root_dir)
print(my_build)
print(tesla_build)
print(build_exists)
print(File.pwd())
    

def prepare_build():
    Conan.setup()
    Cmake.setup()

    File.mkdir("build")
    File.cd("build")

    Conan.run()
    Cmake.run()


def make():
    if not build_exists:
        prepare_build()
    else:
        File.cd("build")
    
    Shell.run(['make'])


if Args.make:
    make()
else:
    prepare_build()

    
