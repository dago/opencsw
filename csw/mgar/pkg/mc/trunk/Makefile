# $Id$
NAME = mc
VERSION = 4.8.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A curses-based visual shell and file manager
define BLURB
endef

# The function "isblank" is not there on Solaris 9, so we can either use
# gnulib and build on Solaris 9, or build on Solaris 10.
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

MASTER_SITES = http://www.midnight-commander.org/downloads/
DISTFILES  = $(DISTNAME).tar.bz2

PATCHFILES = 0001-Ticket-2643-4.8.0-can-t-compile-on-OpenIndiana-Solar.patch

EXTRA_LDFLAGS= -lsocket

RUNTIME_DEP_PKGS_CSWmc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWmc += CSWslang
RUNTIME_DEP_PKGS_CSWmc += CSWglib2

CHECKPKG_OVERRIDES_CSWmc += file-with-bad-content|/usr/local|root/etc/opt/csw/mc/mc.menu
CHECKPKG_OVERRIDES_CSWmc += file-with-bad-content|/usr/local|root/etc/opt/csw/mc/mc.menu.sr
CHECKPKG_OVERRIDES_CSWmc += file-with-bad-content|/usr/local|root/opt/csw/libexec/mc/extfs.d/README
CHECKPKG_OVERRIDES_CSWmc += missing-dependency|CSWperl

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
