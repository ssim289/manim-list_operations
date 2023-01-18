from pathlib import Path
import tomli

_DEFAULT_CONFIG = Path(__file__).parent / "default_config.toml"
CONFIG = {}

def load_config(path: Path):
    with open(path, "rb") as con:
        data = tomli.load(con)
    CONFIG.update(**data)

load_config(_DEFAULT_CONFIG)