import Arm
import Cpp
import Git
import Args
import Time
import File
import Paths
import Deploy
import Verilog
import Compiler


work_dirs = [
    Paths.sand,
    Paths.home,
    Paths.deps,
    Paths.tes,
    Paths.glove,
    Paths.atom,
    Paths.my,
    Paths.money,
]


def all_repos():
    result = []
    for dir in work_dirs:
        result += Git.list_repos(dir)
    return result


def cpp():

    if Args.deploy:
        Deploy.install_all()
        exit()

    if Args.clone_all:
        Git.clone_all_projects()
        exit()

    if Args.deps_info:
        for dir in work_dirs:
            Git.pring_folder_changes(dir)
        exit()

    if Args.pullall:
        for dir in work_dirs:
            Git.pull_folder(dir)
        exit()

    if File.exists(Cpp.root_dir + "/Makefile"):
        if Args.clean:
            Arm.clean()
            print("Clean successful")
        if Args.run:
            Arm.run()
        elif Args.build:
            Arm.build()
        elif Args.flash:
            Arm.flash()
        return

    if Args.clean:
        Cpp.clean()
        print("Clean successful")
        
    if Args.prepare or Args.ide:
        Cpp.prepare()

    if Args.build:
        Cpp.build()


def verilog():
    File.cd(Git.root_dir())
    Time.stamp()
    if Args.build:
        Verilog.build()
        print("Verilog build time: " + Time.duration())
    elif Args.run:
        Verilog.run()
        print("Verilog build and flash time: " + Time.duration())
    elif Args.simulate:
        Verilog.simulate()
        print("Verilog test build time: " + Time.duration())
    elif Args.flash:
        Verilog.flash()
        print("Verilog flash time: " + Time.duration())
    else:
        print("No argument provided to build script")


if Args.verilog:
    verilog()
    exit()

if Args.compilers_info:
    Compiler.print_info()
    exit()

cpp()
