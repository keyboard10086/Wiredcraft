import configparser
import os
from .. import project_root_dir

config = None
def get_config_by_section_and_key(file_name, section_name, key):
    filepath = project_root_dir + "Wiredcraft_API" + os.sep + "config" + os.sep + file_name
    global config
    if config is None:
        config = configparser.ConfigParser()
    config.read(filepath, "utf-8")
    return config.get(section_name, key)