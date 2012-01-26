NAME = sauron
VERSION = 0.6.2
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Scalable system for management of DNS & DHCP services
define BLURB
  Scalable system for management of DNS & DHCP services
endef

MASTER_SITES = http://sauron.jyu.fi/pub/sauron/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

REQUIRED_PKGS = CSWperl CSWpostgresql

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_SCRIPTS = custom

include gar/category.mk

SPKG_SOURCEURL = http://sauron.jyu.fi

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
#	@rm -rf $(DESTDIR)
#	@ginstall -d $(DESTDIR)$(bindir)
#	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
#	@ginstall -d $(DESTDIR)$(mandir)/man1
	echo "DESTDIR: $(DESTDIR)"
	@( cd $(WORKSRC) ; \
	   gmake INSTALL_ROOT=$(DESTDIR) install )
#	   cp -r $(NAME) $(DESTDIR)$(bindir)/$(NAME) ; \
#	   cp -r README $(DESTDIR)$(docdir)/$(NAME) ; \
#	   cp -r $(NAME).1 $(DESTDIR)$(mandir)/man1/$(NAME).1 )
	@$(MAKECOOKIE)
