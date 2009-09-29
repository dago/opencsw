GARNAME = tnef
GARVERSION = 1.4.6
CATEGORIES = utils

DESCRIPTION = Unpacks Microsoft TNEF MIME attachments
define BLURB
  TNEF provides a way to unpack those pesky Microsoft MS-TNEF MIME attachments.
  It operates like tar in order to upack any files which may have been put into
  the MS-TNEF attachment instead of being attached seperately.
endef

MASTER_SITES = http://downloads.sourceforge.net/tnef/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

REQUIRED_PKGS = CSWggettextrt

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=57057
UPSTREAM_USE_SF = 1
UFILES_REGEX = v(\d+(?:\.\d+)*)

CONFIGURE_ARGS = $(DIRPATHS)

NOISALIST = 1

TEST_TARGET = check
INSTALL_SCRIPTS = custom

include gar/category.mk

SPKG_SOURCEURL = http://sourceforge.net/projects/tnef

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@( cd $(WORKSRC) ; \
	   cp -r src/$(GARNAME) $(DESTDIR)$(bindir)/$(GARNAME) ; \
	   cp -r doc/$(GARNAME).1 $(DESTDIR)$(mandir)/man1/$(GARNAME).1 )
	@$(MAKECOOKIE)
