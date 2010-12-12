NAME = tnef
VERSION = 1.4.7
CATEGORIES = utils

DESCRIPTION = Unpacks Microsoft TNEF MIME attachments
define BLURB
  TNEF provides a way to unpack those pesky Microsoft MS-TNEF MIME attachments.
  It operates like tar in order to upack any files which may have been put into
  the MS-TNEF attachment instead of being attached seperately.
endef

MASTER_SITES = http://downloads.sourceforge.net/tnef/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS = CSWggettextrt

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=57057
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

#GARCOMPILER=GCC4
CONFIGURE_ARGS = $(DIRPATHS)
#OPT_FLAGS_SOS = -xO2

NOISALIST = 1

TEST_TARGET = check
INSTALL_SCRIPTS = custom

include gar/category.mk

SPKG_SOURCEURL = http://sourceforge.net/projects/tnef

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@( cd $(WORKSRC) ; \
	   cp -r src/$(NAME) $(DESTDIR)$(bindir)/$(NAME) ; \
	   cp -r doc/$(NAME).1 $(DESTDIR)$(mandir)/man1/$(NAME).1 )
	@$(MAKECOOKIE)
