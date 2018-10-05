import os
import sys
import shutil
import getpass
import zipfile
import urllib.request
import Args
import Shell

home = os.path.expanduser("~")
__build_config_dir = home + '/.build_config'

def full_path(path = '.'):
    return os.path.abspath(path)

def is_root(path = '.'):
    return full_path(path) == full_path(path + '/..')

def get_files(path = '.'):
    return os.listdir(path)

def file_name(name):
    return os.path.basename(name)

def get_name(name):
    return os.path.splitext(file_name(name))[0]

def config_path():
    mkdir(__build_config_dir)
    return __build_config_dir

def mkdir(name):
    if not os.path.exists(name):
        os.makedirs(name)

def cd(path):
    os.chdir(path)

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
    print('Downloading: ' + url)
    urllib.request.urlretrieve(url, file_name, reporthook)
