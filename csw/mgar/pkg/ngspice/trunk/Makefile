NAME = ngspice
VERSION = 20
CATEGORIES = apps
GARTYPE = v2


DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://downloads.sourceforge.net/project/ngspice/ng-spice-rework/$(VERSION)/
DISTFILES  = ng-spice-rework-$(VERSION).tar.gz
PATCHFILES = fix-missing-include-in-src-spicelib-parser-inpptree.c.patch

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
