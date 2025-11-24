import pytest

from src.critic.cli import main
from src.critic.util import io

class CLI:
    def __call__(self, *commands: str):
        options = list(commands)
        with pytest.raises(SystemExit):
            main(options)


@pytest.fixture
def cli():
    c = CLI()
    return c

class Patterns:
    ftype: str

    def get(self) -> list[str]:
        return io.get_patterns(self.ftype)

    def overwrite(self, *patterns: str) -> None:
        for p in io.get_patterns(self.ftype):
            io.drop_pattern(self.ftype, p)
        for p in patterns:
            io.add_pattern(self.ftype, p)

@pytest.fixture
def css_patterns():
    pats = Patterns()
    pats.ftype = "css"
    return pats
