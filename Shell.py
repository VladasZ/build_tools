import os
import shutil
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

def get(commands, simple = True):
    if simple:
        command = ""
        for com in commands:
            command += com + " "
        temp = os.popen(command).read()
        return temp
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
        retcode = p.poll() #returns None while subprocess is running
        line = p.stdout.readline()
        yield line
        if(retcode is not None):
            break   


def which(command):
    return shutil.which(command)

def check(commands):
    try:
        retcode = subprocess.call(commands, stdout = open(os.devnull, 'wb'), stderr = open(os.devnull, 'wb'))
        return retcode == 0
    except:
        return False
