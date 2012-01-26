# $Id$
NAME = libdbi
VERSION = 0.8.4
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A database-independent abstraction layer
define BLURB
  libdbi implements a database-independent abstraction layer in C, similar to the DBI/DBD layer in Perl.
  Writing one generic set of code, programmers can leverage the power of multiple databases and multiple
  simultaneous database connections by using this framework.
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://libdbi.sourceforge.net/

PACKAGES += CSWlibdbi1
SPKG_DESC_CSWlibdbi1 = A database-independent abstraction layer, libdbi.so.1
PKGFILES_CSWlibdbi1 = $(call pkgfiles_lib,libdbi.so.1)

PACKAGES += CSWlibdbi-dev
SPKG_DESC_CSWlibdbi-dev = Development files for libdbi.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibdbi-dev = CSWlibdbi1
OBSOLETED_BY_CSWlibdbi-dev = CSWlibdbi-devel

REINPLACE_USRLOCAL += doc/programmers-guide/x276.html
REINPLACE_USRLOCAL += doc/programmers-guide/quickstart-code.html

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --docdir=$(docdir)/libdbi

# Hardcoded CFLAGS are 'xO4 -fast -w -fsimple -native -xcg92'
# We must override them to at least add 32/64 functionality.
# We must not use -fast and -native as it provides v8+ binaries while we are stuck at pure v8.
# -xcg92 is obsoleted.
EXTRA_CFLAGS = -w -fsimple
BUILD_OVERRIDE_VARS = CFLAGS
BUILD_OVERRIDE_VAR_CFLAGS = $(CFLAGS)

INSTALL_OVERRIDE_VARS = docdir
INSTALL_OVERRIDE_VAR_docdir = $(docdir)/libdbi_dev

include gar/category.mk
