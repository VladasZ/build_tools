import Arm
import Cpp
import Git
import File
import Args
import Make
import Time
import File
import Deps
import Paths
import Cmake
import Conan
import Debug
import Verilog
import Compiler


def cpp():

    if Args.deps_info:
        Git.pring_folder_changes(Paths.deps)
        Git.pring_folder_changes(Paths.tes)
        Git.pring_folder_changes(Paths.glove)
        Git.pring_folder_changes(Paths.atom)
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
