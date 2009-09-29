GARNAME = jpeginfo
GARVERSION = 1.6.0
CATEGORIES = utils

DESCRIPTION = Info and error checking of jpeg files
define BLURB
  Utility to generate informative listings from jpeg files, and to check jpeg files
  for errors. Program also supports automagic deletion of broken jpegs.
endef

MASTER_SITES = http://www.kokkonen.net/tjko/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

REQUIRED_PKGS = CSWjpeg

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =
INSTALL_SCRIPTS = custom

include gar/category.mk

SPKG_SOURCEURL = http://www.kokkonen.net/tjko/projects.html#jpeginfo

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
