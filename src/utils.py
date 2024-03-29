import pathlib

import pandas as pd
import yaml


BASE_PATH = pathlib.Path(__file__).parent.parent.resolve()


def load_yaml_config_file(fname: str):
    path = BASE_PATH / 'config' / f"{fname}.yml"
    with open(path, 'r') as f:
        ret = yaml.load(f.read(), Loader=yaml.FullLoader)
    return ret


def load_yaml_plot_config_file(base_name: str):
    path = BASE_PATH / 'config' / 'plots' / f"{base_name}.yml"
    with open(path, 'r') as f:
        ret = yaml.load(f.read(), Loader=yaml.FullLoader)
    return ret['figures'], ret['config']
