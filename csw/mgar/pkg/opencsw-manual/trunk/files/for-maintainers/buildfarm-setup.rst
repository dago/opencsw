---------------
Buildfarm setup
---------------

.. highlight:: text

Introduction
------------

Packages released by OpenCSW must be built on the OpenCSW buildfarm, but if
you want to experiment, or build in-house packages, you might want to set up
your own build farm, or at least a build host.

Buildfarm setup consists of:

* OpenCSW installation
* `GAR setup`_ and subversion checkout
* `Local catalog mirror`_
* `checkpkg database`_
* pkgdb-web (with Apache)
* system garrc
* `wiki instructions`_ (Java setup, Solaris Studio setup, ssh agent setup)
* signing daemon

.. _GAR setup:
  http://sourceforge.net/apps/trac/gar/wiki/GarSetup

.. _checkpkg database:
  http://wiki.opencsw.org/checkpkg#toc2

.. _wiki instructions:
  http://wiki.opencsw.org/buildfarm

.. _Local catalog mirror:
  ../for-administrators/mirror-setup.html
