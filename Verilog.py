import Git
import Args
import File
import Shell

project_path = Git.root_dir()
project_name = File.folder_name(project_path)

test_module  = "test.v"
top_module   = "top.v"

def build():
    print("yosys -q -p \"synth_ice40 -blif " + project_name + ".blif\" " + top_module)
    Shell.run_string("yosys -q -p \"synth_ice40 -blif " + project_name + ".blif\" " + top_module)
    
    Shell.run_string("arachne-pnr -d 8k -p " +
                     project_name + ".pcf " +
                     project_name + ".blif -o " +
                     project_name + ".asc")

    Shell.run_string("icepack " +
                     project_name + ".asc " +
                     project_name  + ".bin")

def run():
    build()
    Shell.run_string("icoprog -p < " + project_name + ".bin")

def simulate():
    Shell.run(["iverilog", "-g2009", "-o", project_name + ".out" , test_module])
    Shell.run(["./" + project_name + ".out"])

if Args.simulate:
    simulate()

if Args.build:
    build()

if Args.run:
    run()
