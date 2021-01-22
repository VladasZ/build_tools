import os
import Shell


def run():
    Shell.run(['make', '-j' + str(os.cpu_count())])
