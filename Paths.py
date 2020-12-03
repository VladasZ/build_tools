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


main_projects = {
    home + '/.emacs.d': 'https://github.com/vladasz/.emacs.d',
    home + '/.shell'  : 'https://github.com/vladasz/.shell',
    home + '/deploy'  : 'https://github.com/vladasz/deploy',

    home + '/.deps/build_tools' : 'https://github.com/vladasz/build_tools',
    home + '/.deps/cpp_utils'   : 'https://github.com/vladasz/cpp_utils',
    home + '/.deps/geometry'    : 'https://github.com/vladasz/geometry',
    home + '/.deps/gl_wrapper'  : 'https://github.com/vladasz/gl_wrapper',
    home + '/.deps/image'       : 'https://github.com/vladasz/image',
    home + '/.deps/scene'       : 'https://github.com/vladasz/scene',
    home + '/.deps/smon'        : 'https://github.com/vladasz/smon',
    home + '/.deps/test_engine' : 'https://github.com/vladasz/test_engine',
    home + '/.deps/ui'          : 'https://github.com/vladasz/ui'
}

my_projects = {
    home + '/dev/my/LastTime'    : 'https://github.com/vladasz/LastTime',
    home + '/dev/my/SquareBalls' : 'https://github.com/vladasz/SquareBalls'
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


    # - sudo apt update
    # sudo apt install xorg-dev libglu1-mesa-dev libgl1-mesa-dri libgl1-mesa-dev libx11-xcb-dev libxcb-render0-dev libxcb-render-util0-dev libxcb-xkb-dev libxcb-icccm4-dev libxcb-image0-dev libxcb-keysyms1-dev libxcb-randr0-dev libxcb-shape0-dev libxcb-sync-dev libxcb-xfixes0-dev libxcb-xinerama0-dev libglu1-mesa-dev