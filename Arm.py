import Cpp
import File
import Shell

def build():
    Shell.run(["make"])
    
def run():
    build()
    File.copy("BUILD/Nucleo_blink_led.bin", "/media/vladas/NODE_F446RE/Nucleo_blink_led.bin")
    
def clean():
    File.rm("BUILD")
