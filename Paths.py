import os
import Args

home = os.path.expanduser("~")

deps = home + "/.deps"
dev = home + "/dev"
work = dev + "/work"

tes = work + "/tes"
glove = tes + "/glove"

atom = work + "/atom"

my = dev + "/my"

money = my + "/money"

repo_root = "https://github.com/vladasz/"
#repo_root = "git@github.com:VladasZ/"

#git@github.com:VladasZ/test_engine.git

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

my_projects = {
    home + '/dev/my/LastTime'    : repo_root + 'LastTime.git',
    home + '/dev/my/SquareBalls' : repo_root + 'SquareBalls.git',

    home + '/dev/my/money/MoneyCommon' : repo_root + 'MoneyCommon.git',
    home + '/dev/my/money/MoneyServer' : repo_root + 'MoneyServer.git',

    home + '/dev/my/square_editor' : repo_root + 'square_editor.git',

    home + '/dev/my/money/HabitServer' : repo_root + 'HabitServer.git',
}

tesla_projets = {
    home + '/dev/work/tes/teslasuit-studio'    : 'https://gitlab.vrweartek.com/software/teslasuit-studio.git',
    home + '/dev/work/tes/glove/GloveCommon'   : 'https://gitlab.vrweartek.com/Research/GloveCommon.git',
    home + '/dev/work/tes/glove/glovefirmware' : 'https://gitlab.vrweartek.com/Research/glovefirmware.git',
    home + '/dev/work/tes/glove/GloveSoftware' : 'https://gitlab.vrweartek.com/Research/GloveSoftware.git',
    home + '/dev/work/tes/glove/GloveUnity'    : 'https://gitlab.vrweartek.com/Research/gloveunity.git',
    home + '/dev/work/tes/glove/node'          : 'https://gitlab.vrweartek.com/firmware/tglove-node'
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
