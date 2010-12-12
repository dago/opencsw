NAME = bind
VERSION = 9.4.3
RELEASE = P3
DISTVERSION = $(VERSION)-$(RELEASE)
DISTNAME = $(NAME)-$(DISTVERSION)
WORKSRC = $(WORKDIR)/$(DISTNAME)
CATEGORIES = net

DESCRIPTION = ISC BIND reference implementation
define BLURB
  BIND is open-source software that implements the Domain Name System (DNS)
  protocols for the Internet. It is a reference implementation of those
  protocols, but it is also production-grade software, suitable for use in
  high-volume and high-reliability applications.
endef

UPSTREAM_MASTER_SITES = http://ftp.isc.org/isc/bind9/
MASTER_SITES = http://ftp.isc.org/isc/bind9/$(VERSION)-$(RELEASE)/
DISTFILES  = $(NAME)-$(VERSION)-$(RELEASE).tar.gz
DISTFILES += $(call admfiles,CSWbind,preinstall postinstall preremove)

LICENSE = COPYRIGHT
RUNTIME_DEP_PKGS = CSWosslrt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)-([A-Z][0-9])

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-libtool
CONFIGURE_ARGS += --with-openssl=/opt/csw
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --enable-largefile
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/named

INSTALL_SCRIPTS = custom

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)
SPKG_SOURCEURL = http://www.isc.org/software/bind
#SPKG_CLASSES = none cswinitsmf

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)
#	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
#	@cp $(FILEDIR)/CSWbind.cswnamed $(DESTDIR)/etc/opt/csw/init.d/cswnamed
	@ginstall -d $(DESTDIR)/etc/init.d
	@cp $(FILEDIR)/CSWbind.cswnamed $(DESTDIR)/etc/init.d/cswnamed
	@ginstall -d $(DESTDIR)/etc/opt/csw
	@cp $(FILEDIR)/CSWbind.named.conf.CSW $(DESTDIR)/etc/opt/csw/named.conf.CSW
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@cp $(FILEDIR)/CSWbind.README.CSW $(DESTDIR)$(docdir)/$(NAME)/README.CSW
	@cp $(FILEDIR)/CSWbind.db.127.0.0 $(DESTDIR)$(docdir)/$(NAME)/db.127.0.0
	@cp $(FILEDIR)/CSWbind.db.localhost $(DESTDIR)$(docdir)/$(NAME)/db.localhost
	@cp $(FILEDIR)/CSWbind.named.conf $(DESTDIR)$(docdir)/$(NAME)/named.conf
	@cp $(FILEDIR)/CSWbind.named.root $(DESTDIR)$(docdir)/$(NAME)/named.root
	@cp $(FILEDIR)/CSWbind.rndc.key $(DESTDIR)$(docdir)/$(NAME)/rndc.key
	( cd $(WORKSRC) ; \
	  gmake DESTDIR=$(DESTDIR) install )
	@$(MAKECOOKIE)
