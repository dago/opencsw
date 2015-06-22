# $Id$

NAME = openldap
VERSION = 2.4.40
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = Open source implementation of the Lightweight Directory Access Protocol
define BLURB
  The OpenLDAP Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and open source LDAP suite of applications
  and development tools. The project is managed by a worldwide community of
  volunteers that use the Internet to communicate, plan, and develop the
  OpenLDAP Suite and its related documentation.
endef

MASTER_SITES = ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/
DISTFILES  = $(DISTNAME).tgz
DISTFILES += CSWoldap.postinstall
DISTFILES += README.CSW openldaprc
DISTFILES += cswop# This is the 32/64 exec wrapper
DISTFILES += slapd

GARCOMPILER += SOS12U3

EXPANDVARS += CSWoldap.postinstall
EXPANDVARS += cswopenldap
EXPANDVARS += slapd

PATCHFILES += patch-oldap-2.4.16-ntlm.diff

# Use patch until this is fixed:
#   http://www.openldap.org/its/index.cgi/Build?id=6306
PATCHFILES += patch-libtool-64bit.diff

DISTFILES += patch-oldap-2.4.16-ntlm.diff

p-2.4.16-ntlm.diff

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# Maybe in
#   /opt/csw/share/man/man5/ldap.conf.5
# the string
#   /usr/local/var/ldapi
# should be replaced by something more sane in the future.

VENDOR_URL = http://www.openldap.org

LICENSE = COPYRIGHT

BUILD_DEP_PKGS += CSWbdb48devel
BUILD_DEP_PKGS += CSWlibicu-dev
BUILD_DEP_PKGS += CSWlibtool
BUILD_DEP_PKGS += CSWunixodbc-dev
BUILD_DEP_PKGS += CSWsasl-dev
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibwrap-dev
BUILD_DEP_PKGS += CSWperl

PACKAGES += CSWopenldap
SPKG_DESC_CSWopenldap = OpenLDAP server for Lightweight Directory Access Protocol
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWopenldap += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWopenldap += CSWlibldap-r2-4-2
RUNTIME_DEP_PKGS_CSWopenldap += CSWlibltdl7
# We do not want that dependency.
# RUNTIME_DEP_PKGS_CSWopenldap += CSWlibnet
# RUNTIME_DEP_PKGS_CSWopenldap += CSWlibnet1
RUNTIME_DEP_PKGS_CSWopenldap += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWopenldap += CSWlibslp1
RUNTIME_DEP_PKGS_CSWopenldap += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWopenRUNTIME_DEP_PKGS_CSWopenldap += CSWlibuuid1
RUNTIME_DEP_PKGS_CSWopenldap += CSWlibicuuc55
#OBSOLETED_BY_CSWopenldap += CSWoldap
#penldap += CSWoldap
CATALOGNAME_CSWoldre/man/man8/slapd.8

# This is most certainly a false positive
CHECKPKG_OVERRIDES_CSWopenldap += missing-dependency|CSWopenldap-back-bdb

PACKAGES += CSWopenldap-client
SPKG_DESC_CSWopenldap-client = OpenLDAP client executables
PKGFILES_CSWopenldap-client += $(bindir)/.*
PKGFILES_CSWopenldap-client += $(mandir)/man1/.*
RUNTIME_DEP_PKGS_CSWopenldap-client += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWopenldap-client += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWopenldap-clie#OBSOLETED_BY_CSWopenldap-client += CSWoldapclient
#t += CSWoldapclient
CATALOGNAME_CSWoldapclient = openldap_client_stub

PACKAGES += CSWopenldap-dev
SPKG_DESC_CSWopenldap-dev = OpenLDAP development files for libldap-2.4.so.2, libldap_r-2.4.so.2 and liblber-2.4.so.2
PKGFILES_CSWopenldap-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWopenldap-dev += $(mandir)/man3/.*
RUNTIME_DEP_PKGS_CSWopenldap-dev += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWopenldap-dev += CSWlibldap-r2-4-2
RUNTIME_DEP_PKGS_CSWopenldap-dev#OBSOLETED_BY_CSWopenldap-dev += CSWoldapdevel
#ev += CSWoldapdevel
CATALOGNAME_CSWoldapdevel = openldap_devel_stub

