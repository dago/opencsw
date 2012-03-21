NAME = libconfuse
VERSION = 2.7
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A configuration file parser library
define BLURB
  libConfuse is a configuration file parser library, licensed under
  the terms of the ISC license, and written in C. It supports sections
  and (lists of) values (strings, integers, floats, booleans or other
  sections), as well as some other features (such as single/double-quoted
  strings, environment variable expansion, functions and nested include
  statements). It makes it very easy to add configuration file capability
  to a program using a simple API.
endef

MASTER_SITES = http://savannah.nongnu.org/download/confuse/
DISTNAME = confuse-$(VERSION)
DISTFILES += $(DISTNAME).tar.gz

#PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

LICENSE = AUTHORS

PACKAGES += CSWlibconfuse0
SPKG_DESC_CSWlibconfuse0 = A configuration file parser library, libconfuse.so.0
PKGFILES_CSWlibconfuse0 += $(call pkgfiles_lib,libconfuse.so.0)
OBSOLETED_BY_CSWlibconfuse0 += CSWlibconfuse

PACKAGES += CSWlibconfuse-dev
SPKG_DESC_CSWlibconfuse-dev = Development files for libconfuse.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibconfuse-dev += CSWlibconfuse0

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-nls

# For libConfuse 2.7, the test suite doesn't compile cleanly on Solaris,
# so we skip it.  This should be re-assessed with each new release
# from upstream.  Proposed fixes for the test suite to be submitted
# upstream.
SKIPTEST-2.7 = 1
SKIPTEST = $(SKIPTEST-$(VERSION))

include gar/category.mk
