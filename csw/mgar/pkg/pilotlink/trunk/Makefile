# $Id$

NAME = pilot-link
VERSION = 0.12.5
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Free package to manage palmos based PDAs with Unix
define BLURB
  pilot-link is a suite of tools used to connect your Palm or PalmOS
  compatible handheld with Unix, Linux, and any other POSIX-compatible
  machine. pilot-link works with all PalmOS handhelds, including those
  made by Handspring, Sony, and Palm, as well as others.

  pilot-link includes userspace "conduits" that allow you to syncronize
  information to and from your Palm device, as well as libraries of
  Palm-compatible functions that allow other applications to take advantage
  of the code included in pilot-link.

  There are also several language "bindings" that allow you to use your
  favorite development language with pilot-link, such as Java, Tcl, Perl,
  and Python.
endef

MASTER_SITES		=	http://downloads.pilot-link.org/
DISTFILES			=	$(DISTNAME).tar.bz2

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

BUILD_DEP_PKGS		+=	CSWperl
BUILD_DEP_PKGS		+=	CSWtcl
BUILD_DEP_PKGS		+=	CSWpython

RUNTIME_DEP_PKGS	=	CSWperl
RUNTIME_DEP_PKGS	+=	CSWtcl
RUNTIME_DEP_PKGS	+=	CSWpython
# This cannot be tracked with checkpkg
# CHECKPKG_OVERRIDES_CSWpilot-link += surplus-dependency|CSWperl
# CHECKPKG_OVERRIDES_CSWpilot-link += surplus-dependency|CSWtcl
# CHECKPKG_OVERRIDES_CSWpilot-link += surplus-dependency|CSWpython

PATCHFILE			=	0001-Fix-shebang-in-configure.patch

GARCOMPILER			=	GNU
CONFIGURE_ARGS		=	$(DIRPATHS)
CONFIGURE_ARGS		+=	--enable-conduits
CONFIGURE_ARGS		+=	--enable-libusb
CONFIGURE_ARGS		+=	--with-perl=perlexec=$(bindir)/perl
CONFIGURE_ARGS		+=	--with-java
CONFIGURE_ARGS		+=	--with-tcl=$(libdir)
CONFIGURE_ARGS		+=	--with-tclinclude
CONFIGURE_ARGS		+=	--with-python

#LICENCE_CSWpilot-link		=	COPYING
#LICENCE_CSWpilot-link-lib	=	COPYING.LIB

include gar/category.mk

