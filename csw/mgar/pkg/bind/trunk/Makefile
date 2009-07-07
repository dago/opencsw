# remove named.pid or change to type v

GARNAME = bind
GARVERSION = 9.6.1
#RELEASE = P1
#DISTVERSION = $(GARVERSION)-$(RELEASE)
#DISTNAME = $(GARNAME)-$(DISTVERSION)
#WORKSRC = $(WORKDIR)/$(DISTNAME)
CATEGORIES = net

DESCRIPTION = ISC BIND DNS reference implementation
define BLURB
  BIND is open-source software that implements the Domain Name System (DNS)
  protocols for the Internet. It is a reference implementation of those
  protocols, but it is also production-grade software, suitable for use in
  high-volume and high-reliability applications.
endef

UPSTREAM_MASTER_SITES = http://ftp.isc.org/isc/bind9/
#MASTER_SITES = http://ftp.isc.org/isc/bind9/$(GARVERSION)-$(RELEASE)/
#DISTFILES  = $(GARNAME)-$(GARVERSION)-$(RELEASE).tar.gz
MASTER_SITES = http://ftp.isc.org/isc/bind9/$(GARVERSION)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWbind CSWbinddevel CSWlibbind CSWbindutils

CATALOGNAME_CSWbinddevel = bind_devel
CATALOGNAME_CSWbindutils = bind_utils

ARCHALL_CSWbinddevel = 1

LICENSE = COPYRIGHT

SPKG_DESC_CSWbind = ISC BIND DNS main package
SPKG_DESC_CSWbinddevel = ISC BIND DNS development package
SPKG_DESC_CSWlibbind = ISC BIND DNS library package
SPKG_DESC_CSWbindutils = ISC BIND DNS utilities package

REQUIRED_PKGS_CSWbind = CSWlibbind CSWbindutils CSWcswclassutils
REQUIRED_PKGS_CSWbinddevel = CSWbind
REQUIRED_PKGS_CSWlibbind = CSWiconv CSWlibxml2 CSWosslrt CSWzlib
REQUIRED_PKGS_CSWbindutils = CSWlibbind CSWiconv CSWlibxml2 CSWosslrt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)(-([A-Z][0-9]))?

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

# checkpkg can't handle split packages
ENABLE_CHECK = 0

INSTALL_SCRIPTS = custom

# fix class for conf file and named files
PROTOTYPE_FILTER  = awk ' \
	$$$$3 ~ /\/init.d\/cswnamed$$$$/ { $$$$2 = "cswinitsmf" } \
	$$$$3 ~ /\/named.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
	$$$$3 ~ /\/var\/opt\/csw\/named/ { $$$$5 = "named" ; $$$$2 = "ugfiles" } \
	$$$$3 ~ /\/CSWbind\/cswusergroup$$$$/ { $$$$2 = "cswusergroup" } \
	{ print }'

SPKG_SOURCEURL = http://www.isc.org/software/bind
# use usergroup class also
SPKG_CLASSES_CSWbind = none cswusergroup cswugfiles cswcpsampleconf cswinitsmf

include gar/category.mk

#SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

DOCLIST = README.CSW db.127.0.0 db.localhost named.conf named.root rndc.key

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@cp $(FILEDIR)/CSWbind.cswnamed $(DESTDIR)/etc/opt/csw/init.d/cswnamed
	@cp $(FILEDIR)/CSWbind.named.conf.CSW $(DESTDIR)/etc/opt/csw/named.conf.CSW
	@ginstall -d $(DESTDIR)/etc/opt/csw/CSWbind
	@cp $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/CSWbind/
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@$(foreach DOC,$(DOCLIST),cp $(FILEDIR)/$(DOC) $(DESTDIR)$(docdir)/$(GARNAME);)
	( cd $(WORKSRC) ; \
	  gmake DESTDIR=$(DESTDIR) install )
	@touch $(DESTDIR)/var/opt/csw/named/named.pid
	@$(MAKECOOKIE)
