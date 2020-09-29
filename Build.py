import Cpp
import Git
import Args
import Time
import File
import Deps
import Verilog
import Compiler


def cpp():

    if Args.deps_info:
        Deps.print_info()
        exit()

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
