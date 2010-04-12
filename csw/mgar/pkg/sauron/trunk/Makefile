GARNAME = sauron
GARVERSION = 0.6.2
CATEGORIES = utils

DESCRIPTION = Scalable system for management of DNS & DHCP services
define BLURB
  Scalable system for management of DNS & DHCP services
endef

MASTER_SITES = http://sauron.jyu.fi/pub/sauron/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

REQUIRED_PKGS = CSWperl CSWpostgresql

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check
INSTALL_SCRIPTS = custom

include gar/category.mk

SPKG_SOURCEURL = http://sauron.jyu.fi

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
#	@rm -rf $(DESTDIR)
#	@ginstall -d $(DESTDIR)$(bindir)
#	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
#	@ginstall -d $(DESTDIR)$(mandir)/man1
	echo "DESTDIR: $(DESTDIR)"
	@( cd $(WORKSRC) ; \
	   gmake INSTALL_ROOT=$(DESTDIR) install )
#	   cp -r $(GARNAME) $(DESTDIR)$(bindir)/$(GARNAME) ; \
#	   cp -r README $(DESTDIR)$(docdir)/$(GARNAME) ; \
#	   cp -r $(GARNAME).1 $(DESTDIR)$(mandir)/man1/$(GARNAME).1 )
	@$(MAKECOOKIE)
