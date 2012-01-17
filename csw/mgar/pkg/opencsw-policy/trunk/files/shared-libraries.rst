Shared libraries
================

Background
----------

Some packages are providing shared libraries.  When binaries start
linking to them, the updates to packages with shared libraries must be
done in a way that doesn't break existing binaries.

Life cycle of a shared library can be summarized in the following way:

1. A SONAME appears
2. We decide to distribute it
3. Binaries start linking to it
4. Time passes, new version of the same library comes along
5. Binaries stop linking to it
6. SONAME goes away

Historically, shared libraries were packaged either together with base
packages, or split off to their own packages.  However, once updated
shared libraries became available upstream, updated packages included
both old and new versions of shared libraries.  This required package
builds to download and compile multiple versions of the same project.
Notable examples are curl and neon libraries, where CSWcurlrt contained
all three libcurl.so.2, libcurl.so.3 and libcurl.so.4.

Phasing out of shared libraries was difficult.  To phase out a shared
library, it is required to verify that no binaries link to it.  All
dependent packages need to be recompiled against the newest version of
the library, and once this is done, old versions can be removed.
However, even when all dependent packages are already recompiled against
libcurl.so.4, there are no useful indicators that libcurl.so.2 is no
longer linked to.  To verify this, all dependent packages have to be
unpacked, and examined using /usr/ccs/bin/dump that the no longer list
libcurl.so.2 in their NEEDED field.

Once the detection problem is solved, removing the old version of
a library is not as simple as it could be; The whole CSWcurlrt has to be
rebuilt and re-released in a new version which no longer includes
libcurl.so.2.

Goals
-----

* Simplification of handling of shared library life cycles
* Allowing to determine whether a specific shared library is no longer
  linked to, by looking at package dependencies (This avoids potential
  problem of our keeping "legacy binary libs" in a more modern package
  for longer than is neccessary. It also avoids having to keep coping
  the binary into future packages)

Non-goals
---------

* Providing a reliable mechanism to determine whether a given pkgname
  contains a shared library
* Keeping package names short and pretty as a priority

Overview
--------

As a general rule, each soname shall be packaged in a separate package.
This way, it's easy to track dependencies on specific sonames, detect
and phase out sonames that are no longer in use.  It also avoids the
need to rebuild all the versions of software in question if one of the
versions needs an update.

