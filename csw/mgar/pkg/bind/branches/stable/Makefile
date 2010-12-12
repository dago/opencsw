NAME = bind
VERSION = 9.4.3
RELEASE = P3
DISTVERSION = $(VERSION)-$(RELEASE)
DISTNAME = $(NAME)-$(DISTVERSION)
WORKSRC = $(WORKDIR)/$(DISTNAME)
CATEGORIES = net

DESCRIPTION = ISC BIND DNS reference implementation
define BLURB
  BIND is open-source software that implements the Domain Name System (DNS)
  protocols for the Internet. It is a reference implementation of those
  protocols, but it is also production-grade software, suitable for use in
  high-volume and high-reliability applications.
endef

MASTER_SITES = http://ftp.isc.org/isc/bind9/$(VERSION)-$(RELEASE)/
DISTFILES  = $(NAME)-$(VERSION)-$(RELEASE).tar.gz
#MASTER_SITES = http://ftp.isc.org/isc/bind9/$(VERSION)/
#DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWbind CSWbinddevel CSWlibbind CSWbindutils

CATALOGNAME_CSWbinddevel = bind_devel
CATALOGNAME_CSWbindutils = bind_utils

ARCHALL_CSWbinddevel = 1

LICENSE = COPYRIGHT

SPKG_DESC_CSWbind = ISC BIND DNS main package
SPKG_DESC_CSWbinddevel = ISC BIND DNS development package
SPKG_DESC_CSWlibbind = ISC BIND DNS library package
SPKG_DESC_CSWbindutils = ISC BIND DNS utilities package

RUNTIME_DEP_PKGS_CSWbind = CSWlibbind CSWbindutils CSWcswclassutils
RUNTIME_DEP_PKGS_CSWbinddevel = CSWbind
RUNTIME_DEP_PKGS_CSWlibbind = CSWiconv CSWlibxml2 CSWosslrt CSWzlib
RUNTIME_DEP_PKGS_CSWbindutils = CSWlibbind CSWiconv CSWlibxml2 CSWosslrt

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = http://ftp.isc.org/isc/bind9/
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS  = $(DIRPATHS)
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

# checkpkg can't handle split packages
ENABLE_CHECK = 0

INSTALL_SCRIPTS = custom

PROTOTYPE_FILTER  = awk ' \
	$$$$3 ~ /\/init.d\/cswnamed$$$$/ { $$$$2 = "cswinitsmf" } \
	$$$$3 ~ /\/named.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
	$$$$3 ~ /\/var\/opt\/csw\/named/ { $$$$5 = "named" ; $$$$2 = "ugfiles" } \
	$$$$3 ~ /\/CSWbind\/cswusergroup$$$$/ { $$$$2 = "cswusergroup" } \
	{ print }'

SPKG_SOURCEURL = http://www.isc.org/software/bind
SPKG_CLASSES_CSWbind = none cswusergroup ugfiles cswcpsampleconf cswinitsmf

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

DOCLIST = README.CSW db.127.0.0 db.localhost named.conf named.root rndc.key

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@cp $(FILEDIR)/CSWbind.cswnamed $(DESTDIR)/etc/opt/csw/init.d/cswnamed
	@cp $(FILEDIR)/CSWbind.named.conf.CSW $(DESTDIR)/etc/opt/csw/named.conf.CSW
	@ginstall -d $(DESTDIR)/opt/csw/etc/CSWbind
	@cp $(FILEDIR)/cswusergroup $(DESTDIR)/opt/csw/etc/CSWbind/
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@$(foreach DOC,$(DOCLIST),cp $(FILEDIR)/$(DOC) $(DESTDIR)$(docdir)/$(NAME);)
	( cd $(WORKSRC) ; \
	  gmake DESTDIR=$(DESTDIR) install )
	@ginstall -d $(DESTDIR)/var/opt/csw/named
	@touch $(DESTDIR)/var/opt/csw/named/named.pid
	@$(MAKECOOKIE)
