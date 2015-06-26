NAME = unbound
VERSION = 1.5.3
CATEGORIES = server
GARTYPE = v2
DESCRIPTION = A validating, recursive, and caching DNS resolver
define BLUR
  Unbound is designed as a set of modular components, so that also
  DNSSEC (secure DNS) validation and stub-resolvers (that do not run as
  a server, but are linked into an application) are easily possible.
endef

VENDOR_URL = http://www.unbound.net/
MASTER_SITES = http://unbound.net/downloads/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += cswunbound
DISTFILES += cswusergroup

PACKAGING_PLATFORMS +=  solaris10-sparc solaris10-i386
PACKAGES = CSWunbound CSWlibunbound2 CSWunbound-devel CSWunbound-host

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+#PATCHFILES += 0001-fix-preprocessing-bug.patchd+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREM_MASTER_SITES = 

#CONFIGURE_CONFIGURE_ARGS += --with-libevent=/opt/csw
CONFIGURE_ARGS += --with-libexpat=/opt/csw
CONFIGUTE_ARGS += --with-solaris-threads
CONFIGURE_ARGS += --with-ldns=/opt/csw
CONFIGURE_ARGS += --with-ssl=/opt/cswE_ARGS += --with-ssl
CONFIGURE_ARGS += --with-pidfile=/var/run/unbound.pid
CONFIGURE_ARGS += --syscCONFIGURE_ARGS += --enable-sharedconfdir=/etc/opt/csw

STRIP_LIBTOOL = 0

# make test doesn't work for the moment on Solaris
SKIPTEST = 1
# 64-Bit build disabled
#EXTRA_BUILD_ISAS_i386   = amd64
#EXTRA_BUILD_ISAS_sparc  = sparcv9

#MERGE_DIRS_isa-sparcv9  = $(libdir)
#MERGE_DIRS_isa-sparcv9 += $(sbindir)
#MERGE_DIRS_isa-amd64  = $(libdir)
#MERGE_DIRS_isa-amd64 += $(sbindir)

#ISAXEC_DIRS                  = $(sbindir)
#EXTRA_ISAEXEC_EXCLUDE_FILES  = $(sbindir)/unbound-anchor
#EXTRA_ISAEXEC_EXCLUDE_FILES += $(sbindir)/unbound-checkconf
#EXTRA_ISAEXEC_EXCLUDE_FILES += $(sbindir)/unbound-control
#EXTRA_ISAEXEC_EXCLUDE_FILES += $(sbindir)/unbound-control-setup
#EXTRA_ISAEXEC_EXCLUDE_FILES += $(sbindir)/unbound-host

#EXTRA_MERGE_EXCLUDE_FILES_isa-amd64  = $(prefix)/sbin/unbound-anchor
#EXTRA_MERGE_EXCLUDE_FILES_isa-amd64 += $(prefix)/sbin/unbound-checkconf
#EXTRA_MERGE_EXCLUDE_FILES_isa-amd64 += $(prefix)/sbin/unbound-control
#EXTRA_MERGE_EXCLUDE_FILES_isa-amd64 += $(prefix)/sbin/unbound-control-setup
#EXTRA_MERGE_EXCLUDE_FILES_isa-amd64 += $(prefix)/sbin/unbound-host

#EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9  = $(prefix)/sbin/unbound-anchor
#EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9 += $(prefix)/sbin/unbound-checkconf
#EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9 += $(prefix)/sbin/unbound-control
#EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9 += $(prefix)/sbin/unbound-control-setup
#EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9_isa-sparcv8plus+vis += $(prefix)/sbin/unbound-host

SPKG_CLASSES_CSWunbound = none cswusergroup cswcpsampleconf cswinitsmf
INITSMF                 = /etc/opt/csw/init.d/cswunbound
USERGROUP               = /etc/opt/csw/CSWunbound/cswusergroup
SAMPLECONF              = /etc/opt/csw/unbound/unbound.conf
USERGROUP               = /etc/opt/csw/pkg/CSWunbound/cswusergroup

CATALOGNAME_CSWunbound       = unbound
SPKG_DESC_CSWunbound         = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWunbound += CSWlibunbound2
RUNTIME_DEP_PKGS_CSWunbo#und += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWunbound += CSWlibldns1
RUNTIME_DEP_PKGS_CSW1-0-0 RUNTIME_DEP_PKGS_CSWunbound += CSWlibevent2-0-5 += CSWlibevent2-0-5

CATALOGNAME_CSWlibunbound2       = libunbound2
SPKG_DESC_CSWlibunbound2         = Library implementing DNS resolution and validation
PKGFILES_CSWlibunbound2       #  += $(PKGFILES_RT)
RUNTIME_DEP_PKGS_CSWlibunbound2 += CSWlibldns1
RUNTIME_DEP_PKGS_CSWlibu1-0-0 RUNTIME_DEP_PKGS_CSWlibunbound2 += CSWlibevent2-0-5 += CSWlibevent2-0-5

CATALOGNAME_CSWunbound-devel       = unbound_devel
SPKG_DESC_CSWunbound-devel         = $(DESCRIPTION) development package
PKGFILES_CSWunbound-devel         += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWunbound-devel += CSWlibunbound2

CATALOGNAME_CSWunbound-host       = unbound_host
SPKG_DESC_CSWunbound-host         = Unbound DNS lookup utility
PKGFILES_CSWunbound-host         += $(sbindir)/unbound-host
PKGFILES_CSWunbound-host         += $(mandir)/#RUNTIME_DEP_PKGS_CSWunbound-host += CSWlibldns1
RUNTIME_DEP_PKGS_CSWunbound-host += CSWlibunbound2
RUNTIME_DEP_PKGS_CSWunbound-host += CSWlibssl1-0-0 += CSWlibevent2-0-5

include gar/category.mk

post-install-modulated:
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswunbound $(DESTDIR)/etc/opt/csw/init.d/cswunbound
	@ginstall -d $(DESTDIR)/etc/opt/csw/pkg/CSWunbound
	@ginstall -m 755 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWunbound/cswusergro