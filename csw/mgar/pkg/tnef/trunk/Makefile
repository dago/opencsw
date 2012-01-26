NAME = tnef
VERSION = 1.4.8
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Unpacks Microsoft TNEF MIME attachments
define BLURB
  TNEF provides a way to unpack those pesky Microsoft MS-TNEF MIME attachments.
  It operates like tar in order to upack any files which may have been put into
  the MS-TNEF attachment instead of being attached seperately.
endef

MASTER_SITES = http://downloads.sourceforge.net/tnef/
DISTFILES    = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS_CSWtnef += CSWlibintl8

CONFIGURE_ARGS = $(DIRPATHS)

NOISALIST = 1

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
