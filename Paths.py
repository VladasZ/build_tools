import Debug
import System

def browser():
    if System.is_windows:
        return 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    raise Debug.not_implemented()