PACKAGES += CSWopenldap-back-perl
SPKG_DESC_CSWopenldap-back-perl = OpenLDAP Perl backend
PKGFILES_CSWopenldap-back-perl += $(call baseisadirs,$(libexecdir),openldap/back_perl.*)
PKGFILES_CSWopenldap-back-perl += $(mandir)/man5/slapd-perl.5
RUNTIME_DEP_PKGS_CSWopenldap-back-perl += CSWperl
RUNTIME_DEP_PKGS_CSWopenldap-back-perl += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWopenldap-back-perl += CSWlibldap-r2-4-2
RUNTIME_DEP_PKGS_CSWopenldap-back-p# We don't have 64 bit Perl yet
CHECKPKG_OVERRIDES_CSWopenldap-back-perl += 64-bit-binaries-missing-perl += CSWopenldap

PACKAGES += CSWopenldap-back-bdb
SPKG_DESC_CSWopenldap-back-bdb = OpenLDAP BerkerleyDB bdb backend
PKGFILES_CSWopenldap-back-bdb += $(call baseisadirs,$(libexecdir),openldap/back_bdb.*)
PKGFILES_CSWopenldap-back-bdb += $(mandir)/man5/slapd-bdb.5
RUNTIME_DEP_PKGS_CSWopenldap-back-bdb += CSWbdb48
RUNTIME_DEP_PKGS_CSWopenldap-back-bdb += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWopenldap-back-bdb += CSWlibldap-r2-4-2
RUNTIME_DEP_PKGS_CSWopenldap-back-bdb += CSWopenldap

PACKAGES += CSWopenldap-back-hdb
SPKG_DESC_CSWopenldap-back-hdb = OpenLDAP BerkerleyDB hdb backend
PKGFILES_CSWopenldap-back-hdb += $(call baseisadirs,$(libexecdir),openldap/back_hdb.*)
RUNTIME_DEP_PKGS_CSWopenldap-back-hdb += CSWbdb48
RUNTIME_DEP_PKGS_CSWopenldap-back-hdb += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWopenldap-back-hdb += CSWlibldap-r2-4-2
RUNTIME_DEP_PKGS_CSWopenldap-back-hdb += CSWopenldap

PACKAGES += CSWopenldap-back-sql
SPKG_DESC_CSWopenldap-back-sql = OpenLDAP SQL backend
PKGFILES_CSWopenldap-back-sql += $(call baseisadirs,$(libexecdir),openldap/back_sql.*)
PKGFILES_CSWopenldap-back-sql += $(mandir)/man5/slapd-sql.5
RUNTIME_DEP_PKGS_CSWopenldap-back-sql += CSWlibodbc2
RUNTIME_DEP_PKGS_CSWopenldap-back-sql += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWopenldap-back-sql += CSWlibldap-r2-4-2
RUNTIME_DEP_PKGS_CSWopenldap-back-sql += CSWopenldap

PACKAGES += CSWliblber2-4-2
SPKG_DESC_CSWliblber2-4-2 = OpenLDAP ASN.1 BER library, liblber-2.4.so.2
PKGFILES_CSWliblber2-4-2 += $(call pkgfiles_lib,liblber-2.4.so.2)
RUNTIME_DEP_PKGS_CSWlibldap2-4-2 += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWlibldap2-4-#OBSOLETED_BY_CSWliblber2-4-2 += CSWoldaprt
#2-4-2 += CSWoldaprt
CATALOGNAME_CSWoldaprt = openldap_rt_stub

PACKAGES += CSWlibldap2-4-2
SPKG_DESC_CSWlibldap2-4-2 = OpenLDAP LDAP library, libldap-2.4.so.2
PKGFILES_CSWlibldap2-4-2 += $(call pkgfiles_lib,libldap-2.4.so.2)
PKGFILES_CSWlibldap2-4-2 += $(sysconfdir)/ldap.conf
PKGFILES_CSWlibldap2-4-2 += $(mandir)/man5/ldap.conf.5
RUNTIME_DEP_PKGS_CSWlibldap2-4-2# += CSWliblber2-4-2
OBSOLETED_BY_CSWlibldap2an/man5/ldap.conf.5

PACKAGES += CSWlibldap-r2-4-2
SPKG_DESC_CSWlibldap-r2-4-2 = OpenLDAP reentrant LDAP library, libldap_r-2.4.so.2
PKGFILES_CSWlibldap-r2-4-2 += $(call pkgfiles_lib,libldap_r-2.4.so.2)
RUNTIME_DEP_PKGS_CSWlibldap-r2-4-2 += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWlibldap-r2-4-2 += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWlibldap-r2-4-#2 += CSWlibssl1-0-0
OBSOLETED_BY_CSWlibldap-r2-4-2 += CSWoldaprt

