import argparse

from .core import parse
from .util import printing
from .util import io
from .util.conf import config

def build_parser() -> argparse.ArgumentParser:

    cli = argparse.ArgumentParser(
        "critic",
        description="A neat pure-python tool to prepare your static files for deployment"
    )

    logs = cli.add_mutually_exclusive_group()
    logs.add_argument("-v", "--verbose", action="store_true", help="Increase output")
    logs.add_argument("-q", "--quiet", action="store_true", help="Silence all output")
    subs = cli.add_subparsers(dest="command")

    mini = subs.add_parser("minify", prefix_chars="-+", help="Minify your files")
    mini.add_argument(
        "type",
        choices=["css", "all"],
        default="all",
        nargs="?",
        help="The file type to use",
        metavar="<file type>"
    )
    mini.add_argument(
        "-d", "--demo",
        action="store_true",
        help="Displays files that would be affected, without doing anything"
    )
    mini.add_argument(
        "-l", "--list-patterns", action="store_true",
        help="List the patterns currently saved"
    )
    mini.add_argument(
        "+p", "+pattern", action="extend", nargs="+", type=lambda x: ("+", x),
        help="Add a new pattern", metavar="<glob>"
    )
    mini.add_argument(
        "-p", "-pattern", action="extend", nargs="+",
        type=lambda x: ("-", x), help="Drop a pattern",
        metavar="<glob>"
    )

    return cli

def main(argv=None) -> int:
    cli = build_parser()
    args = cli.parse_args(argv)

    if getattr(args, "verbose", False):
        config["verbose"] = True
    if getattr(args, "quiet", False):
        config["quiet"] = True

    min: bool = args.command == "minify"

    if min:
        ft: str = args.type.lower()
        css: bool = ft in ["css", "all"]
        if args.demo:
            if css:
                for file in io.files("css"):
                    printing.cli("Minified " + file)
            cli.exit()
        elif args.list_patterns:
            if css:
                for pattern in io.get_patterns("css"):
                    printing.cli("CSS: " + pattern)
            cli.exit()
        elif getattr(args, "p", False):
            dynamic_file_type = False
            if ft == "all":
                dynamic_file_type = True
            for pattern in args.p:
                if dynamic_file_type:
                    ft = pattern[1].rsplit(".", 1)[1]
                    if ft not in ["css"]:
                        raise TypeError(f"The pattern '{pattern[1]}' is not a valid language (one of 'css')")
                if pattern[0] == "+":
                    io.add_pattern(ft, pattern[1])
                elif pattern[0] == "-":
                    io.drop_pattern(ft, pattern[1])
                cli.exit()
        else:
            if css and config.get("css"):
                parse("css")
            cli.exit()

    print(cli.format_help())
    cli.exit()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
