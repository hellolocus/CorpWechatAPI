import configparser
import sys,os
current_path = sys.path.append(os.path.dirname(sys.modules[__name__].__file__))
print(current_path)
def  read_config(cfg_file):
    config = configparser.ConfigParser()
    config.read(cfg_file,encoding='utf-8')
    return config
sys_cfg = read_config('../cfg/config.cfg')
