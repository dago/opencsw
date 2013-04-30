---------------
Buildfarm setup
---------------

.. highlight:: text

Introduction
------------

Packages released by OpenCSW must be built on the OpenCSW buildfarm, but if
you want to experiment, or build in-house packages, you might want to set up
your own build farm, or at least a build host.

Core setup
----------

The following setup is sufficient to create packages using the OpenCSW build
system. You can set up a small virtual machine on a home server, or build
a set of custom packages in your company.

* `basic OpenCSW installation`_, as you would do on any Solaris host where
  you're using OpenCSW packages.
* `GAR setup`_, including subversion checkout of build recipes. This is the
  core part of the package building system,

A `packaging video tutorial`_ is available. It covers all the steps from
a fresh Solaris 10 install to a built package. It takes about 2-3h to complete
it (but YMMV).

Advanced setup
--------------

The following components are not required, but are quite useful.

* `local catalog mirror`_ will allow you to quickly access all packages that
  are in any of OpenCSW catalogs for any Solaris version.
* `checkpkg database`_ will allow you to check packages for common problems,
  for example library dependencies.
* pkgdb-web (with Apache) is a web app on which you can browse your package
  database and inspect package metadata without having to unpack and examine
  packages in the terminal. Information such as list of files, pkginfo content
  and /usr/ccs/bin/dump output are available on that page.
* system garrc is useful when you have multiple users, for example colleagues
  at work who also want to build packages.
* `Additional setup documented on the wiki`_

  * Java setup
  * Solaris Studio setup if you want to build software with that compiler.
    Many of existing build recipes at OpenCSW use this compiler, not GCC.
  * ssh agent setup for paswordless logins

* catalog signing daemon is useful if you wish to build package catalogs
  locally and sign them with a GPG key.

  * `Catalog signing daemon source code`_

.. _GAR setup:
  http://sourceforge.net/apps/trac/gar/wiki/GarSetup

.. _checkpkg database:
  http://wiki.opencsw.org/checkpkg#toc2

.. _Additional setup documented on the wiki:
  http://wiki.opencsw.org/buildfarm

.. _local catalog mirror:
  ../for-administrators/mirror-setup.html

.. _basic OpenCSW installation:
  ../for-administrators/getting-started.html

.. _packaging video tutorial:
  http://youtu.be/JWKCbPJSaxw

.. _Catalog signing daemon source code:
  http://sourceforge.net/p/opencsw/code/HEAD/tree/catalog_signatures/
