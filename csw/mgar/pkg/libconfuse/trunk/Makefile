GARNAME = libconfuse
GARVERSION = 2.6
CATEGORIES = lib

# For libConfuse 2.6, the test suite doesn't compile cleanly on Solaris,
# so we skip it.  This should be re-assessed with each new release
# from upstream.  Proposed fixes for the test suite to be submitted
# upstream.
ifeq ($(GARVERSION),2.6)
#TEST_TARGET = check
TEST_SCRIPTS = skip
test-skip:
	$(DONADA)
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

MASTER_SITES = http://bzero.se/confuse/
DISTFILES  = confuse-$(GARVERSION).tar.gz
DISTNAME = confuse-$(GARVERSION)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-nls

include gar/category.mk
