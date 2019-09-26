import time

_stamp = time.time()


def stamp():
    global _stamp
    _stamp = time.time()


def duration():
    _duration = time.time() - _stamp
    return str(_duration) + " seconds"
