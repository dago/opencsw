NAME = libconfuse
VERSION = 2.7
CATEGORIES = lib

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# For libConfuse 2.7, the test suite doesn't compile cleanly on Solaris,
# so we skip it.  This should be re-assessed with each new release
# from upstream.  Proposed fixes for the test suite to be submitted
# upstream.
ifeq ($(VERSION),2.7)
#TEST_TARGET = check
TEST_SCRIPTS = 
endif

DESCRIPTION = a configuration file parser library
define BLURB
  libConfuse is a configuration file parser library, licensed under
  the terms of the ISC license, and written in C. It supports sections
  and (lists of) values (strings, integers, floats, booleans or other
  sections), as well as some other features (such as single/double-quoted
  strings, environment variable expansion, functions and nested include
  statements). It makes it very easy to add configuration file capability
  to a program using a simple API.
endef

#MASTER_SITES = http://bzero.se/confuse/
MASTER_SITES = http://savannah.nongnu.org/download/confuse/
PATCHFILES = 
DISTFILES  = confuse-$(VERSION).tar.gz
DISTFILES += $(PATCHFILES)
DISTNAME = confuse-$(VERSION)

EXTRA_DOCS = $(PATCHFILES)

PACKAGES += CSWlibconfuse0-1
SPKG_DESC_CSWlibconfuse0-1 = a configuration file parser library

PACKAGES += CSWlibconfuse0-dev
SPKG_DESC_CSWlibconfuse0-dev = Development files for libconfuse
RUNTIME_DEP_PKGS_CSWlibconfuse0-dev = CSWlibconfuse0-1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-nls

include gar/category.mk
