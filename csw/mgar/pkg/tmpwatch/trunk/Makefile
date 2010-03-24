GARNAME = tmpwatch
GARVERSION = 2.10.1
CATEGORIES = apps

DESCRIPTION = Removes files which haven't been accessed for a period of time
define BLURB
  The tmpwatch utility recursively searches through specified directories
  and removes files which have not been accessed in a specified period of
  time. tmpwatch is normally used to clean up directories which are used
  for temporarily holding files (for example, /tmp). 
endef

VENDOR_URL   = https://fedorahosted.org/tmpwatch/
MASTER_SITES = https://fedorahosted.org/releases/t/m/tmpwatch/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.bz2
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk

