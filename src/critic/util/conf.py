import os
import glob
import tomllib
from typing import Any
from pathlib import Path
from importlib import util
from importlib.resources import files

APP_NAME = "critic"

BConfVals = str|int|bool

ConfDict = dict[str, BConfVals|dict[str, BConfVals|dict[str, BConfVals|dict[str, BConfVals]]]]


def get_config_dir() -> Path:
    home = Path.home()
    if os.system == "nt":
        base = os.getenv("APPDATA")
        if base:
            return Path(base) / APP_NAME
        return home / "AppData" / "Local" / APP_NAME
    if os.system == "darwin":
        return home / "Library" / "Application Support" / APP_NAME
    xdg = os.getenv("XDG_CONFIG_HOME")
    if xdg:
        return Path(xdg) / APP_NAME
    return home / ".config" / APP_NAME

CONFIG_DIR = get_config_dir()
PATTERNS_DIR = CONFIG_DIR / "patterns"

def ensure_user_patterns() -> None:
    PATTERNS_DIR.mkdir(parents=True, exist_ok=True)
    defaults_dir = files("critic.core") / "patterns"
    for entry in defaults_dir.iterdir():
        if entry.name.endswith(".txt"):
            target = PATTERNS_DIR / entry.name
            if not target.exists():
                text = entry.read_text(encoding="utf-8")
                target.write_text(text, encoding="utf-8")

def _parse_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]

def load_patterns(name: str) -> list[str]:
    user_file = PATTERNS_DIR / name
    if user_file.exists():
        return _parse_lines(user_file.read_text(encoding="utf-8")) # Continue here

def test_deps() -> tuple[bool, bool]:
    numpy: bool = util.find_spec("numpy") is not None
    pandas: bool = util.find_spec("pandas") is not None
    return numpy, pandas

def start_traversal(data: dict, default: dict) -> ConfDict:
    """Returns the userdata, plus any keys missing from user data are added and set to the default value"""
    default_keys = set(default.keys())
    missing_keys = default_keys - set(data.keys())
    for key in missing_keys:
        data[key] = default[key]
    for key in data:
        if isinstance(data[key], dict):
            data[key] = traverse(data[key], default[key])
    return data

def traverse(data: dict, default: dict):
    def_keys = set(default.keys())
    missing_keys = def_keys - set(data.keys())
    for key in missing_keys:
        data[key] = default[key]
    for key in data:
        if isinstance(data[key], dict):
            data[key] = traverse(data[key], default[key])
    return data
    

class Config:
    file: bool
    data: ConfDict
    def __init__(self):
        files = glob.glob("**/critic.toml")
        files.extend(glob.glob("critic.toml"))
        userData = {}
        if len(files) > 1:
            raise ValueError("Multiple config files for critic found. Please ensure there is only one critic.toml file in your project, are you are in the proper Current Working Directory")
        if len(files) == 0:
            self.data = tomllib.load(open(os.path.join(os.path.dirname(__file__), "defaults.toml"), "rb"))
        else:
            self.file = True
            f = open(files[0], "rb")
            defaults = tomllib.load(open(os.path.join(os.path.dirname(__file__), "defaults.toml"), "rb"))
            userData = tomllib.load(f)
            self.data = start_traversal(userData, defaults)
                

    def get(self, key: str) -> Any:
        if key in self.data:
            return self.data[key]

    def set(self, key: str, value: Any) -> None:
        self.data[key] = value

    def delete(self, key: str) -> None:
        del self.data[key]

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, key: str) -> Any:
        self.get(key)

    def __setitem__(self, key: str, value: Any) -> None:
        self.set(key, value)

    def __delitem__(self, key: str) -> None:
        self.delete(key)

    def __contains__(self, key: str) -> bool:
        return key in self.data

config = Config()
