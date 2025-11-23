from .conf import config

def cli(obj: str) -> None:
    if not config.get("quiet"):
        print(obj)

def verbose(obj: str) -> None:
    if config.get("verbose"):
        print(obj)
