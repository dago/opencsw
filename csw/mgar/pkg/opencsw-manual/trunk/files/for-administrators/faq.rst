--------------------------
Frequently Asked Questions
--------------------------

Are services started by default?
================================

By default, services are started upon package installation. You can change that
by `disabling SMF in csw.conf`_.

.. _disabling SMF in csw.conf:
   http://wiki.opencsw.org/cswclassutils-package#toc10

If you disable service startup by default, and you are using OpenSSH from
OpenCSW, and you upgrade the openssh package, the ssh service will not be
started by default, locking you out of the system. Make sure you make an
additional entry telling the SSH service to start automatically.

How can I install CSW packages in a location other than ``/opt/csw``?
=====================================================================

OpenCSW packages are not relocatable, so you can't install them in a location
other than /opt/csw. Even if the packages were relocatable from the package
system point of view, there are usually paths hard-coded within the packaged
applications that point to and rely on /opt/csw (for libraries, configuration
files, data files and such). Relocating such applications is
application-specific.

How can I transfer packages to a computer without an Internet connection?
=========================================================================

Please see :ref:`installing on a host without an Internet connection
<installing-on-a-host-without-an-internet-connection>`.

Why do packages go by two names (e.g. CSWftype2 and freetype2)?
===============================================================

There are two names associated with every piece of software that we ship: a
package name (a.k.a. pkgname, or pkginst) and a catalog name. The package name
is used by the underlying Solaris SVR4 package management tools (pkgadd, pkgrm,
pkginfo), needs to fit historical limits (32 characters), and is sometimes
cryptically condensed. The catalog name has no significance to Solaris itself,
and is used by pkgutil and in package catalogs.

Why not use third party dependencies?
=====================================

Problems with declaring SUNW and SFW packages as dependencies are:

* pkgutil can't download and install them, so declaring them as dependencies
  won't help during installation
* they often contain old versions of software (or libraries), while OpenCSW
  package need newer versions
* OpenCSW packages must be installable on multiple Solaris versions; a package
  built for Solaris 9 will also install on Solaris 10. In many cases, the
  required shared libraries are in packages of different names, e.g. 64-bit
  version of libfoo.so.1 might be in SUNWfoo on Solaris 10 and SUNWfoox on
  Solaris 9.

Where are the Solaris 10 version of a package I'm looking at?
=============================================================

As of April 2014 most packages are built for Solaris 10, but since it's
possible to install a Solaris 9 package on Solaris 10, we take advantage of
that fact and put Solaris 9 packages in Solaris 10 catalogs.

There are cases where a package can benefit from features specific to Solaris
10, and we create separate Solaris 9 and Solaris 10 package builds.

Are the binaries compiled for advanced Instruction Set Architectures?
=====================================================================

Binaries are compiled for basic ISAs. In most cases, performance is not
significantly improved by compiling for advanced ISAs.  For those cases where
it is, we usually provide cpu-optimized libraries.

If you know of a specific binary that would benefit from cpu-specific
optimizations, feel free to contact this package's maintainer and ask about it.
