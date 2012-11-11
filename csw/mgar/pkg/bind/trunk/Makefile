# readme for chroot pkg?
# owner/group for device files? (root:sys)

NAME = bind
VERSION = 9.8.4
#VERSION = 9.9.0
GARTYPE = v2

# Enable these for Px-releases
#RELEASE = rc1
#RELEASE = P4
#DISTVERSION = $(VERSION)-$(RELEASE)
#SPKG_VERSION = $(VERSION)$(RELEASE)
#DISTNAME = $(NAME)-$(VERSION)-$(RELEASE)
##DISTNAME = $(NAME)-$(VERSION)$(RELEASE)
#WORKSRC = $(WORKDIR)/$(DISTNAME)

DESCRIPTION = ISC BIND DNS reference implementation
define BLURB
  BIND is open-source software that implements the Domain Name System (DNS)
  protocols for the Internet. It is a reference implementation of those
  protocols, but it is also production-grade software, suitable for use in
  high-volume and high-reliability applications.
endef

# Enable these for Px-releases
#MASTER_SITES = http://ftp.isc.org/isc/bind9/$(VERSION)-$(RELEASE)/
##MASTER_SITES = http://ftp.isc.org/isc/bind9/$(VERSION)$(RELEASE)/
#DISTFILES  = $(DISTNAME).tar.gz

# Disable these for Px-releases
MASTER_SITES = http://ftp.isc.org/isc/bind9/$(VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

DISTFILES += CSWbindchroot.postinstall

LICENSE = COPYRIGHT

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWbind
CATALOGNAME_CSWbind = bind
SPKG_DESC_CSWbind = ISC BIND DNS main package
RUNTIME_DEP_PKGS_CSWbind  = CSWlibbind
RUNTIME_DEP_PKGS_CSWbind += CSWbindutils
RUNTIME_DEP_PKGS_CSWbind += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWbind += CSWlibldap2-4-2

PACKAGES += CSWbind-dev
CATALOGNAME_CSWbind-dev = bind_dev
SPKG_DESC_CSWbind-dev = ISC BIND DNS development package
RUNTIME_DEP_PKGS_CSWbind-dev  = CSWbind
RUNTIME_DEP_PKGS_CSWbind-dev += CSWlibbind

PACKAGES += CSWlibbind
CATALOGNAME_CSWlibbind = libbind
SPKG_DESC_CSWlibbind = ISC BIND DNS library package
RUNTIME_DEP_PKGS_CSWlibbind  = CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibbind += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibbind += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibbind += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlibbind += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibbind += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibbind += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWlibbind += CSWlibcom-err3

PACKAGES += CSWbindutils
CATALOGNAME_CSWbindutils = bind_utils
SPKG_DESC_CSWbindutils = ISC BIND DNS utilities package
RUNTIME_DEP_PKGS_CSWbindutils  = CSWlibbind
RUNTIME_DEP_PKGS_CSWbindutils += CSWlibkrb5-3

PACKAGES += CSWbindchroot
CATALOGNAME_CSWbindchroot = bind_chroot
SPKG_DESC_CSWbindchroot = ISC BIND DNS chroot package
RUNTIME_DEP_PKGS_CSWbindchroot = CSWbind
ARCHALL_CSWbindchroot = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libtool
CONFIGURE_ARGS += --with-openssl=/opt/csw
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --enable-largefile
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/named
CONFIGURE_ARGS += --with-dlz-ldap=/opt/csw

EXTRA_MERGE_EXCLUDE_FILES = .*~ $(libdir)/.*\.a $(libdir)/.*\.la

#EXTRA_INC = /opt/csw/include

PKGFILES_CSWbind-dev   = $(PKGFILES_DEVEL)
PKGFILES_CSWbind-dev  += .*\.so
PKGFILES_CSWlibbind    = .*\.so\..*
PKGFILES_CSWbindutils  = $(bindir)/.*
PKGFILES_CSWbindchroot = .*chroot.*

