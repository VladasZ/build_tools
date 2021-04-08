import os
import Args
import Debug


def _get_home():
    if "HOME" in os.environ:
        return os.environ["HOME"]
    return os.path.expanduser("~")

home = _get_home()

deps = home + "/.deps"
rdeps = home + "/.rdeps"
dev = home + "/dev"
work = dev + "/work"
sand = dev + "/sand"

tes = work + "/tes"
glove = tes + "/glove"

atom = work + "/atom"

my = dev + "/my"

money = my + "/money"

repo_root = "https://github.com/vladasz/"

if Args.ssh:
    repo_root = "git@github.com:VladasZ/"

main_projects = {
    home + '/.emacs.d': repo_root + '.emacs.d.git',
    home + '/.shell'  : repo_root + '.shell.git',
    home + '/deploy'  : repo_root + 'deploy.git',

    home + '/.deps/build_tools' : repo_root + 'build_tools.git',
    home + '/.deps/cpp_utils'   : repo_root + 'cpp_utils.git',
    home + '/.deps/geometry'    : repo_root + 'geometry.git',
    home + '/.deps/gl_wrapper'  : repo_root + 'gl_wrapper.git',
    home + '/.deps/image'       : repo_root + 'image.git',
    home + '/.deps/scene'       : repo_root + 'scene.git',
    home + '/.deps/smon'        : repo_root + 'smon.git',
    home + '/.deps/test_engine' : repo_root + 'test_engine.git',
    home + '/.deps/ui'          : repo_root + 'ui.git'
}

sand_projects = {
    sand + "/rust_sand" : repo_root + 'rust_sand.git'
}

my_projects = {
    home + '/dev/my/money/HabitServer' : repo_root + 'HabitServer.git',
}

tesla_root = "https://gitlab.vrweartek.com/"

if Args.ssh:
    tesla_root = "git@gitlab.vrweartek.com:"

tesla_projets = {
    home + '/dev/work/tes/teslasuit-studio'    : tesla_root + "software/teslasuit-studio.git",
    # home + '/dev/work/tes/glove/GloveCommon'   : tesla_root + "Research/GloveCommon.git",
    # home + '/dev/work/tes/glove/glovefirmware' : tesla_root + "Research/glovefirmware.git",
    # home + '/dev/work/tes/glove/GloveSoftware' : tesla_root + "Research/GloveSoftware.git",
    home + '/dev/work/tes/GloveUnity'    : tesla_root + "Research/gloveunity.git"
    # home + '/dev/work/tes/glove/node'          : tesla_root + "firmware/tglove-node"
}

atom_projects = {
    home + '/dev/work/atom/apg-ios' : 'https://gitlab.atomichronica.com/apg/app.git'
}

args_projects = main_projects

all_projects = {}
all_projects.update(main_projects)
all_projects.update(tesla_projets)
all_projects.update(atom_projects)

if Args.my:
    args_projects.update(my_projects)

if Args.tesla:
    args_projects.update(tesla_projets)

if Args.atom:
    args_projects.update(atom_projects)

if Args.sand:
    args_projects.update(sand_projects)
