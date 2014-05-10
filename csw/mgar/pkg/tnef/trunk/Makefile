NAME = tnef
VERSION = 1.4.10
GARTYPE = v2

DESCRIPTION = Unpacks Microsoft TNEF MIME attachments
define BLURB
endef

MASTER_SITES = http://downloads.sourceforge.net/tnef/
DISTFILES    = $(NAME)-$(VERSION).tar.gztnef += CSWlibintl8

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
	   cp -r doc/$(NAME).1 $(DESTDIR)$(mandir)/man1/$(NAME).1