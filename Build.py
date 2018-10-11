import File
import Args
import Make
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

    File.mkdir('build')
    File.cd('build')

    Conan.run()
    Cmake.run()

    if Args.make:
        Make.run()

def verilog():
    if Args.build:
        Verilog.build()
    elif Args.run:
        Verilog.run()
    elif Args.test:
        Verilog.test()

if Args.verilog:
    verilog()
else:
    cpp()
