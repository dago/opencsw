----------------------
OpenCSW for Developers
----------------------

This is a manual for developers who want to build own software, using
tools and libraries provided by OpenCSW.

Linking against OpenCSW libraries
=================================

To build own software against libraries distributed by OpenCSW, install the
relevant ``*_dev`` packages. They contain the header files, and ``*.so``
symlinks necessary during linking.

When building againt OpenCSW software, these flags will typically make it
work::

  CPPFLAGS="-I/opt/csw/include"
  LDFLAGS="-L/opt/csw/lib -R/opt/csw/lib"
  PKG_CONFIG_PATH="/opt/csw/lib/pkgconfig"

If you're building a 64-bit binary, use these::

  CPPFLAGS="-I/opt/csw/include"
  LDFLAGS="-L/opt/csw/lib/64 -R/opt/csw/lib/64"
  PKG_CONFIG_PATH="/opt/csw/lib/64/pkgconfig"

.. _LD_LIBRARY_PATH - just say no:
   https://blogs.oracle.com/rie/entry/tt_ld_library_path_tt

