GARNAME = xsel
GARVERSION = 1.2.0
CATEGORIES = utils

DESCRIPTION = Command-line tool to access X clipboard and selection buffers
define BLURB
  XSel is a command-line program for getting and setting the contents of
  the X selection. Normally this is only accessible by manually
  highlighting information and pasting it with the middle mouse button. 
endef

MASTER_SITES = http://www.vergenet.net/~conrad/software/xsel/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
NORUNPATH = 1

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	@ginstall -d -m 755 $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
