import os
import subprocess
import Debug

def run_string(string):
    if os.system(string):
        Debug.throw("Shell script has failed")

def run(commands = [], *args):

    command_string = ""
    
    for command in commands:
        command_string += command + " "
    
    print(command_string)

    child = subprocess.Popen(commands, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
    while child.poll() is None:
        output_line = child.stdout.readline()
        if (output_line):
            print(output_line)
    code = child.returncode
    if (code):
        os.sys.exit(code)

def get(commands = [], *args):
    child = subprocess.Popen(commands, stdout=subprocess.PIPE)
    result = ""
    while child.poll() is None:
        output_line = child.stdout.readline()
        if (output_line):
            result += output_line.decode("utf-8")[:-1]
    code = child.returncode
    if (code):
        os.sys.exit(code)
    return result
    
