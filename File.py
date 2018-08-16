import os
import getpass
import Shell
import System

def mkdir(name):
    if not os.path.exists(name):
        os.makedirs(name)

def cd(path):
    os.chdir(path)

def chown(path):
	if System.isWindows():
		return
	Shell.run(['sudo', 'chown', '-R', 'vladaszakrevskis', path])
