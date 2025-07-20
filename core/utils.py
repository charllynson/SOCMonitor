import yaml
from loguru import logger

def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def save_json(path, data):
    import json
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        logger.info(f"Dados salvos em: {path}")