import os
import getpass
import Shell

def mkdir(name):
    if not os.path.exists(name):
        os.makedirs(name)

def cd(path):
    os.chdir(path)

def chown(path):
    Shell.run(['sudo', 'chown', '-R', 'vladaszakrevskis', path])
