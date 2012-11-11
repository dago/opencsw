NAME = bvi
VERSION = 1.3.2
GARTYPE = v2

DESCRIPTION = A vi-like binary file (hex) editor
define BLURB
  The bvi is a display-oriented editor for binary files, based on the vi
  texteditor. If you are familiar with vi, just start the editor and begin
  to edit! A bmore program is also included in the package. If you never
  heard about vi, maybe bvi is not the best choice for you. 
endef

VENDOR_URL   = http://bvi.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
DISTFILES    = $(NAME)-$(VERSION).src.tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).src.tar.gz
UPSTREAM_MASTER_SITES = http://sourceforge.net/projects/bvi/files/

TEST_SCRIPTS =

# bvi uses --libdir to store a help file
CONFIGURE_ARGS = $(filter-out --libdir%, $(DIRPATHS))
CONFIGURE_ARGS += --libdir=$(datadir)/$(NAME)

NORUNPATH = 1

include gar/category.mk

post-install-modulated: DOCS=CHANGES CREDITS
post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	cp $(addprefix $(WORKSRC)/, $(DOCS)) $(DOCDEST)
	@$(MAKECOOKIE)
