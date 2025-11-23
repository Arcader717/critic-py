# critic-py

**critic** is a neat pure-python tool for preparing your static files for deployment

## Description

**critic** was legitimately made out of boredom. Considering my main project at the time was failing, and I had a number of restrictions that finally clamped down on it and made it impossible to use it. So I decided to make something else, to help with issues that might've caused the original problem. And I really wanted to make a CLI tool lmao

**critic** currently only comes with a *minifier*, but there are plans for *static compression*, and *analysis*. It's mainly meant to be used in a CI environment, because of the destructive potential, but certain functions can be used without requiring a search on how to revert to a previous commit on [StackOverflow](https://stackoverflow.com)

## Installation

use a package manager like [pip](https://pip.pypa.io/en/stable) to install critic. 
This assumes you have `pip`, if not you can check out [a guide by python](https://packaging.python.org/en/latest/tutorials/installing-packages/) for installing `pip` onto your machine

```bash
pip install critic
```

Also, this is a package that relies only on the 

## Usage

Currently, you can only minify CSS, and even then, it's lacking a lot of features. But, it handles nested CSS! And I love nested CSS :heart:

```bash
critic minify css
```

## Roadmap

I've got big dreams for this project. 
Not sure how many of them I'll reach, 
but I can at least get disappointed in myself when I add yet another feature out of boredom before I've completed one that's been on here since forever

- [x] CSS Parser
- [ ] CSS Minification
  - [x] Remove comments
  - [x] Remove unnecessary whitespace
  - [ ] 

## Contributing

Check out the [Code of Conduct](CODE_OF_CONDUCT.md) and [Contributing](CONTRIBUTING.md) guidlines when you want to contribute! 
For major changes, please open an issue first to discuss you would like to change.

Also, update tests as appropriate

## License

[MIT](https://choosealicense.com/licenses/mit/)

