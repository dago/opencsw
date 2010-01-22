GARNAME = ngspice
GARVERSION = 20
CATEGORIES = apps


DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://downloads.sourceforge.net/project/ngspice/ng-spice-rework/$(GARVERSION)/
DISTFILES  = ng-spice-rework-$(GARVERSION).tar.gz
PATCHFILES = fix-missing-include-in-src-spicelib-parser-inpptree.c.patch

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
