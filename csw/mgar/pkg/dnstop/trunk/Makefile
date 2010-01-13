GARNAME = dnstop
GARVERSION = 20090128
CATEGORIES = net

DESCRIPTION = Displays various tables of DNS traffic
define BLURB
  Displays various tables of DNS traffic
endef

MASTER_SITES = http://dns.measurement-factory.com/tools/dnstop/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

LICENSE = LICENSE

REQUIRED_PKGS = CSWlibpcap

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

pre-build-modulated:
	@echo " ==> Pre-build $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
	   gpatch < ../../../../$(FILEDIR)/Makefile.p )
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@ginstall -m 755 -d $(DESTDIR)$(bindir)
	@ginstall -m 755 $(WORKSRC)/dnstop $(DESTDIR)$(bindir)
	@ginstall -m 755 -d $(DESTDIR)$(mandir)/man8
	@ginstall -m 444 $(WORKSRC)/dnstop.8 $(DESTDIR)$(mandir)/man8
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKSRC)/CHANGES $(DESTDIR)$(docdir)/$(GARNAME)
	@$(MAKECOOKIE)