This idea is based on the Debian shared libraries packaging policy
[#debian-policy]_ and has been discussed [#discussion]_ on the mailing
list.

Advantages:

* easy and complete lifecycle of shared libraries

* phasing out of shared libraries can become part of standard catalog
  update procedures
* simpler packages, simpler builds (no need for version modulations and
  complex merges, good for new maintainers)
* isolation of old non-fixable files with issues (if there's an old
  library mentioning /export/medusa, you don't have to worry about it
  being stopped during release after you push it once)
* no re-pushing of old files
* more packages overall (good for stats!)
* number of packages released per software upgrade remains the same.  If
  there were, say, 4 packages to release with each Python update, the
  number remains: 4 per release.  There will be one new CSWlibpython*
  package, and the old CSWlibpython library won't be upgraded.


Disadvantages:

* maintainers need to make more decisions when packaging
* there's some amount of work to be done to do the transition, such as
  creation of new packages and dependencies
* some package names become long and complex (however, they are only
  dependencies; users don't need to type these in)

Implementation details
----------------------

Package naming
~~~~~~~~~~~~~~

Names of packages shall be derived from sonames, and from sonames only.
They shall not depend on project name, or project version.  If a project
is named foo, and contains libbar.so.0, the package name shall be based
on libbar, not foo.

A table listing examples of sonames and corresponding package
names. [#soname-pkgname-unit-test]_

========================= ======================= =========================
soname                    pkgname                 catalogname
========================= ======================= =========================
libfoo.so.0               CSWlibfoo0              libfoo0
libfoo-0.so               CSWlibfoo0              libfoo0
libfoo.so.0.1             CSWlibfoo0-1            libfoo0_1
libapr-1.so.0             CSWlibapr1-0            libapr1_0
libbabl-0.1.so.0          CSWlibbabl0-1-0         libbabl0_1_0
libgettextlib-0.14.1.so   CSWlibgettextlib0-14-1  libgettextlib0_14_1
libapr-1.so.10            CSWlibapr-1-10          libapr_1_10
libstdc++.so.6            CSWlibstdc++6           libstdc++6
libdnet.1                 CSWlibdnet1             libdnet1
libUpperCase.so.1         CSWlibuppercase1        libuppercase1
libpyglib-2.0-python.so.0 CSWlibpyglib2-0python0  libpyglib2_0python0
libpython3.1.so.1.0       CSWlibpython3-1-1-0     libpython3_1_1_0
libapr-1.so.10.0.0        CSWlibapr1-10-0-0       libapr1_10_0_0
========================= ======================= =========================

Separators
^^^^^^^^^^

Separators are added between two adjacent numbers, and removed if a number and a letter are next to each other.  For example, ``libfoo.so.0`` becomes ``CSWlibfoo0``, and ``libfoo-1.so.0`` becomes ``CSWlibfoo1-0``.

Linkable shared objects
~~~~~~~~~~~~~~~~~~~~~~~

The policy or recommendation shall refer to libraries which are //linkable,// meaning other binaries can link against them.  Shared objects in private directories, such as /opt/csw/lib/someproject/foo.so (think Python modules) are not shared libraries which other projects can link to, and therefore there is no benefit in placing them in separate packages.

Special cases
^^^^^^^^^^^^^

Some packages (e.g. Kerberos libraries) put private shared libraries into /opt/csw/lib.  They don't expose any public API, and only own Kerberos binaries link to them.  Private shared libraries can be bundled with the main package, without splitting them off.

Examples
^^^^^^^^

============================================================================== ============
file                                                                           linkable?
============================================================================== ============
/opt/csw/lib/libfoo.so.0.2                                                     Yes
/opt/csw/lib/sparcv9/libfoo.so.0.2                                             Yes
/opt/csw/lib/sparcv8plus+vis/libfoo.so.0.2                                     Yes
/opt/csw/lib/amd64/libfoo.so.0.2                                               Yes
/opt/csw/libexec/bar                                                           No
/opt/csw/share/bar                                                             No
/opt/csw/lib/gnucash/libgncmod-stylesheets.so.0.0.0                            No
/opt/csw/lib/erlang/lib/megaco-3.6.0.1/priv/lib/megaco_flex_scanner_drv_mt.so  No
/opt/csw/share/Adobe/Reader8/Reader/sparcsolaris/lib/libcrypto.so.0.9.6        No
/opt/csw/customprefix/lib/libfoo.so.0.2                                        Yes
/opt/csw/boost-gcc/lib/libboost_wserialization.so.1.44.0                       Yes
============================================================================== ============

Example implementation and its unit tests can be found in checkpkg
sources [#is-library-linkable-implementation]_ and corresponding unit
tests. [#is-library-linkable-unit-tests]_

Private shared libraries
^^^^^^^^^^^^^^^^^^^^^^^^

Some software projects install private (non-linkable) shared libraries
into libdir (e.g. ``/opt/csw/lib``) by default.  To ensure that they are
private, they need to be moved to a subdirectory, e.g.
``/opt/csw/lib/<project>``.

To create a private library and install 32 and 64-bit libraries, they
need to be laid out as follows:

On sparc::

  /opt/csw/lib/foo
  /opt/csw/lib/foo/32 --> .
  /opt/csw/lib/foo/64 --> sparcv9

On i386::

  /opt/csw/lib/foo
  /opt/csw/lib/foo/32 --> .
  /opt/csw/lib/foo/64 --> amd64

In GAR, it can be simplified by symlinking:

* 32 to ``$(ISA_DEFAULT)``
* 64 to ``$(ISA_DEFAULT64)``

The runpath needs to be set to ``/opt/csw/lib/foo/64``, e.g. ``-R/opt/csw/lib/foo/64``.

Grouping shared libraries
-------------------------

There can be cases in which a set of shared libraries is likely to be
upgraded together. Considering the following set of libraries:

* libfoo.so.0
* libfoo_bar.so.0
* libfoo_baz.so.0

It's possible that all the following libraries will be updated together.
In such a case, all these shared objects can be put in a single package.
The decision shall be made by the maintainer.

If versions of shared libraries don't match, chances are that their API
will not be changing together, and it's a good idea not to package them
together.  For example, the following three libraries are best kept in
separate packages.

* libfoo.so.0
* libfoo_bar.so.1
* libfoo_baz.so.0

When making the decision, the question a maintainer should ask, should
be: "Are all these shared libraries going to be retired together?" If
the answer is positive, shared libraries shall be in a single package.
However, in the face of uncertainty (it's hard to predict the future),
placing each file in a separate package is always a safe choice.

Transitioning of the existing packages
--------------------------------------

Consists of moving the shared library to own package, and making the
original package an empty, transitional one.  The phasing out of
transitional packages follows the same rules as any other packages: when
nothing depends on them, they can be removed.

A simple example:

* Before

  - CSWlibfoo (libfoo.so.1)

* After

  - CSWlibfoo (empty) → CSWlibfoo1 (libfoo.so.1)

For an existing more complex package, with already existing two versions
of a library:

* Before

  - CSWlibfoo (libfoo.so.1, libfoo.so.2)

* After

  - CSWlibfoo (empty) → CSWlibfoo1 (libfoo.so.1)
  - CSWlibfoo (empty) → CSWlibfoo2 (libfoo.so.2)

Potential problems
==================

Potential collisions in package naming would include libfoo.so.1 and
libfoo-1.so both resolving to CSWlibfoo1.  If this case ever occurs, the
naming conflict needs to be resolved manually.  However, to this time,
such a case has been never observed.

Certain sonames are long enough that the corresponding package names are
over 29 characters long.  However, it affects a small percent of
libraries, roughly about 98% SONAMEs generate package names within
limits.

Footnotes
=========

.. [#discussion] `An idea for a shared libraries policy`_ -
   mailing list discussion
.. [#debian-policy]
   `Debian shared libraries packaging policy`_
.. [#is-library-linkable-implementation]
   `IsLibraryLinkable implementation`_
.. [#is-library-linkable-unit-tests]
   `IsLibraryLinkable unit tests`_
.. [#soname-pkgname-unit-test]
   checkpkg unit tests with
   `examples of mappings between SONAMEs, pkgnames and catalognames`_
.. _Debian shared libraries packaging policy:
   http://www.debian.org/doc/debian-policy/
   ch-sharedlibs.html#s-sharedlibs-runtime
.. _An idea for a shared libraries policy:
   http://lists.opencsw.org/pipermail/maintainers/2010-September/
   012752.html
.. _IsLibraryLinkable implementation:
   http://sourceforge.net/apps/trac/gar/browser/csw/mgar/gar/v2/
   lib/python/sharedlib_utils.py#L24
.. _IsLibraryLinkable unit tests:
   http://sourceforge.net/apps/trac/gar/browser/csw/mgar/gar/v2/
   lib/python/sharedlib_utils_test.py#L13
.. _examples of mappings between SONAMEs, pkgnames and catalognames:
   http://sourceforge.net/apps/trac/gar/browser/csw/mgar/gar/v2/
   lib/python/sharedlib_utils_test.py#L68
