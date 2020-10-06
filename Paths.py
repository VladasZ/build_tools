import os

home = os.path.expanduser("~")

deps = home + "/.deps"
dev = home + "/dev"
work = dev + "/work"

tes = work + "/tes"
glove = tes + "/glove"

atom = work + "/atom"

my = dev + "/my"


projects = {'~/.emacs.d': 'https://github.com/vladasz/.emacs.d',
            '~/.shell'  : 'https://github.com/vladasz/.shell',
            '~/deploy'  : 'https://github.com/vladasz/deploy',

            '~/.deps/build_tools' : 'https://github.com/vladasz/build_tools',
            '~/.deps/cpp_utils'   : 'https://github.com/vladasz/cpp_utils',
            '~/.deps/geometry'    : 'https://github.com/vladasz/geometry',
            '~/.deps/gl_wrapper'  : 'https://github.com/vladasz/gl_wrapper',
            '~/.deps/image'       : 'https://github.com/vladasz/image',
            '~/.deps/scene'       : 'https://github.com/vladasz/scene',
            '~/.deps/smon'        : 'https://github.com/vladasz/smon',
            '~/.deps/test_engine' : 'https://github.com/vladasz/test_engine',
            '~/.deps/ui'          : 'https://github.com/vladasz/ui',

            '~/dev/work/tes/teslasuit-studio'    : 'https://gitlab.vrweartek.com/software/teslasuit-studio.git',
            '~/dev/work/tes/glove/GloveCommon'   : 'https://gitlab.vrweartek.com/Research/GloveCommon.git',
            '~/dev/work/tes/glove/glovefirmware' : 'https://gitlab.vrweartek.com/Research/glovefirmware.git',
            '~/dev/work/tes/glove/GloveSoftware' : 'https://gitlab.vrweartek.com/Research/GloveSoftware.git',
            '~/dev/work/tes/glove/GloveUnity'    : 'https://gitlab.vrweartek.com/Research/gloveunity.git',

            '~/dev/my/LastTime'    : 'https://github.com/vladasz/LastTime',
            '~/dev/my/SquareBalls' : 'https://github.com/vladasz/SquareBalls',

            '~/dev/work/atom/apg-ios' : 'https://gitlab.atomichronica.com/apg/app.git'}
