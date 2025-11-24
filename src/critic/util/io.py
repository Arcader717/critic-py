import glob
import warnings
from importlib.resources import files as pfiles

from . import printing
from .conf import get_patterns, save_patterns
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

def add_pattern(file_type: str, pattern: str) -> None:
    file_type = file_type.lower()
    if "~" in pattern:
        warnings.warn("Glob patterns starting with tilde expansion (starts with '~') are not supported and may cause unexpected behavior", UnsupportedGlobPatternWarning)
    if "{" in pattern or "}" in pattern:
        warnings.warn("Glob patterns containing brace expansion ('{' or '}') are not supported and may cause unexpected behavior", UnsupportedGlobPatternWarning)
    if "$" in pattern:
        warnings.warn("Glob patterns containing shell variable expansions ('$') are not supported and may cause unexpected behavior", UnsupportedGlobPatternWarning)
    if ".." in pattern:
        warnings.warn("Patterns containing parent directory references ('..') are not supported and may cause unexpected behavior", UnsupportedGlobPatternWarning)
    if "!" in pattern:
        warnings.warn("Patterns containing negations ('!') have iffy support in python and may cause unexpected behavior", UnsupportedGlobPatternWarning)
    if file_type not in ["css"]:
        raise ValueError("File type must be one of 'css'")
    patterns = get_patterns(file_type)
    patterns.append(pattern)
    save_patterns(file_type, patterns)
    printing.cli(f"Added pattern '{pattern}' to {file_type}")

def drop_pattern(file_type: str, pattern: str) -> None:
    patterns = get_patterns(file_type)
    for line in patterns:
        if line.strip() == pattern:
            patterns.remove(line)
            break
    save_patterns(file_type, patterns)
    printing.cli(f"Removed pattern '{pattern}' from {file_type} patterns")
    