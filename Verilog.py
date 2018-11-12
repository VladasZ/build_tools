import Git
import Args
import File
import Shell

project_path = Git.root_dir()
project_name = File.folder_name(project_path)

test_module  = "test.v"
top_module   = "top.v"

simulation_flag_file_name = "simulation_flag.v"

def build():
    File.write(simulation_flag_file_name, "")
    
    print("yosys -q -p \"synth_ice40 -blif " + project_name + ".blif\" " + top_module)
    Shell.run_string("yosys -q -p \"synth_ice40 -blif " + project_name + ".blif\" " + top_module)
    
    Shell.run_string("arachne-pnr -d 8k -p " +
                     project_name + ".pcf " +
                     project_name + ".blif -o " +
                     project_name + ".asc")

    Shell.run_string("icepack " +
                     project_name + ".asc " +
                     project_name  + ".bin")

def flash():
    Shell.run_string("icoprog -p < " + project_name + ".bin")

def run():
    build()
    flash()
    
def simulate():
    File.write(simulation_flag_file_name, "`define SIMULATION")

    file_name = project_name + ".out"
    Shell.run(["iverilog", "-g2012", "-o", file_name , test_module])
    Shell.run(["./" + file_name])
#    File.zip(project_name + ".vcd")
    File.zip("dump.vcd")
