import yaml
import time

__options = {}
__refresh = 0


def options():
    global __options
    global __refresh
    if time.time() - __refresh > 30:
        __options = yaml.load(open('config/options.yml', 'r'))
        __refresh = time.time()
        __options = __options or {}
    return __options
