.. critic-py documentation master file, created by
   sphinx-quickstart on Sun Nov 23 10:27:10 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

critic-py
=========

**critic** is a neat pure-python tool for preparing your static files for deployment

Description
-----------

**critic** was legitimately made out of boredom. Considering my main project at the time was failing, and I had a number of restrictions that finally clamped down on it and made it impossible to use it. So I decided to make something else, to help with issues that might've caused the original problem. And I really wanted to make a CLI tool lmao

**critic** currently only comes with a *minifier*, but there are plans for *static compression*, and *analysis*. It's mainly meant to be used in a CI environment, because of the destructive potential, but certain functions can be used without requiring a search on how to revert to a previous commit on [StackOverflow](https://stackoverflow.com)

Installation
------------

use a package manager like `pip`_ to install critic. 
This assumes you have `pip`, if not you can check out `a guide from python`_ for installing `pip` onto your machine


.. code-block:: bash

   $ pip install critic-py

Also, this is a package that relies only on the python stdlib, so no need to worry about extensive dependencies!

Usage
-----

Currently, you can only minify CSS, and even then, it's lacking a lot of features. But, it handles nested CS, and I love nested CSS! |:heart:|

To use it, just type in:

.. code-block:: bash

   $ critic minify css

Roadmap
-------

I've got big dreams for this project. 
Not sure how many of them I'll reach, 
but I can at least get disappointed in myself when I add yet another feature out of boredom before I've completed one that's been on here since forever


* |:white_check_mark:| CSS Parser
* |:x:| CSS Minification
   * |:white_check_mark:| Remove comments
   * |:white_check_mark:| Remove unnecessary whitespace
   * |:x:| Combining duplicate rules
   * |:x:| Combining selectors with duplicate declarations
   * |:x:| Leading zeros, and trailing units (for things like `0.5px` to `.5px`, and `0px` to `0` respectively)
* |:x:| Documentation
* |:x:| Tests for the CLI (With pytest!)
* |:x:| HTML Parser
* |:x:| HTML Minification
   * |:x:| Remove Comments
   * |:x:| Remove unnecessary whitespace
   * |:x:| Others I haven't thought of yet
* |:x:| JS Parsser
* |:x:| JS Minification
   * |:x:| JS Mangling
   * |:x:| Sourcemaps
   * |:x:| Remove unnecessary whitespace
   * |:x:| Insert semicolons where needed to prevent JS Automatic Semicolon Insertion

Contributing
------------

Check out the `Code of Conduct`_ and `Contributing`_ guidlines when you want to contribute! 
For major changes, please open an issue first to discuss you would like to change.

Also, update tests as appropriate

License
-------

`MIT`_

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quickstart
   cli


.. _pip: https://pip.pypa.io/en/stable
.. _a guide from python: https://packaging.python.org/en/latest/tutorials/installing-packages/
.. _Code of Conduct: https://github.com/Arcader717/critic-py/blob/main/CODE_OF_CONDUCT.md
.. _Contributing: https://github.com/Arcader717/critic-py/blob/main/CONTRIBUTING.md
.. _MIT: https://choosealicense.com/licenses/mit/