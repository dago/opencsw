--------------
Package naming
--------------

.. highlight:: text

We are paying attention to package naming, so we can maintain consistency across
the catalog. For example, we have special rules about how to name packages with
shared libraries, or development packages. In general, we often find ourselves
following Debian, so if you're in doubt, consulting the Debian package
repository is a good idea.

pkgname vs catalogname
----------------------

pkgname is also known as pkginst. It's a name of a package in the Solaris
packaging system. These package names start with the company ticker (e.g.
SUNW). OpenCSW package start with “CSW”.

Catalognames on the other hand, are names used in the catalog index. This means
that one package has two names, for example “CSWfoo” (pkgname) and “foo”
(catalogname).

Applications and named projects
-------------------------------

Use the project name, keep it short and simple. If the name consists of many
words, separate words. Use dashes to separate words in the pkgname (CSWfoo-bar)
and underscores in the catalogname (foo_bar).

Shared libraries
----------------

Shared libraries follow a special naming convention. In short, if you're
packaging libfoo.so.1, there should be a package containing just that library,
and the package should be named CSWlibfoo1. See the shared libraries article for
more information.

Development packages
--------------------

Software name plus the “-dev” suffix. For example: CSWfoo-dev and foo_dev.

Perl, Python, Ruby
------------------

Prepend packages with pm\_, py\_ and rb\_, respectively.
