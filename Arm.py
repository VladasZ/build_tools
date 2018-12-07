import Shell

def run(params= []):
    Shell.run(["arm-none-eabi-gcc"] + params)


run(["-v"])
