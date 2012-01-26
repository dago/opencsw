# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! build state unknown, work in progress, please verify
#
NAME = stressapptest
VERSION = 1.0.3
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Stress test application for simulating high load situations
define BLURB
  Stressful Application Test (or stressapptest, its unix name) tries to
  maximize randomized traffic to memory from processor and I/O, with the
  intent of creating a realistic high load situation in order to test the
  existing hardware devices in a computer. 
endef

VENDOR_URL    = http://code.google.com/p/stressapptest/
MASTER_SITES  = http://stressapptest.googlecode.com/files/
DISTFILES  	  = $(NAME)-$(VERSION)_autoconf.tar.gz
DISTNAME 	  = $(NAME)-$(VERSION)_autoconf
UFILES_REGEX  = $(NAME)-(\d+(?:\.\d+)*)_autoconf.tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
