import Cpp
import File
import Shell

def build():
    Shell.run(["make"])
#    Shell.run(["arm-none-eabi-objcopy", "-O", "binary", "NUCLEO_F446RE/arm.elf", "NUCLEO_F446RE/arm.bin"])

def run():
    build()
    File.copy("BUILD/Nucleo_blink_led.bin", "/media/vladas/NODE_F446RE/Nucleo_blink_led.bin")
    
    
def clean():
    File.rm("BUILD")