EXTRE.CSW $(PATCHFILES) openldaprc

# This is also used during EXPANDVARS
bdbdir = $(prefix)/bdb48

EXTRA_LIB = $(bdbdir)/lib 
EXTRA_INC = $(bdbdir)/include

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

MIGRATE_FILES_CSWoldapclient = openldap

# Is this causing this?
#   https://www.opencsw.org/mantis/view.php?id=4555
NOISALIST = 1
#LD_OPTIONS =
#EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS) -z ignore
EXTRA_LINKER_FLAGS = -lrt

NODIRPATHS = --docdir

BUILD64 = 1

# This takes some more work, the sbin/ files should be linked to libexec but the linklevel s not deep enough
# ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-crypt
CONFIGURE_ARGS += --enable-lmpasswd
CONFIGURE_ARGS += --enable-modules
CONFIGURE_ARGS += --enable-rlookups
CONFIGURE_ARGS += --enable-slp
CONFIGURE_ARGS += --enable-wrappers
CONFIGURE_ARGS += --enable-backends=mod
CONFIGURE_ARGS += --enable-overlays=mod
CONFIGURE_ARGS += --enable-spasswd
CONFIGURE_ARGS +CONFIGURE_ARGS += --enable-mdb=mod

# Legacy backends
CONFIGURE_ARGS += --enable-bdb=mod
CONFIGURE_ARGS += --enable-hdb=mod+= --with-cyrus-sasl

# Is the absence of this arg causing https://www.opencsw.org/mantis/view.php?id=4468 ?
CONFIGURE_ARGS += --enable-dynamic

# Disable MySQL Cluster
CONFIGURE_ARGS += --disable-ndb

# This libnet is meant to be provided for BeOS only, the libnet.so picked up from OpenCSW
# is completely unrelated. Disable the linkage until this is fixed:
#   http://www.openldap.org/its/index.cgi?findid=7071
CONFIGURE_ARGS += ac_cv_lib_net_main=no
CONFIGURE_ARGS += ac_cv_lib_net_socket=no

# We have Perl only for 32 bit:
#   <http://opencsw.org/mantis/view.php?id=4484>
CONFIGURE_ARGS_32 += --enable-perl=mod
CONFIGURE_ARGS_64 += --enable-perl=no

CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MEMORYMODEL))

# The testsuite take# s a couple of hosbin dir missing in Common PKG?
CHECKPKG_OVERRIDES_CSWopenldap += missing-dependency|CSWapache24|or|CSWbonnie++|or|CSWleafnode|or|CSWlighttpd|or|CSWlogrotate|or|CSWproftpd|or|CSWsysstat|or|CSWzabbix-agent|or|CSWzabbix-server hours
SKIPTEST ?= 1

# Perl backend is built, although it has been told not+= -s ,.*/opt/csw/libexec/sparcv9/openldap/back_perl.*,,
EXTRA_PAX_ARGS += -s ,.*/opt/csw/libexec/amd64/openldap/back_perl.*,,

# Relocate 32 bit slapd to default isa subdir for 32/64 selector
EXTRA_PAX_ARGS += -s ,/opt/csw/libexec/slapd,/opt/csw/libexec/$(ISA_DEFAULT)/slapdpenldap/back_perl.*,,

# These are the config templates. As we have preserveconf which takes
# care of this we exclude them in the package.
EXTRA_MERGE_EXCLUDE_FILES = .*\.default

PRESERVECONF  = /etc/opt/csw/openldap/ldap.conf
PRESERVECONF += /etc/opt/csw/openldap/slapd.conf

INITSMF = /etc/opt/csw/init.d/cswopenldap

include gar/cateallpost-merge-modulated:
	ginstall -D $(WORKDIR)/cswopenldap \
		$(PKGROOT)/etc/opt/csw/init.d/cswopenldap
	$(foreach F,$(EXTRA_DOCS),ginstall --mode=644 -D $(WORKDIR)/$F $(PKGROOT)$(doginstall -D $(WORKDIR)/slapd $(PKGROOT)$(libexecdir)/slapddocdir)/$(NAME)/$F;)
	@# Enable BDB backend so OpenLDAP can start
	perl -pi -e 's/#\s*(modulepath)/$$1/; s/#\s*(moduleload\s*back_bdb.la)/$$1/' $(PKGROOT)$(sysconfdir).CSW
	@$(MAKECOOKIE)
