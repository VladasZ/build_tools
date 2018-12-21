import Cpp
import File
import Shell

def build():
    Shell.run(["make"])
    Shell.run(["arm-none-eabi-objcopy", "-O", "binary", "NUCLEO_F446RE/arm.elf", "NUCLEO_F446RE/arm.bin"])

def run():
    build()
    File.copy("NUCLEO_F446RE/arm.bin", "/media/vladas/NODE_F446RE/arm.bin")
    
    
def clean():
    File.rm("NUCLEO_F446RE")
