import os
import shutil
import subprocess

def run_string(string):
    print(string)
    if os.system(string):
        print("Shell script has failed")
        exit()

def _execute(commands, silent):
    command_string = ""
    for command in commands:
        command_string += command + " "
    if not silent:
        print(command_string)

    output_line = ""
    output = ""

    try:
        stdout = subprocess.PIPE
        child = subprocess.Popen(commands,
                                 stdout = stdout,
                                 bufsize = 1,
                                 universal_newlines = True)
        output = ""
        while child.poll() is None:
            output_line = child.stdout.readline()
            if (output_line):
                if not silent:
                    print(output_line, end =" ")
                output += output_line
        code = child.returncode
        if (code and not silent):
            os.sys.exit(code)
    except:
        if not silent:
            raise
    return output


def run(commands):
    return _execute(commands, silent = False)

def get(commands):
    command = ""
    for com in commands:
        command += com + " "
    return subprocess.getoutput(command)

def which(command):
    return shutil.which(command)

def check(commands):
    try:
        retcode = subprocess.call(commands, stdout = open(os.devnull, 'wb'), stderr = open(os.devnull, 'wb'))
        return retcode == 0
    except:
        return False
