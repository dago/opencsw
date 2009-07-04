GARNAME = bvi
GARVERSION = 1.3.2
CATEGORIES = utils

DESCRIPTION = A vi-like binary file (hex) editor
define BLURB
  Long description
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).src.tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).src.tar.gz
UPSTREAM_MASTER_SITES = http://sourceforge.net/projects/bvi/files/

TEST_SCRIPTS =

# bvi uses --libdir to store a help file
CONFIGURE_ARGS = $(filter-out --libdir%, $(DIRPATHS))
CONFIGURE_ARGS += --libdir=$(datadir)/$(GARNAME)

NORUNPATH = 1

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
