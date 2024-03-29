import os
import sys
import shutil
import zipfile
import urllib.request
import Paths
import Debug

__build_config_dir = Paths.home + '/.build_config'


def is_file(path):
    return os.path.isfile(path)


def rm(path):
    Debug.info("Deleting: " + path)
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)


def convert_path(path):
    if os.path.sep != '/':
        path = path.replace(os.path.sep, '/')
    return path


def copy(src, dst):
    Debug.info("Copying:\n" + src + " to:\n" + dst)
    if is_file(src):
        shutil.copyfile(src, dst)
    else:
        shutil.copytree(src, dst)


def full_path(path='.'):
    return convert_path(os.path.abspath(os.path.expanduser(path)))


def is_root(path='.'):
    return full_path(path) == full_path(path + '/..')


def get_files(path='.'):
    return os.listdir(full_path(path))


def extension(path):
    return os.path.splitext(path)[1]


def folder_name(path="."):
    return os.path.basename(full_path(path))


def without_file_name(path):
    return os.path.dirname(path)


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


def pwd():
    return full_path('.')


def make(path):
    open(path, 'w+')


def exists(path) -> bool:
    return os.path.exists(full_path(path))


def zip(file):
    zip = zipfile.ZipFile(file + ".zip", 'w', zipfile.ZIP_DEFLATED)
    zip.write(file)
    zip.close()


def unzip(path, destination):
    print('Unzipping: ' + path)
    with zipfile.ZipFile(path, "r") as zip_ref:
        zip_ref.extractall(destination)


def parent_folder(path='.'):
    return os.path.basename(full_path(path + '/..'))


def get_project_name():
    path = full_path('.')
    while True:
        if is_root(path):
            return ""
        if parent_folder(path) == "source":
            return os.path.basename(path)
        path = full_path(path + "/..")

        print(path)
        print(path + "/..")


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
    mkdir(without_file_name(file_name))
    urllib.request.urlretrieve(url, file_name)


def write(path, text):
    path = full_path(path)
    rm(path)
    file = open(path, "w+")
    file.write(text)
    file.close()


def append(path, text):
    path = full_path(path)
    file = open(path, "a+")
    file.write(text)
    file.close()


def get_lines(path):
    with open(path) as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines


def cat(path):
    print(open(path).read())


def fold_user(path):
    return path.replace(os.path.expanduser('~'), '~', 1)
