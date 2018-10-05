import File
import Args
import Cmake

root_dir = Cmake.root_dir()

my_build = File.exists(root_dir + "/build.py")
tesla_build = File.exists(root_dir + "configuration/build.py")


    

