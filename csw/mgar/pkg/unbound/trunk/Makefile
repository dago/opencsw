GARNAME = unbound
GARVERSION = 1.4.7
CATEGORIES = server

DESCRIPTION = A validating, recursive, and caching DNS resolver
define BLUR
  Unbound is designed as a set of modular components, so that also
  DNSSEC (secure DNS) validation and stub-resolvers (that do not run as
  a server, but are linked into an application) are easily possible.
endef

PACKAGES = CSWunbound CSWlibunbound2 CSWunbound-devel
CATALOGNAME_CSWunbound = unbound
CATALOGNAME_CSWlibunbound2 = libunbound2
CATALOGNAME_CSWunbound-devel = unbound_devel
LICENSE = LICENSE

MASTER_SITES = http://unbound.net/downloads/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += cswunbound
DISTFILES += cswusergroup

EXTRA_BUILD_ISAS_i386  = pentium_pro
EXTRA_BUILD_ISAS_sparc = sparcv8plus

MERGE_DIRS_isa-sparcv8plus  = $(libdir)
MERGE_DIRS_isa-sparcv8plus += $(sbindir)
MERGE_DIRS_isa-pentium_pro  = $(libdir)
MERGE_DIRS_isa-pentium_pro += $(sbindir)

ISAXEC_DIRS = $(sbindir)
ISAEXEC_EXCLUDE_FILES  = $(sbindir)/unbound-anchor
ISAEXEC_EXCLUDE_FILES += $(sbindir)/unbound-checkconf
ISAEXEC_EXCLUDE_FILES += $(sbindir)/unbound-control
ISAEXEC_EXCLUDE_FILES += $(sbindir)/unbound-control-setup
ISAEXEC_EXCLUDE_FILES += $(sbindir)/unbound-host

EXTRA_MERGE_EXCLUDE_FILES_isa-pentium_pro  = $(prefix)/sbin/unbound-anchor
EXTRA_MERGE_EXCLUDE_FILES_isa-pentium_pro += $(prefix)/sbin/unbound-checkconf
EXTRA_MERGE_EXCLUDE_FILES_isa-pentium_pro += $(prefix)/sbin/unbound-control
EXTRA_MERGE_EXCLUDE_FILES_isa-pentium_pro += $(prefix)/sbin/unbound-control-setup
EXTRA_MERGE_EXCLUDE_FILES_isa-pentium_pro += $(prefix)/sbin/unbound-host

EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv8plus  = $(prefix)/sbin/unbound-anchor
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv8plus += $(prefix)/sbin/unbound-checkconf
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv8plus += $(prefix)/sbin/unbound-control
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv8plus += $(prefix)/sbin/unbound-control-setup
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv8plus += $(prefix)/sbin/unbound-host

SPKG_CLASSES_CSWunbound = none cswusergroup cswcpsampleconf cswinitsmf
PROTOTYPE_FILTER = awk '$$$$3 ~ /\/init.d\/cswunbound$$$$/ { $$$$2 = "cswinitsmf" } $$$$3 ~ /\/CSWunbound\/cswusergroup$$$$/ { $$$$2 = "cswusergroup" } $$$$3 ~ /\/unbound\/unbound.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } { print }'

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGING_PLATFORMS +=  solaris9-sparc solaris9-i386

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGUTE_ARGS += --with-solaris-threads
CONFIGURE_ARGS += --with-ldns=/opt/csw
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --with-libevent=/opt/csw
CONFIGURE_ARGS += --with-libexpat=/opt/csw
CONFIGURE_ARGS += --with-pidfile=/var/run/unbound.pid
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw

# Gost requiers OpenSSL 1.0
CONFIGURE_ARGS += --disable-gost

STRIP_LIBTOOL = 0

SPKG_DESC_CSWunbound = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWunbound += CSWlibunbound2
RUNTIME_DEP_PKGS_CSWunbound += CSWexpat
RUNTIME_DEP_PKGS_CSWunbound += CSWlibevent
RUNTIME_DEP_PKGS_CSWunbound += CSWlibldns1
RUNTIME_DEP_PKGS_CSWunbound += CSWosslrt

SPKG_DESC_CSWlibunbound2 = Library implementing DNS resolution and validation
PKGFILES_CSWlibunbound2 += $(PKGFILES_RT)
RUNTIME_DEP_PKGS_CSWlibunbound2 += CSWlibldns1
RUNTIME_DEP_PKGS_CSWlibunbound2 += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibunbound2 += CSWlibevent

SPKG_DESC_CSWunbound-devel = $(DESCRIPTION) development package
PKGFILES_CSWunbound-devel += $(PKGFILES_DEVEL)

# make test doesn't work for the moment on Solaris
SKIPTEST = 1

post-install-modulated:
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswunbound $(DESTDIR)/etc/opt/csw/init.d/cswunbound
	@ginstall -d $(DESTDIR)/etc/opt/csw/pkg/CSWunbound
	@ginstall -m 755 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWunbound/cswusergroup
	@mv $(DESTDIR)/etc/opt/csw/unbound/unbound.conf $(DESTDIR)/etc/opt/csw/unbound/unbound.conf.CSW
	@chmod 444 $(DESTDIR)/etc/opt/csw/unbound/unbound.conf.CSW
	@$(MAKECOOKIE)

include gar/category.mk
