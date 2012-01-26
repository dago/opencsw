# $Id$
NAME = ffcall
VERSION = 1.10
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Foreign function call libraries
define BLURB
  This is a collection of four libraries which can be used to build foreign function call interfaces in embedded interpreters.
endef

MASTER_SITES = http://www.haible.de/bruno/gnu/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.haible.de/bruno/packages-ffcall.html

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

pre-install-modulated:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)
