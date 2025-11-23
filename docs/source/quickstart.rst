Quickstart
==========

Installation
------------

To get started, ensure you have an acceptable python version (eg. 3.11+). 
Then make sure you have `pip`_

.. termynal::

   $ pip install -U critic-py
   -->
   Successfully installed critic-py

Considering `critic-py` doesn't require any dependencies other than the `python standard library`_,
all you should be installing is the latest version of critic-py

Setup
-----

Technically, there is no setup required, but I would like to point out something.
I made this with Flask in mind, so I'm sorry if this doesn't apply to everyone |:sweat_smile:|

However, I did realize early on that this could be a whole lot more general than I previously thought, so I planned for more general patterns

For this instance, we'll pretend this is a Flask application, using the ``static`` directory, and the css you want to minify is under the ```styles``` in that same ``static`` directory

So if your project directory looks similar to:

.. code-block::

   .
   ├── templates/
   ├── static/
   │   ├── styles/
   │   │   ├── app.css
   │   │   └── ...
   │   └── scripts/
   │       └── ...
   ├── wsgi.py
   ├── leave_me_alone.css
   └── app.py

Then the default pattern might not be specific enough for you. You can remove the default, then add a new one that's more specific.

.. note::

   I'd highly recommend using the ``-d`` or ``--demo`` option when you're unsure what files could be affected by minifying

.. termynal::

   $ critic minify -d css
   Minified static/styles/app.css (demo)
   Minified leave_me_alone.css (demo)
   $ critic minify -p **/*.css
   Dropped pattern '**/*.css' from css patterns
   $ critic minify +p static/styles/*.css
   Added pattern 'static/styles/*.css'
   $ critic minify -d css
   Minified static/styles/app.css (demo)

And viola (lol), problem solved.

Usage
-----

Considering that your Core Web Vitals will tank if you don't minize and compress your static files,
I am here to offer a solution for one of those things, and it's not even that good lmao.

.. danger::

   I'd suggest running the ``--demo`` option before running :ref:`minify <critic_minify>` without it. 
   With this command you can see *which* files would be affected
   
   :ref:`minify <critic_minify>` is not technically destructive, but it would require a prettifier to undo the minification. 
   Thing is, I haven't tested any prettifiers on the minified output, so it may be actually destructive in that case

.. termynal::

   $ critic minify css
   -->
   Parsed and minified static/styles/app.css



.. _pip: https://pip.pypa.io/en/stable/getting-started/
.. _python standard library: https://docs.python.org/3/library/index.html