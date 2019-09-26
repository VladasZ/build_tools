import Cpp
import File
import Args
import Shell
import System


def build():
    command = ["make"]
    if Args.hand:
        command += ["HAND_BUILD=-DHAND_BUILD"]
    Shell.run(command)
    print("Build successful")


def flash():
    print("Uploading arm build")

    board_name = "NODE_F446RE"

    if not Args.hand:
        board_name += " 1"

    path_prefix = "/Volumes/" if System.is_mac else "/media/vladas/"
    File.copy("BUILD/Nucleo_blink_led.bin", path_prefix + board_name + "/Nucleo_blink_led.bin")


def run():
    clean()
    build()
    flash()


def clean():
    File.rm("BUILD")
