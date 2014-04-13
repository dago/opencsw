--------------
Catalog format
--------------

Space separated fields::

  common version package file md5 size dependencies category i-dependencies

For example::

  bind 9.4.2,REV=2008.07.09_rev=p1 CSWbind bind-9.4.2,REV=2008.07.09_rev=p1-SunOS5.8-sparc-CSW.pkg.gz f68df57fcf54bfd37304b79d6f7eeacc 2954112 CSWcommon|CSWosslrt net none

The format of the ``dependencies`` and ``i-dependencies`` fields::

1. When the list is empty: ``none``
2. When the list is non-empty, pipe-separated list of pkginst names:
   ``CSWfoo|CSWbar``

A package can only occur once in the catalog, meaning that both package names
(pkginst) and catalog names must be unique in a catalog.

The catalog may have to be extended to support more features like if
there's a source package available. In that case extra fields should be
added to the end so not to break existing tools.

Signatures
==========

A catalog file can be signed with gpg, cleartext style, with the signature
embedded in the file.

CREATIONDATE
============

The first line can contain::

  # CREATIONDATE 2014-03-16T08:39:58Z

See also:

* `Building a catalog`_

.. _Building a catalog:
  building-a-catalog.html
