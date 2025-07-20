import yaml
from loguru import logger as log

def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)
