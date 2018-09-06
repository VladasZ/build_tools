import Shell
import System
import Browser
import Compiler
import Application

print(Compiler.default().name)
print(System.platform)

Shell.run(['cmake', '--version'])

print('helloooyy')


Browser.open('google.com')
