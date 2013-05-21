--------------
Catalog format
--------------

Catalog format in short::

  common version package file md5 size dependencies category i-dependencies

For example::

  bind 9.4.2,REV=2008.07.09_rev=p1 CSWbind bind-9.4.2,REV=2008.07.09_rev=p1-SunOS5.8-sparc-CSW.pkg.gz f68df57fcf54bfd37304b79d6f7eeacc 2954112 CSWcommon|CSWosslrt net none

Each field is space separated, the dependencies field can be split with
the pipe char, like in the example above with two dependencies. The same
goes for the category and incompatible dependencies fields.

A package can only occur once in the catalog, meaning that both package
names and catalog names must be unique in a catalog.

The catalog may have to be extended to support more features like if
there's a source package available. In that case extra fields should be
added to the end so not to break existing tools.

See also:

* `Building a catalog`_

.. _Building a catalog:
  building-a-catalog.html
