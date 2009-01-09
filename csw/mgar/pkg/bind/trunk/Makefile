GARNAME = bind
GARVERSION = 9.6.0
RELEASE = P1
DISTVERSION = $(GARVERSION)-$(RELEASE)
DISTNAME = $(GARNAME)-$(DISTVERSION)
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
MASTER_SITES = http://ftp.isc.org/isc/bind9/$(GARVERSION)-$(RELEASE)/
DISTFILES  = $(GARNAME)-$(GARVERSION)-$(RELEASE).tar.gz
DISTFILES += $(call admfiles,CSWbind,preinstall preremove)
DISTFILES += $(call admfiles,CSWbinddevel,)
DISTFILES += $(call admfiles,CSWlibbind,)
DISTFILES += $(call admfiles,CSWbindutils,)

SPKG_DESC_CSWbind = ISC BIND main package
SPKG_DESC_CSWbinddevel = ISC BIND development package
SPKG_DESC_CSWlibbind = ISC BIND library package
SPKG_DESC_CSWbindutils = ISC BIND utilities package

REQUIRED_PKGS_CSWbind = CSWlibbind CSWbindutils CSWcswclassutils
REQUIRED_PKGS_CSWbinddevel = CSWbind
REQUIRED_PKGS_CSWlibbind = CSWiconv CSWlibxml2 CSWosslrt CSWzlib
REQUIRED_PKGS_CSWbindutils = CSWlibbind

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)-([A-Z][0-9])

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-libtool
CONFIGURE_ARGS += --with-openssl=/opt/csw
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --enable-largefile
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/named

EXTRA_MERGE_EXCLUDE_FILES = .*~ $(libdir)/.*\.a $(libdir)/.*\.la

PKGFILES_CSWbinddevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibbind   = $(libdir)/.*
PKGFILES_CSWbindutils = $(bindir)/.*

ENABLE_CHECK = 0

INSTALL_SCRIPTS = custom

PROTOTYPE_FILTER  = awk '$$$$3 ~ /\/init.d\/cswnamed$$$$/ { $$$$2 = "cswinitsmf" } $$$$3 ~ /\/named.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } $$$$3 ~ /\/var\/opt\/csw\/named/ { $$$$5 = "named" } { print }'

SPKG_SOURCEURL = http://www.isc.org/software/bind
SPKG_CLASSES_CSWbind = none cswcpsampleconf cswinitsmf

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@cp $(FILEDIR)/CSWbind.cswnamed $(DESTDIR)/etc/opt/csw/init.d/cswnamed
	@cp $(FILEDIR)/CSWbind.named.conf.CSW $(DESTDIR)/etc/opt/csw/named.conf.CSW
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@cp $(FILEDIR)/CSWbind.README.CSW $(DESTDIR)$(docdir)/$(GARNAME)/README.CSW
	@cp $(FILEDIR)/CSWbind.db.127.0.0 $(DESTDIR)$(docdir)/$(GARNAME)/db.127.0.0
	@cp $(FILEDIR)/CSWbind.db.localhost $(DESTDIR)$(docdir)/$(GARNAME)/db.localhost
	@cp $(FILEDIR)/CSWbind.named.conf $(DESTDIR)$(docdir)/$(GARNAME)/named.conf
	@cp $(FILEDIR)/CSWbind.named.root $(DESTDIR)$(docdir)/$(GARNAME)/named.root
	@cp $(FILEDIR)/CSWbind.rndc.key $(DESTDIR)$(docdir)/$(GARNAME)/rndc.key
	@cp $(WORKSRC)/COPYRIGHT $(DESTDIR)$(docdir)/$(GARNAME)/LICENSE
	( cd $(WORKSRC) ; \
	  gmake DESTDIR=$(DESTDIR) install )
	@touch $(DESTDIR)/var/opt/csw/named/named.pid
	@$(MAKECOOKIE)
