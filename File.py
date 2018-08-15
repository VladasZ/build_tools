import os

def mkdir(name):
	if not os.path.exists(name):
    	os.makedirs(name)

def cd(path):
	os.chdir(path)
