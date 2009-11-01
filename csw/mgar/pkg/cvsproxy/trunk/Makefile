GARNAME = cvsproxy
GARVERSION = 1.0.1
CATEGORIES = utils

DESCRIPTION = Provides a CVS proxy
define BLURB
  Provides a CVS proxy
endef

MASTER_SITES = http://www.sra.co.jp/people/m-kasahr/cvsproxy/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

REQUIRED_PKGS = CSWtcpwrap
SPKG_SOURCEURL = http://www.sra.co.jp/people/m-kasahr/cvsproxy

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

ETCSERVICES = /opt/csw/etc/pkg/$(GARNAME)/services
INETDCONF = /opt/csw/etc/pkg/$(GARNAME)/inetd.conf

include gar/category.mk

post-install-modulated:
	@echo "==> Post-install fixes"
	@ginstall -d -m 755 $(DESTDIR)$(docdir)/$(GARNAME)
	@cp $(WORKSRC)/README $(DESTDIR)$(docdir)/$(GARNAME)
	@cp $(WORKSRC)/NEWS $(DESTDIR)$(docdir)/$(GARNAME)
	@cp $(WORKSRC)/ChangeLog $(DESTDIR)$(docdir)/$(GARNAME)
	@mv $(DESTDIR)/opt/csw/libexec/cvsproxy $(DESTDIR)/opt/csw/libexec/cvsproxy.tmp
	@ginstall -d -m 755 $(DESTDIR)/opt/csw/libexec/$(GARNAME)
	@mv $(DESTDIR)/opt/csw/libexec/cvsproxy.tmp $(DESTDIR)/opt/csw/libexec/$(GARNAME)/cvsproxy
	@ginstall -d -m 755 $(DESTDIR)/opt/csw/etc/pkg/$(GARNAME)
	@cp $(FILEDIR)/services $(DESTDIR)/opt/csw/etc/pkg/$(GARNAME)
	@cp $(FILEDIR)/inetd.conf $(DESTDIR)/opt/csw/etc/pkg/$(GARNAME)
	@$(MAKECOOKIE)
