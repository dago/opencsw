# $Id$

NAME = openldap
VERSION = 2.4.31
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
DISTFILES += cswopenldap openldap.xml

EXPANDVARS = cswopenldap
EXPANDVARS += CSWoldap.postinstall

PATCHFILES += patch-oldap-2.4.16-ntlm.diff
PATCHFILES += patch-libtool-64bit.diff
DISTFILES += patch-oldap-2.4.16-ntlm.diff

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
RUNTIME_DEP_PKGS_CSWopenldap += CSWbdb48
RUNTIME_DEP_PKGS_CSWopenldap += CSWlibicudata48
RUNTIME_DEP_PKGS_CSWopenldap += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWopenldap += CSWliblber2-4-3
RUNTIME_DEP_PKGS_CSWopenldap += CSWlibldap-r2-4-3
RUNTIME_DEP_PKGS_CSWopenldap += CSWlibltdl7
# We do not want that dependency.
# RUNTIME_DEP_PKGS_CSWopenldap += CSWlibnet
# RUNTIME_DEP_PKGS_CSWopenldap += CSWlibnet1
RUNTIME_DEP_PKGS_CSWopenldap += CSWlibodbc2
RUNTIME_DEP_PKGS_CSWopenldap += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWopenldap += CSWlibslp1
RUNTIME_DEP_PKGS_CSWopenldap += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWopenldap += CSWlibwrap1
RUNTIME_DEP_PKGS_CSWopenldap += CSWperl

# Evaluate later
CHECKPKG_OVERRIDES_CSWopenldap += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/slapd.8

PACKAGES += CSWopenldap-client
SPKG_DESC_CSWopenldap-client = OpenLDAP client executables
PKGFILES_CSWopenldap-client += $(bindir)/.*
PKGFILES_CSWopenldap-client += $(mandir)/man1/.*
RUNTIME_DEP_PKGS_CSWopenldap-client += CSWliblber2-4-3
RUNTIME_DEP_PKGS_CSWopenldap-client += CSWlibldap2-4-3
RUNTIME_DEP_PKGS_CSWopenldap-client += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWopenldap-client += CSWlibssl1-0-0

PACKAGES += CSWopenldap-dev
SPKG_DESC_CSWopenldap-dev = OpenLDAP development files for libldap-2.4.so.3, libldap_r-2.4.so.3 and liblber-2.4.so.3
PKGFILES_CSWopenldap-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWopenldap-dev += $(mandir)/man3/.*
RUNTIME_DEP_PKGS_CSWopenldap-dev += CSWliblber2-4-3
RUNTIME_DEP_PKGS_CSWopenldap-dev += CSWlibldap-r2-4-3
RUNTIME_DEP_PKGS_CSWopenldap-dev += CSWlibldap2-4-3

PACKAGES += CSWliblber2-4-3
SPKG_DESC_CSWliblber2-4-3 = OpenLDAP ASN.1 BER library, liblber-2.4.so.3
PKGFILES_CSWliblber2-4-3 += $(call pkgfiles_lib,liblber-2.4.so.3)
RUNTIME_DEP_PKGS_CSWlibldap2-4-3 += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWlibldap2-4-3 += CSWlibssl1-0-0

PACKAGES += CSWlibldap2-4-3
SPKG_DESC_CSWlibldap2-4-3 = OpenLDAP LDAP library, libldap-2.4.so.3
PKGFILES_CSWlibldap2-4-3 += $(call pkgfiles_lib,libldap-2.4.so.3)
PKGFILES_CSWlibldap2-4-3 += $(sysconfdir)/ldap.conf
PKGFILES_CSWlibldap2-4-3 += $(mandir)/man5/ldap.conf.5
RUNTIME_DEP_PKGS_CSWlibldap2-4-3 += CSWliblber2-4-3

# Evaluate later
CHECKPKG_OVERRIDES_CSWlibldap2-4-3 += file-with-bad-content|/usr/local|root/opt/csw/share/man/man5/ldap.conf.5

PACKAGES += CSWlibldap-r2-4-3
SPKG_DESC_CSWlibldap-r2-4-3 = OpenLDAP reentrant LDAP library, libldap_r-2.4.so.3
PKGFILES_CSWlibldap-r2-4-3 += $(call pkgfiles_lib,libldap_r-2.4.so.3)
RUNTIME_DEP_PKGS_CSWlibldap-r2-4-3 += CSWliblber2-4-3
RUNTIME_DEP_PKGS_CSWlibldap-r2-4-3 += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWlibldap-r2-4-3 += CSWlibssl1-0-0

FOREIGN_PACKAGES += CSWliblber2-3-0

FOREIGN_PACKAGES += CSWlibldap2-3-0

FOREIGN_PACKAGES += CSWlibldap-r2-3-0

EXTRA_DOCS = README.CSW $(PATCHFILES) openldaprc

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
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

NODIRPATHS = --docdir

BUILD64 = 1

# This takes some more work, the sbin/ files should be linked to libexec but the linklevel is not deep enough
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
CONFIGURE_ARGS += --with-cyrus-sasl

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

# The testsuite takes a couple of hours
SKIPTEST ?= 1

# Perl backend is built, although it has been told not to.
EXTRA_PAX_ARGS = -s ,.*/opt/csw/libexec/sparcv9/openldap/back_perl.*,,
EXTRA_PAX_ARGS = -s ,.*/opt/csw/libexec/amd64/openldap/back_perl.*,,

# These are the config templates. As we have preserveconf which takes
# care of this we exclude them in the package.
EXTRA_MERGE_EXCLUDE_FILES = .*\.default

PRESERVECONF  = /etc/opt/csw/openldap/ldap.conf
PRESERVECONF += /etc/opt/csw/openldap/slapd.conf

INITSMF = /etc/opt/csw/init.d/cswopenldap

include gar/category.mk

CFLAGS := $(filter-out -I%,$(CFLAGS))
DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))

post-merge-modulated:
	ginstall -D $(WORKDIR)/cswopenldap \
		$(PKGROOT)/etc/opt/csw/init.d/cswopenldap
	$(foreach F,$(EXTRA_DOCS),ginstall --mode=644 -D $(WORKDIR)/$F $(PKGROOT)$(docdir)/$(NAME)/$F;)
	@# Enable BDB backend so OpenLDAP can start
	perl -pi -e 's/#\s*(modulepath)/$$1/; s/#\s*(moduleload\s*back_bdb.la)/$$1/' $(PKGROOT)$(sysconfdir)/openldap/slapd.conf
	@$(MAKECOOKIE)
