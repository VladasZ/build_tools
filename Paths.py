import Debug
import System

def browser():
    if System.isWindows:
        return 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    raise Debug.not_implemented()
