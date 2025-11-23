import os
import glob
import warnings
from importlib.resources import files as pfiles

from . import printing
from ..errors import UnsupportedGlobPatternWarning

pattern_directory = pfiles("critic") / "core" / "patterns"

_PATS = {
    "css": (pattern_directory / "css.txt").read_text(encoding="utf-8").splitlines()
}

def files(file_type: str) -> list[str]:
    patterns: list[str] = []
    for p in get_patterns(file_type):
        f = glob.glob(p, recursive=True)
        patterns.extend(f)
    return patterns

def get_patterns(file_type: str) -> list[str]:
    if file_type.lower() not in ["css"]:
        raise ValueError("The file type must be one of 'css'")
    data = _PATS[file_type]
    return [line.strip() for line in data if line.strip()]

def add_pattern(file_type: str, pattern: str) -> None:
    if pattern.startswith("~"):
        warnings.warn("Glob patterns starting with tilde expansion (starts with '~') are not supported and may cause unexpected behavior", UnsupportedGlobPatternWarning)
    if "{" in pattern or "}" in pattern:
        warnings.warn("Glob patterns containing brace expansion ('{' or '}') are not supported and may cause unexpected behavior", UnsupportedGlobPatternWarning)
    if "$" in pattern:
        warnings.warn("Glob patterns containing shell variable expansions ('$') are not supported and may cause unexpected behavior", UnsupportedGlobPatternWarning)
    if ".." in pattern:
        warnings.warn("Patterns containing parent directory references ('..') are not supported and may cause unexpected behavior", UnsupportedGlobPatternWarning)
    if "!" in pattern:
        warnings.warn("Patterns containing negations ('!') have iffy support in python and may cause unexpected behavior", UnsupportedGlobPatternWarning)
    if file_type.lower() not in ["css"]:
        raise ValueError("File type must be one of 'css'")
    with open(pattern_directory + file_type.lower() + ".txt", "a") as f:
        f.write(pattern + "\n")
        printing.cli(f"Added pattern '{pattern}' from {file_type}")

def drop_pattern(file_type: str, pattern: str) -> None:
    with open(pattern_directory + file_type.lower() + ".txt", "r") as f:
        data = f.readlines()
    for line in data:
        if line.strip() == pattern:
            data.remove(line)
            break
    with open(pattern_directory + file_type.lower() + ".txt", "w") as f:
        f.writelines(data)
        printing.cli(f"Removed pattern '{pattern}' from {file_type} patterns")
    