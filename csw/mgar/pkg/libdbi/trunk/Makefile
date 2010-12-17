# $Id$
NAME = libdbi
VERSION = 0.8.4
CATEGORIES = lib

DESCRIPTION = A database-independent abstraction layer
define BLURB
  libdbi implements a database-independent abstraction layer in C, similar to the DBI/DBD layer in Perl.
  Writing one generic set of code, programmers can leverage the power of multiple databases and multiple
  simultaneous database connections by using this framework.
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibdbi1 CSWlibdbi-devel

CATALOGNAME_CSWlibdbi1 = libdbi1
CATALOGNAME_CSWlibdbi-devel = libdbi_devel

SPKG_DESC_CSWlibdbi1 = $(DESCRIPTION) containing libdbi.so.1
SPKG_DESC_CSWlibdbi-devel = Development files for libdbi

RUNTIME_DEP_PKGS_CSWlibdbi-devel = CSWlibdbi1

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --docdir=$(docdir)/libdbi

# Hardcoded CFLAGS are 'xO4 -fast -w -fsimple -native -xcg92'
# We must override them to at least add 32/64 functionality.
# We must not use -fast and -native as it provides v8+ binaries while we are stuck at pure v8.
# -xcg92 is obsoleted.
EXTRA_CFLAGS = -w -fsimple
BUILD_OVERRIDE_VARS = CFLAGS
BUILD_OVERRIDE_VAR_CFLAGS = $(CFLAGS)

TEST_TARGET = check

INSTALL_OVERRIDE_VARS = docdir
INSTALL_OVERRIDE_VAR_docdir = $(docdir)/libdbi-devel

PKGFILES_CSWlibdbi1 = $(PKGFILES_RT)

include gar/category.mk
