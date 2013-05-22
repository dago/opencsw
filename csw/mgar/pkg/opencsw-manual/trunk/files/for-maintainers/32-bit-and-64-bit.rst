--------------------------
32-bit and 64-bit packages
--------------------------

64-bit binaries aren't always best
----------------------------------

It's counter-intuitive, but 64-bit binaries are more memory-hungry and
often slower than 32-bit ones. It makes sense to build 64-bit binaries
when:

* There's a measurable speed boost.
* The application needs to access more than 2G of RAM.
* The application needs to open more than 256 file descriptors.
* The application must match the kernel because it accesses its internal
  structures. One example is the ``lsof`` utility.

There's also the 2G file size restriction, but it can be worked around
by adding the ``-D_LARGEFILE64_SOURCE=1`` flag to the C preprocessor
as documented in `lf64(5)`.

32-bit or 64-bit ‒ Executables
------------------------------

When building packages, the general guideline with regard to bitness is
that executables should default to 32-bit, unless there are reasons to
default them to 64-bit. So the default would be::

  /opt/csw/bin/foo (32-bit binary)
  /opt/csw/bin/sparcv9/foo (64-bit binary)

If ``/opt/csw/bin`` is in PATH, the 32-bit binary will be run by
default, but if the user wants, they can run the 64-bit binary as well.

To run the 64-bit binary where/when possible, you can use isaexec::

  /opt/csw/bin/foo → isaexec (hardlink)
  /opt/csw/bin/sparcv8/foo (32-bit binary)
  /opt/csw/bin/sparcv9/foo (64-bit binary)

The ``isaexec`` program is a wrapper which detects the architecture and
looks for the most advanced binary the current architecture can run. On
sparc, it almost always means running a 64-bit binary. So if you use
``isaexec``, it means defaulting to 64-bit in most cases.

32-bit or 64-bit ‒ Shared libraries
-----------------------------------

The policy regarding shared libraries is different: if possible, do
include 64-bit shared libraries in your package. Even though they might
not be used by default, certain projects might significantly benefit
from them at some point. One example would be ImageMagick, which
performs better in 64-bit mode, and requires numerous shared libraries
to run.

.. _64-bit header files:

Development packages (header files)
-----------------------------------

Development packages in most cases don't distinguish between 32-bit and
64-bit ‒ you don't have to do anything.

However, there are some software projects (e.g. ``gmp``) which install
different headers depending on bitness. These have to be handled
specifically, but providing both 32-bit and 64-bit header files with
a specific switch file. For example::

  /opt/csw/include/foo.h (the switch file)
  /opt/csw/include/foo-32.h
  /opt/csw/include/foo-64.h

The contents of ``foo.h`` would be::

  /* Allow 32 and 64 bit headers to coexist */
  #if defined __amd64 || defined __x86_64 || defined __sparcv9
  #include "foo-64.h"
  #else
  #include "foo-32.h"
  #endif

To implement the following in GAR, you need to set ``EXTRA_PAX_ARGS`` to
rewrite specific header names to be bit-specific, and then manually
install the switch file::

  EXTRA_PAX_ARGS_32  = -s ",^\.$(includedir)/foo.h$$,.$(includedir)/foo-32.h,p"
  EXTRA_PAX_ARGS_64  = -s ",^\.$(includedir)/foo.h$$,.$(includedir)/foo-64.h,p"
  EXTRA_PAX_ARGS = $(EXTRA_PAX_ARGS_$(MEMORYMODEL))

  (...)

  include gar/category.mk

  post-merge:
    ginstall $(FILEDIR)/foo.h $(PKGROOT)$(includedir)/foo.h
    @$(MAKECOOKIE)

This operation must happen in the post-merge stage, because this
operation must be done after we've built binaries for all architectures
and we're merging them into a single directory tree. See the
`modulations in GAR video`_ for more information.

Other files which happen to be 32-bit or 64-bit specific
--------------------------------------------------------

Usually only binaries and libraries differ; all other files have the
same content regardless to the architecture.  However, some software
projects might embed architecture specific information into files which
aren't binaries and don't have a mechanism of choosing the right version
of the file at runtime::

  /opt/csw/bin/foo → isaexec (hardlink)
  /opt/csw/sparcv8/foo (32-bit binary, has /opt/csw/lib in RUNPATH)
  /opt/csw/sparcv9/foo (64-bit binary, has /opt/csw/lib/64 in RUNPATH)
  /opt/csw/lib/64 → sparcv9 (symlink)
  /opt/csw/lib/libfoo.so.1 (32-bit library)
  /opt/csw/lib/sparcv9/libfoo.so.1 (64-bit library)
  /opt/csw/lib/foo/arch_specific_data (ZONK! no mechanism to differentiate!)

The `64-bit header files`_ example shown above is a lucky case, because
header files follow the C syntax, so you can use the ``#if defined``
conditional statement. In the general case there is no single solution,
it all depends on whether you can write a conditional statement such
that you get the 32-bit or 64-bit content depending on a choice made at
runtime.


Compiling 64-bit binaries
-------------------------

To compile a 64-bit binary, you add ``-m64`` to the compiler invocation.
See more about :ref:`linking against OpenCSW libraries`.

In GAR, there's a shortcut::

  BUILD64 = 1


**See also**

* `Solaris 64-bit Developer's Guide`_
* `Are 64-bit Binaries Really Slower than 32-bit Binaries?`_

.. _Solaris 64-bit Developer's Guide:
   http://docs.sun.com/app/docs/doc/816-5138

.. _Are 64-bit Binaries Really Slower than 32-bit Binaries?:
   http://www.osnews.com/story/5768

.. _modulations in GAR video:
   http://youtu.be/7I3efByIg84
