import Git
import File
import Args
import Make
import Cpp
import Time
import Cmake
import Conan
import Debug
import Verilog

def cpp():
    if Args.prepare or Args.ide:
        Cpp.prepare()
    elif Args.build:
        Cpp.build()
    elif Args.run:
        Cpp.run()
    elif Args.clean:
        Cpp.clean()
        print("Clean successful")
    else:
        print("No argument provided to build script")
        
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
else:
    cpp()
