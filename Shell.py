import os
import subprocess

def run(commands = [], *args):
       print(commands)
       child = subprocess.Popen(commands, stdout=subprocess.PIPE)
       while child.poll() is None:
           output_line = child.stdout.readline()
           if (output_line):
               print(output_line.decode("utf-8")[:-1])
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
    