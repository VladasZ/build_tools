import Git
import File
import Args
import Make
import Time
import Cmake
import Conan
import Debug
import Verilog

def cpp():
    conan_dir = Conan.root_dir()
    File.cd(conan_dir)

    print(conan_dir)

    Conan.setup()
    Cmake.setup()

    Time.stamp()
    
    File.mkdir('build')
    File.cd('build')

    Conan.run()
    Cmake.run()

    print("Project prebuild time: " + Time.duration())
    
    if Args.make:
        Make.run()
        print("Project build time: " + Time.duration())

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
