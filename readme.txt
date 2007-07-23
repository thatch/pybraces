========
pybraces
========

This is a quick hack as an encoding to support using braces instead of
significant whitespace in Python.  It transforms all '{' at EOL to a colon and
more indentation on the next line.  '}' dedents likewise.  Semicolons are not
something this script deals with -- they're supported in Python but the way I
use them (delimiting end of line) is a little silly.

Installation
============

You'll need to copy or symlink braces.py into your Python lib/encodings
directory, and ensure that your user has rights to create the .pyc or .pyo
file there.

Example Files
=============

demo0.py
--------

This shows off the core functionality -- being able to convert braces to
indentation (or at least ignore them, since this already has decent
indentation).  The important part is the 'encoding: braces' on line two.

doc.py
------

This shows that multiline strings can also benefit::

    >>> import doc
    >>> print doc.__doc__


