import Cpp
import File
import Shell
import System

def build():
    Shell.run(["make"])
    
def run():
    build()
    print("Uploading arm build")
    path_prefix = "/Volumes/" if System.is_mac else "/media/vladas/"
    File.copy("BUILD/Nucleo_blink_led.bin", path_prefix + "NODE_F446RE/Nucleo_blink_led.bin")
    
def clean():
    File.rm("BUILD")
