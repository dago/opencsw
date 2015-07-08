# readme for chroot pkg?
# owner/group for device files? (root:sys)
# dlz extensions problematic, remove source: /bin/tests/system, rm -rf dlzexternal

NAME = bind
VERSION = 9.9.7
GARTYPE = v2

# Enable these for Px-releases
RELEASE = P1
DISTVERSION = $(VERSION)-$(RELEASE)
SPKG_VERSION = $(VERSION)$(RELEASE)
DISTNAME = $(NAME)-$(VERSION)-$(RELEASE)
WORKSRC = $(WORKDIR)/$(DISTNAME)

DESCRIPTION = ISC BIND DNS reference implementation
define BLURB
endef

# Enable these for Px-releases
MASTER_SITES = http://ftp.isc.org/isc/bind9/$(VERSION)-$(RELEASE)/
DISTFILES  = $(DISTNAME).tar.gz

# Disable these for Px-releases
#MASTER_SITES = http://ftp.isc.org/isc/bind9/$(VERSION)/
#DISTFILES  = $(NAME)-$(VERSION).tar.gz

DISTFILES += CSWbindchroot.postinstall

LICENSE = COPYRIGHT

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWbind
CATALOGNAME_CSWbind = bind
SPKG_DESC_CSWbind = ISC BIND DNS main package
RUNTIME_DEP_PKGS_CSWbind += CSWbindutils
RUNTIME_DEP_PKGS_CSWbind += CSWlibbind
RUNTIME_DEP_PKGS_CSWbind += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWbind += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWbind += CSWlibxml2-2

PACKAGES += CSWbind-dev
CATALOGNAME_CSWbind-dev = bind_dev
SPKG_DESC_CSWbind-dev = ISC BIND DNS development package
RUNTIME_DEP_PKGS_CSWbind-dev  = CSWbind
RUNTIME_DEP_PKGS_CSWbind-dev += CSWlibbind

PACKAGES += CSWlibbind
CATALOGNAME_CSWlibbind = libbind
SPKG_DESC_CSWlibbind = ISC BIND DNS library package
RUNTIME_DEP_PKGS_CSWlibbind += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibbind += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibbind += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibbind += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibbind += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibbind += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlibbind += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibbind += CSWlibz1

PACKAGES += CSWbindutils
CATALOGNAME_CSWbindutils = bind_utils
SPKG_DESC_CSWbindutils = ISC BIND DNS utilities package
RUNTIME_DEP_PKGS_CSWbindutils += CSWlibbind
RUNTIME_DEP_PKGS_CSWbindutils += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWbindutils += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWbindutils += CSWlibreadline6

PACKAGES += CSWbindchroot
CATALOGNAME_CSWbindchroot = bind_chroot
SPKG_DESC_CSWbindchroot = ISC BIND DNS chroot package
RUNTIME_DEP_PKGS_CSWbindchroot = CSWbind
ARCHALL_CSWbindchroot = 1

GARCOMPILER = GNU

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-libtool
CONFIGURE_ARGS += --with-openssl=/opt/csw
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --enable-largefile
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/named
CONFIGURE_ARGS += --enable-rrl
#CONFIGURE_ARGS += --with-dlz-ldap=/opt/csw

EXTRA_MERGE_EXCLUDE_FILES = .*~ $(libdir)/.*\.a $(libdir)/.*\.la $(mandir)/man1/isc-config.sh.1 $(bindir)/isc-config.sh

PKGFILES_CSWbindutils  = $(bindir)/dig
PKGFILES_CSWbindutils += $(bindir)/host
PKGFILES_CSWbindutils += $(bindir)/nslookup
PKGFILES_CSWbindutils += $(bindir)/nsupdate
PKGFILES_CSWbind-dev   = $(PKGFILES_DEVEL)
PKGFILES_CSWbind-dev  += .*\.so
PKGFILES_CSWlibbind    = .*\.so\..*
PKGFILES_CSWbindchroot = .*chroot.*

TEST_SCRIPTS    = custom
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

CHECKPKG_OVERRIDES_CSWbindutils += surplus-dependency|CSWlibiconv2
CHECKPKG_OVERRIDES_CSWbind += surplus-dependency|CSWlibiconv2
CHECKPKG_OVERRIDES_CSWbind += surplus-dependency|CSWbindutils
CHECKPKG_OVERRIDES_CSWbind += surplus-dependency|CSWlibssl1-0-0
CHECKPKG_OVERRIDES_CSWbindutils += catalogname-does-not-match-pkgname|pkgname=CSWbindutils|catalogname=bind_utils|expected-catalogname=bindutils
CHECKPKG_OVERRIDES_CSWbindchroot += catalogname-does-not-match-pkgname|pkgname=CSWbindchroot|catalogname=bind_chroot|expected-catalogname=bindchroot

# Will not split out all these libs
CHECKPKG_OVERRIDES_CSWlibbind += shared-lib-pkgname-mismatch|file=opt/csw/lib/libbind9.so.90.0.13|soname=libbind9.so.90|pkgname=CSWlibbind|expected=CSWlibbind9-90
CHECKPKG_OVERRIDES_CSWlibbind += shared-lib-pkgname-mismatch|file=opt/csw/lib/libdns.so.106.1.1|soname=libdns.so.106|pkgname=CSWlibbind|expected=CSWlibdns106
CHECKPKG_OVERRIDES_CSWlibbind += shared-lib-pkgname-mismatch|file=opt/csw/lib/libisc.so.104.0.2|soname=libisc.so.104|pkgname=CSWlibbind|expected=CSWlibisc104
CHECKPKG_OVERRIDES_CSWlibbind += shared-lib-pkgname-mismatch|file=opt/csw/lib/libisccfg.so.90.2.4|soname=libisccfg.so.90|pkgname=CSWlibbind|expected=CSWlibisccfg90
CHECKPKG_OVERRIDES_CSWlibbind += shared-lib-pkgname-mismatch|file=opt/csw/lib/liblwres.so.91.0.2|soname=liblwres.so.91|pkgname=CSWlibbind|expected=CSWliblwres91
CHECKPKG_OVERRIDES_CSWlibbind += shared-lib-pkgname-mismatch|file=opt/csw/lib/libisccc.so.90.0.6|soname=libisccc.so.90|pkgname=CSWlibbind|expected=CSWlibisccc90

# Some new checks, have no idea about their relevance
CHECKPKG_OVERRIDES_CSWlibbind += no-direct-binding

include gar/category.mk

DOCLIST = README.CSW db.127.0.0 db.localhost named.conf named.root rndc.key

test-custom:
	@echo " ==> Testing $(NAME) (custom)"
	( cd $(WORKSRC) ; \
	  gmake force-test )
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/CSWbind.cswnamed $(DESTDIR)/etc/opt/csw/init.d/cswnamed
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
