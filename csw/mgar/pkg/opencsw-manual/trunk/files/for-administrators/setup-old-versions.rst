.. _old-solaris:

Solaris 8 or 9
==============

.. NOTE::
   OpenCSW no longer offers catalogs for Solaris 8.

.. NOTE::
   Solaris 9 is on its way to deprecation. Solaris 9 catalogs get very few
   package updates.

``pkgadd`` on Solaris 8 and 9 does not support installation directly via http. In such case
you need to download pkgutil with a separate tool like wget, and install it
from disk::

  wget http://mirror.opencsw.org/opencsw/pkgutil.pkg
  pkgadd -d pkgutil.pkg all

Continue to :ref:`Full setup <installation-full-setup>`.
