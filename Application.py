import File
import Shell
import Paths
import System

class Application:

    def __init__(self, path):
        self.path = path
        self.name = File.get_name(path)

    def run(self, parameters = ''):
        Shell.run([self.path, parameters])

browser = Application(Paths.browser())

