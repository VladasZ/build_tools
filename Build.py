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
    Time.stamp()
    if Args.prepare:
        Cpp.prepare()
        print("Project prepare time: " + Time.duration())
    elif Args.build:
        Cpp.build()
        print("Project build time: " + Time.duration())
    elif Args.run:
        Cpp.build()
        print("Project build time: " + Time.duration())
        Cpp.run()
    elif Args.clean:
        Cpp.clean()
        print("Clean successful")
    
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
        
if Args.verilog:
    verilog()
else:
    cpp()