INSTALL_SCRIPTS = custom

PROTOTYPE_MODIFIERS = 1
PROTOTYPE_FILES_1   = /var/opt/csw/named.*
PROTOTYPE_CLASS_1   = ugfiles
PROTOTYPE_USER_1    = named
PROTOTYPE_GROUP_1   = named

INITSMF     = /etc/opt/csw/init.d/cswnamed
SAMPLECONF  = /etc/opt/csw/named.conf
SAMPLECONF += /etc/opt/csw/bind.keys
SAMPLECONF += /etc/opt/csw/pkg/CSWbind/bind
USERGROUP   = /etc/opt/csw/pkg/CSWbind/cswusergroup

SPKG_SOURCEURL = http://www.isc.org/software/bind

CHECKPKG_OVERRIDES_CSWbind += surplus-dependency|CSWbindutils
CHECKPKG_OVERRIDES_CSWbindutils += catalogname-does-not-match-pkgname|pkgname=CSWbindutils|catalogname=bind_utils|expected-catalogname=bindutils
CHECKPKG_OVERRIDES_CSWbindchroot += catalogname-does-not-match-pkgname|pkgname=CSWbindchroot|catalogname=bind_chroot|expected-catalogname=bindchroot
# Will not split out all these libs
CHECKPKG_OVERRIDES_CSWlibbind += shared-lib-pkgname-mismatch|file=opt/csw/lib/libbind9.so.80.0.7|soname=libbind9.so.80|pkgname=CSWlibbind|expected=CSWlibbind9-80
CHECKPKG_OVERRIDES_CSWlibbind += shared-lib-pkgname-mismatch|file=opt/csw/lib/libdns.so.88.1.1|soname=libdns.so.88|pkgname=CSWlibbind|expected=CSWlibdns88
CHECKPKG_OVERRIDES_CSWlibbind += shared-lib-pkgname-mismatch|file=opt/csw/lib/libisc.so.84.1.0|soname=libisc.so.84|pkgname=CSWlibbind|expected=CSWlibisc84
CHECKPKG_OVERRIDES_CSWlibbind += shared-lib-pkgname-mismatch|file=opt/csw/lib/libisccc.so.80.0.2|soname=libisccc.so.80|pkgname=CSWlibbind|expected=CSWlibisccc80
CHECKPKG_OVERRIDES_CSWlibbind += shared-lib-pkgname-mismatch|file=opt/csw/lib/libisccfg.so.82.0.3|soname=libisccfg.so.82|pkgname=CSWlibbind|expected=CSWlibisccfg82
CHECKPKG_OVERRIDES_CSWlibbind += shared-lib-pkgname-mismatch|file=opt/csw/lib/liblwres.so.80.0.3|soname=liblwres.so.80|pkgname=CSWlibbind|expected=CSWliblwres80

include gar/category.mk

DOCLIST = README.CSW db.127.0.0 db.localhost named.conf named.root rndc.key

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/CSWbind.cswnamed $(DESTDIR)/etc/opt/csw/init.d/cswnamed
#	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw
	@ginstall -m 644 $(FILEDIR)/CSWbind.named.conf.CSW $(DESTDIR)/etc/opt/csw/named.conf
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWbind
	@ginstall -m 444 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWbind/
	@ginstall -m 644 $(FILEDIR)/bind.CSW $(DESTDIR)/etc/opt/csw/pkg/CSWbind/bind
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(NAME)
	@$(foreach DOC,$(DOCLIST),cp $(FILEDIR)/$(DOC) $(DESTDIR)$(docdir)/$(NAME);)
	( cd $(WORKSRC) ; \
	  gmake DESTDIR=$(DESTDIR) install )
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/named
	@touch $(DESTDIR)/var/opt/csw/named/named.pid
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/named/chroot/dev
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/named/chroot/etc/opt/csw
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/named/chroot/var/named
	@$(MAKECOOKIE)
