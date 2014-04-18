----------------------
OpenCSW for Developers
----------------------

This is a manual for developers who want to build own software, using
tools and libraries provided by OpenCSW.

.. _linking against OpenCSW libraries:

Linking against OpenCSW libraries
=================================

To build own software against libraries distributed by OpenCSW, install the
relevant ``*_dev`` packages. They contain the header files, and ``*.so``
symlinks necessary during linking.

When building againt OpenCSW software, aside from setting the ``PATH``
correctly, these flags will typically make it work::

  CPPFLAGS="-I/opt/csw/include"
  LDFLAGS="-L/opt/csw/lib -R/opt/csw/lib"
  PKG_CONFIG_PATH="/opt/csw/lib/pkgconfig"

If you're building a 64-bit binary, use these::

  CPPFLAGS="-I/opt/csw/include"
  LDFLAGS="-L/opt/csw/lib/64 -R/opt/csw/lib/64"
  PKG_CONFIG_PATH="/opt/csw/lib/64/pkgconfig"

64-bit libraries live in these directories, depending on the architecture::

  /opt/csw/lib/sparcv9
  /opt/csw/lib/amd64

The ``/opt/csw/lib/64`` path is a symlink to a chosen architecture
subdirectory. For example, on SPARC ``/opt/csw/lib/64`` is a symlink to
``/opt/csw/lib/sparcv9``.

All binaries compiled with the ``-R/opt/csw/lib/64`` flag will try to look at
that path and find their corresponding sparcv9 or amd64 libraries. This way you
can use the same ``-R`` flag for both sparc and intel 64-bit builds.

