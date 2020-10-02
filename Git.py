import File
import Debug
import Shell


def root_dir(path='.'):
    _path = path
    while not File.is_root(_path):
        if File.exists(_path + '/.projectile'):
            super_project = Shell.get(["git", "rev-parse", "--show-superproject-working-tree"])
            if super_project:
                return super_project
            return File.full_path(_path)
        _path = _path + "/.."
    Debug.throw("Git root directory not found for path: " + File.full_path(path))


def clone(link, destination, delete_existing=False, recursive=False, ignore_existing=False):

    if delete_existing:
        if has_changes(destination):
            Debug.throw("Can not delete repository with changes at path: " + destination)
        else:
            File.rm(destination)

    if len(destination) > 0 and File.exists(destination):
        if ignore_existing:
            return
        Debug.throw("Git repository: " + link + " already exists for path: " + File.full_path(destination))

    command = ["git", "clone", link, destination]

    if recursive:
        command += ["--recursive"]

    Shell.run(command)


def pull(path):
    if not is_git_repo(path):
        Debug.info(path + " :not a git repo. Skipping.")
        return
    Shell.run_string("git -C " + path + " pull")


def is_git_repo(path) -> bool:
    return File.exists(path + "/.git")


def is_repo_string(path) -> str:
    return "Is a git repository" if is_git_repo(path) else "Is not a git repository"


def has_changes(path) -> bool:
    if not is_git_repo(path):
        return False
    return len(Shell.get(["git", "-C", File.full_path(path), "status", "-s"])) != 0


def pring_folder_changes(path):
    for repo in File.get_files(path):
        if repo == ".DS_Store":
            continue
        if has_changes(path + "/" + repo):
            print(repo + " - has changes")


def pull_folder(path):
    for repo in File.get_files(path):
        if repo == ".DS_Store":
            continue
        full_path = path + "/" + repo
        if has_changes(full_path):
          Debug.throw(repo + " - has changes")
        pull(full_path)
