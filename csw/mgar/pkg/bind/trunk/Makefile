GARNAME = bind
GARVERSION = 9.6.1
RELEASE = P2
DISTVERSION = $(GARVERSION)-$(RELEASE)
SPKG_VERSION = $(GARVERSION)$(RELEASE)
DISTNAME = $(GARNAME)-$(GARVERSION)-$(RELEASE)
WORKSRC = $(WORKDIR)/$(DISTNAME)
CATEGORIES = net

DESCRIPTION = ISC BIND DNS reference implementation
define BLURB
  BIND is open-source software that implements the Domain Name System (DNS)
  protocols for the Internet. It is a reference implementation of those
  protocols, but it is also production-grade software, suitable for use in
  high-volume and high-reliability applications.
endef

MASTER_SITES = http://ftp.isc.org/isc/bind9/$(GARVERSION)-$(RELEASE)/
DISTFILES  = $(DISTNAME).tar.gz
#MASTER_SITES = http://ftp.isc.org/isc/bind9/$(GARVERSION)/
#DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWbindchroot.postinstall

PACKAGES = CSWbind CSWbinddevel CSWlibbind CSWbindutils CSWbindchroot

CATALOGNAME_CSWbinddevel = bind_devel
CATALOGNAME_CSWbindutils = bind_utils
CATALOGNAME_CSWbindchroot = bind_chroot

ARCHALL_CSWbinddevel = 1
ARCHALL_CSWbindchroot = 1

LICENSE = COPYRIGHT

SPKG_DESC_CSWbind = ISC BIND DNS main package
SPKG_DESC_CSWbinddevel = ISC BIND DNS development package
SPKG_DESC_CSWlibbind = ISC BIND DNS library package
SPKG_DESC_CSWbindutils = ISC BIND DNS utilities package
SPKG_DESC_CSWbindchroot = ISC BIND DNS chroot package

REQUIRED_PKGS_CSWbind = CSWlibbind CSWbindutils CSWiconv CSWlibxml2 CSWosslrt CSWzlib
REQUIRED_PKGS_CSWbinddevel = CSWbind
REQUIRED_PKGS_CSWlibbind = CSWiconv CSWlibxml2 CSWosslrt CSWzlib
REQUIRED_PKGS_CSWbindutils = CSWlibbind CSWiconv CSWlibxml2 CSWosslrt CSWzlib
REQUIRED_PKGS_CSWbindchroot = CSWbind

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
PKGFILES_CSWbindchroot = .*chroot.*

INSTALL_SCRIPTS = custom

PROTOTYPE_FILTER  = awk ' \
	$$$$3 ~ /\/var\/opt\/csw\/named/ { $$$$2 = "ugfiles" ; $$$$5 = "named" ; $$$$6 = "named" } \
	{ print }'

INITSMF = /etc/opt/csw/init.d/cswnamed
SAMPLECONF = /etc/opt/csw/named.conf /etc/opt/csw/CSWbind/bind
USERGROUP = /etc/opt/csw/CSWbind/cswusergroup

SPKG_SOURCEURL = http://www.isc.org/software/bind

# Still needed because of ugfiles
SPKG_CLASSES_CSWbind = none cswusergroup ugfiles cswcpsampleconf cswinitsmf
SPKG_CLASSES_CSWbindchroot = none ugfiles

include gar/category.mk

DOCLIST = README.CSW db.127.0.0 db.localhost named.conf named.root rndc.key

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/CSWbind.cswnamed $(DESTDIR)/etc/opt/csw/init.d/cswnamed
	@ginstall -m 644 $(FILEDIR)/CSWbind.named.conf.CSW $(DESTDIR)/etc/opt/csw/named.conf
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/CSWbind
	@ginstall -m 444 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/CSWbind/
	@ginstall -m 644 $(FILEDIR)/bind.CSW $(DESTDIR)/etc/opt/csw/CSWbind/bind
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(GARNAME)
	@$(foreach DOC,$(DOCLIST),cp $(FILEDIR)/$(DOC) $(DESTDIR)$(docdir)/$(GARNAME);)
	( cd $(WORKSRC) ; \
	  gmake DESTDIR=$(DESTDIR) install )
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/named
	@touch $(DESTDIR)/var/opt/csw/named/named.pid
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/named/chroot/dev
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/named/chroot/etc/opt/csw
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/named/chroot/var/named
	@$(MAKECOOKIE)
