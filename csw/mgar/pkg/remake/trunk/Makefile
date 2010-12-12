NAME = remake
VERSION = 3.81_dbg_0.2
CATEGORIES = devel

DESCRIPTION = GNU Make debugger
define BLURB
  remake is a patched and modernized version of GNU make utility that adds
  improved error reporting, the ability to trace execution in a comprehensible
  way, and a debugger.
endef

MASTER_SITES = http://cloud.github.com/downloads/rocky/remake/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

SPKG_SOURCEURL = http://bashdb.sourceforge.net/remake/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
