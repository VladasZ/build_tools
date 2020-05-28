import os
import Shell


def run(path='.'):
    Shell.run(['make', '-j' + str(os.cpu_count())])
