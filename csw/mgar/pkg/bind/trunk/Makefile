# readme for chroot pkg?
# owner/group for device files? (root:sys)

NAME = bind
VERSION = 9.7.2
CATEGORIES = net

# Enable these for Px-releases
RELEASE = P3
DISTVERSION = $(VERSION)-$(RELEASE)
SPKG_VERSION = $(VERSION)$(RELEASE)
DISTNAME = $(NAME)-$(VERSION)-$(RELEASE)
WORKSRC = $(WORKDIR)/$(DISTNAME)

DESCRIPTION = ISC BIND DNS reference implementation
define BLURB
  BIND is open-source software that implements the Domain Name System (DNS)
  protocols for the Internet. It is a reference implementation of those
  protocols, but it is also production-grade software, suitable for use in
  high-volume and high-reliability applications.
endef

# Enable these for Px-releases
MASTER_SITES = http://ftp.isc.org/isc/bind9/$(VERSION)-$(RELEASE)/
DISTFILES  = $(DISTNAME).tar.gz

# Disable these for Px-releases
#MASTER_SITES = http://ftp.isc.org/isc/bind9/$(VERSION)/
#DISTFILES  = $(NAME)-$(VERSION).tar.gz

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

RUNTIME_DEP_PKGS_CSWbind = CSWlibbind CSWbindutils CSWiconv CSWlibxml2 CSWosslrt CSWzlib
RUNTIME_DEP_PKGS_CSWbinddevel = CSWbind
RUNTIME_DEP_PKGS_CSWlibbind = CSWiconv CSWlibxml2 CSWosslrt CSWzlib
RUNTIME_DEP_PKGS_CSWbindutils = CSWlibbind CSWiconv CSWlibxml2 CSWosslrt CSWzlib
RUNTIME_DEP_PKGS_CSWbindchroot = CSWbind

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
PKGFILES_CSWbinddevel += .*\.so
PKGFILES_CSWlibbind = .*\.so\..*
PKGFILES_CSWbindutils = $(bindir)/.*
PKGFILES_CSWbindchroot = .*chroot.*

INSTALL_SCRIPTS = custom

PROTOTYPE_MODIFIERS = 1
PROTOTYPE_FILES_1 = /var/opt/csw/named.*
PROTOTYPE_CLASS_1 = ugfiles
PROTOTYPE_USER_1 = named
PROTOTYPE_GROUP_1 = named

INITSMF = /etc/opt/csw/init.d/cswnamed
SAMPLECONF  = /etc/opt/csw/named.conf
SAMPLECONF += /etc/opt/csw/bind.keys
SAMPLECONF += /etc/opt/csw/pkg/CSWbind/bind
USERGROUP = /etc/opt/csw/pkg/CSWbind/cswusergroup

SPKG_SOURCEURL = http://www.isc.org/software/bind

CHECKPKG_OVERRIDES_CSWbind += surplus-dependency|CSWbindutils
CHECKPKG_OVERRIDES_CSWbindchroot += surplus-dependency|CSWbind
CHECKPKG_OVERRIDES_CSWbinddevel += archall-devel-package
CHECKPKG_OVERRIDES_CSWlibbind += non-uniform-lib-versions-in-package|sonames=['libbind9.so.60',|'libdns.so.69',|'libisc.so.62',|'libisccc.so.60',|'libisccfg.so.62',|'liblwres.so.60']

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
