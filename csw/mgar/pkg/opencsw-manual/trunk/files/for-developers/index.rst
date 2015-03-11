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

Typical file layout of libraries::

  CSWfoo_dev: /opt/csw/include/foo.h
              /opt/csw/lib/libfoo.so -> libfoo.so.1
  CSWlibfoo1: /opt/csw/lib/libfoo.so.1 -> libfoo.so.1.0.0
              /opt/csw/lib/libfoo.so.1.0.0 (regular file)

Autotools and GCC
-----------------

Set ``PATH`` to include the path to the compiler you wish to use. If you're
using GCC from OpenCSW, you set it to ``/opt/csw/bin``.

Autotools-based projects by default accept a standard set of environment
variables. Here are values for a 32-bit build::

  CFLAGS="-m32"  # if you're using GCC
  CPPFLAGS="-I/opt/csw/include"
  LDFLAGS="-L/opt/csw/lib -R/opt/csw/lib"
  PKG_CONFIG_PATH="/opt/csw/lib/pkgconfig"

If you're building a 64-bit binary, use these::

  CFLAGS="-m64"  # if you're using GCC
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

We recommend the `Autotools Mythbuster`_ as a reference to Autotools.

A non-autotools project
-----------------------

If you're building a project which does not use autotools, you need to
tell the compiler to do the following:

1. Look into ``/opt/csw/include`` for the ``.h`` files. In GCC, it's achieved
   with ``-I/opt/csw/include``. Without it, compilation will fail.
2. Look into ``/opt/csw/lib`` for the ``.so`` files. In GCC, it's achieved
   with ``-L/opt/csw/lib``. Without it, linking will fail.
3. Put ``/opt/csw/lib`` into the ``RPATH`` field in the ELF header. In GCC,
   this is achieved with ``-R/otp/csw/lib/``. Without it, binaries will build,
   but won't run.

For 64-bit builds, use ``/opt/csw/lib/64``.

If your compiler is not GCC, you might need to pass different flags.

How to add flags to the compiler invocations, depends on the build system of
the software you're building.

.. _Autotools Mythbuster: https://autotools.io/
