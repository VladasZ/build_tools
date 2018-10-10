import File
import Args
import Make
import Cmake
import Conan

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
    
