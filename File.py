import os
import sys
import shutil
import getpass
import zipfile
import urllib.request
import Args
import Shell

user_dir = os.path.expanduser("~")
__build_config_dir = user_dir + '/.build_config'

def config_path():
	mkdir(__build_config_dir)
	return __build_config_dir

def mkdir(name):
    if not os.path.exists(name):
        os.makedirs(name)

def cd(path):
    os.chdir(path)

#def chown(path):
#	if not platform.system() == 'Windows':
#		Shell.run(['sudo', 'chown', '-R', 'vladaszakrevskis', path])

def rm(path):
	if os.path.exists(path):
		shutil.rmtree(path)

def make(path):
	open(path, 'w+')

def exists(path):
	return os.path.exists(path)

def unzip(path, destination):    
    print('Unzipping: ' + path)
    with zipfile.ZipFile(path,"r") as zip_ref:
        zip_ref.extractall(destination)

def build_folder():
	if Args.make:
		return 'make'
	return 'build'

def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize:
            sys.stderr.write("\n")
    else:
        sys.stderr.write("read %d\n" % (readsofar,))

def download(url, file_name):
	print('Donwloading: ' + url)
	urllib.request.urlretrieve(url, file_name, reporthook)
