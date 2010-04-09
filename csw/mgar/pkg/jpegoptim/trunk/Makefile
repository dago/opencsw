GARNAME = jpegoptim
GARVERSION = 1.2.3
CATEGORIES = utils

DESCRIPTION = Utility to optimize jpeg files
define BLURB
  Utility to optimize jpeg files
endef

MASTER_SITES = http://www.kokkonen.net/tjko/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

RUNTIME_DEP_PKGS = CSWjpeg

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

TEST_TARGET =
INSTALL_SCRIPTS = custom

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

SPKG_SOURCEURL = http://www.kokkonen.net/tjko/projects.html

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@( cd $(WORKSRC) ; \
	   cp -r $(GARNAME) $(DESTDIR)$(bindir)/$(GARNAME) ; \
	   cp -r README $(DESTDIR)$(docdir)/$(GARNAME) ; \
	   cp -r $(GARNAME).1 $(DESTDIR)$(mandir)/man1/$(GARNAME).1 )
	@$(MAKECOOKIE)
