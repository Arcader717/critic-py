import re
from typing import Iterable

from ..util import io, printing

# Regex
CSS_COMMENT = re.compile(r"/\*[\s\S]*?\*/", re.DOTALL)

class CSSParser:

    def __init__(self):
        self.data: dict[str, dict[str, str]] = {}

    def _comments(self, css: str) -> str:
        css = CSS_COMMENT.sub("", css)
        css = css.replace("\n", "").strip(" ")
        return css

    def _parse(self, css: str) -> dict[str, dict[str, str]]:
        tokens: list[tuple[str, str]] = []
        buffer = ""
        for c in css:
            if c in "{}":
                if buffer.strip():
                    tokens.append(("text", buffer.strip()))
                    buffer = ""
                tokens.append(("brace", c))
            else:
                buffer += c
        if buffer.strip():
            tokens.append(("text", buffer.strip()))

        stack = []
        rules: dict[str, str] = {}

        def combine_selectors(parents, child):
            output = []
            child_parts = [p.strip() for p in child.split(",")]
            parent_parts = [p.strip() for p in parents.split(",")] if parents else [""]
            for p in parent_parts:
                for c in child_parts:
                    if "&" in c:
                        output.append(c.replace("&", p).strip())
                    else:
                        if p:
                            output.append((p + " " + c).strip())
                        else:
                            output.append(c.strip())
            return ", ".join(output)

        i = 0
        while i < len(tokens):
            tokType, tokValue = tokens[i]
            if tokType == "text":
                if i + 1 < len(tokens) and tokens[i+1] == ("brace", "{"):
                    p = stack[-1][0] if stack else ""
                    full_sel = combine_selectors(p, tokValue)
                    stack.append((full_sel, []))
                    i += 2
                    continue
                if stack:
                    stack[-1][1].append(tokValue)
            elif tokType == "brace" and tokValue == "}":
                sel, decls = stack.pop()
                if decls:
                    rule_body = " ".join(d.rstrip(";") + ";" for d in decls)
                    rules[sel] = rule_body
            i += 1
        data: dict[str, dict[str, str]] = {}
        for selector, properties in rules.items():
            props = properties.split(";", 1)
            data[selector] = {}
            for prop in props:
                if prop == "":
                    continue
                key, value = prop.split(":", 1)
                data[selector.strip()][key.strip()] = value.strip()
        self.data = data
        return data

    def feed(self, css: str) -> str:
        css = self._comments(css)
        data = self._parse(css)
        return self._serialize(data)

    def __iter__(self) -> Iterable[dict[str, str]]: # Used for checking every property and value (analysis)
        for selector, properties in self.data.items():
            for property, value in properties.items():
                yield {"selector": selector, "property": property, "value": value}

    def _serialize(self, data: dict[str, dict[str, str]]) -> str:
        css: str = ""
        for selector, properties in data.items():
            css += selector + "{"
            css += ";".join([f"{key}:{value}" for key, value in properties.items()])
            css += "}"
        return css


def parse(file_type: str, write: bool = True) -> None:
    files: list[str] = io.files(file_type)
    for file in files:
        printing.verbose(f"Parsing {file}...")
        with open(file, "r+") as f:
            data = f.read()
            if file_type == "css":
                parser = CSSParser()
                data = parser.feed(data)
                printing.cli(f"Parsed and minified {file}")
            else:
                raise ValueError(f"Language '{file_type}' is not supported")
            if write:
                f.seek(0)
                f.write(data)
                f.truncate()
