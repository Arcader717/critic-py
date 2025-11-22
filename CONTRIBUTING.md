# Contributing to critic

Thanks for your interest in **critic**! It means a lot to me!
This project is FOSS and contributions are welcome, whether through code, bug reports, docs, tests, or feature ideas.

This is a guide that will explain how to get started.

---

## Ways to Contribute

You can contribute in a number of ways:

- **Reporting Bugs** (things like unexpected behaviors, crashes, or incorrect/invalid output)
- **Suggesting Enhancements** (like new features or improvements
- **Improving Documentation**
- **Submitting Pull Requests** for fixes or new features
- **Helping to review existing issues and PRs**

If you aren't sure if something is appropriate, open an issue and ask.

---

## Code of Conduct

All contributors must follow the project's [Code of Conduct](.github/CODE_OF_CONDUCT.md).

---

## Getting Started

These steps assume you have Python 3.10+ installed and git installed

1. **Fork the repository** on Github
2. **Clone your fork**:

   ```bash
   git clone https://github.com/<your-username>/critic-py.git
   cd critic
   ```

3. **Create a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

4. **Install in editable mode** with dev tools:
   
   ```bash
   pip install -e ".[dev]"
   ```

---

## Development Guidelines

### Branching

Use descriptive branch names:

- `fix/css-selector-crash`
- `feature/parser-speedup`
- `docs/translate-german`

### Commit Messages

Keep commits focused, and use short, descriptive messages. There is no need to explain why or what exactly you changed, as it should be understandable by looking at your diffs

- `Fix parsing of nested selectors`
- `Add optional dependencies for analyze`
- `Translate README.md to German`

### Code Style

The project follows certain styles. You don't really need to worry about it, until it's pushed to the main repo. For that we use the following tools

- **[Black](https://black.readthedocs.io/en/stable/getting_started.html)** for **formatting**
- **[Ruff](https://docs.astral.sh/ruff/linter/)** for **linting**
- **[mypy](https://mypy.readthedocs.io/en/stable/getting_started.html)** for static type checking

Most of these tools will already have configurations, so you can run them without issue.

For example, you can run:

```bash
black .
ruff check .
mypy .
```

and if it all passes, you should be good to go!

---

## Submitting Pull Requests

1. Make that your PR:
   - is focused
   - includes tests when relevant
   - updates documentation if needed
   - follows the [Code Style](#code-style) described above
2. Push your branch and open a PR on Github and:
   - explain *what* you changed and *why*
   - link to any related issues
   - keep all discussion focused, constructive, and respectful 
3. I'll review your PR, and may:
   - merge it directly
   - ask for changes
   - discuss alternative approaches
   - close it if it's out of scope

---

## Reporting Bugs

When reporting a bug, please include:

- What you expected to happen
- What actually happened
- Steps to reproduce
- Minimal code sample, if possible
- Python version and OS

---

## Suggesting Features

Great ideas are welcome, so please open an issue describing:

- What the feature does
- Why it's useful
- Any technical considerations
- an optional example usage

---

## Project Structure

```
critic-py
├── src
│   ├── critic
│   │   ├── utils
│   │   │   ├── conf.py
│   │   │   ├── io.py
│   │   │   ├── other.py
│   │   │   └── defaults.toml
│   │   ├── langs
│   │   │   ├── __init__.py
│   │   │   ├── html.py
│   │   │   ├── css.py
│   │   │   └── js.py
│   │   ├── patterns
│   │   │   ├── html.txt
│   │   │   ├── css.txt
│   │   │   └── js.txt
│   │   ├── exceptions
│   │   │   ├── warnings.py
│   │   │   └── errors.py
│   │   ├── __init__.py
│   │   └── cli.py
│   └── pyproject.toml
├── tests/
├── docs/
├── README.md
├── CODE_OF_CONDUCT.md
└── LICENSE
```

---

## License

By submitting a contribution, you agree that your work will be licensed under the same license as the project (**The MIT License**)

See: [LICENSE](LICENSE)

---

Thanks again for taking the time out of your day to contribute!
