GARNAME = cvsproxy
GARVERSION = 1.0.1
CATEGORIES = utils

DESCRIPTION = Provides a CVS proxy
define BLURB
  Provides a CVS proxy
endef

MASTER_SITES = http://www.sra.co.jp/people/m-kasahr/cvsproxy/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

post-install-modulated:
	@echo "==> Post-install fixes"
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@cp $(WORKSRC)/README $(DESTDIR)$(docdir)/$(GARNAME)
	@cp $(WORKSRC)/NEWS $(DESTDIR)$(docdir)/$(GARNAME)
	@cp $(WORKSRC)/ChangeLog $(DESTDIR)$(docdir)/$(GARNAME)
	@$(MAKECOOKIE)
