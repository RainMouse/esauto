import os
import json

CONFIG = {}
CONFIG_PATH = os.path.join('./config', 'config.json')

def _init():
    global CONFIG
    CONFIG = json.load(open(CONFIG_PATH))

def _get_value(name : str) :

    return CONFIG[name]
    

