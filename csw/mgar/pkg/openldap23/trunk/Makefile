# TBD:
# ! currently libldap and libldap_r link against the installed 2.4 which is really bad

NAME = openldap
VERSION = 2.3.43
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
SOURCEFILES  = $(foreach VERSION,$(MODULATIONS_VERSION),$(NAME)-$(VERSION).tgz)
DISTFILES  = $(DISTNAME).tgz

PATCHFILES += patch-libtool-64bit.diff

LICENSE = COPYRIGHT

VENDOR_URL = http://www.openldap.org

PACKAGES += CSWliblber2-3-0
SPKG_DESC_CSWliblber2-3-0 = OpenLDAP library, liblber-2.3.so.0
PKGFILES_CSWliblber2-3-0 += $(call pkgfiles_lib,liblber-2.3.so.0)

PACKAGES += CSWlibldap2-3-0
SPKG_DESC_CSWlibldap2-3-0 = OpenLDAP library, libldap-2.3.so.0
PKGFILES_CSWlibldap2-3-0 += $(call pkgfiles_lib,libldap-2.3.so.0)
RUNTIME_DEP_PKGS_CSWlibldap2-3-0 += CSWliblber2-3-0

PACKAGES += CSWlibldap-r2-3-0
SPKG_DESC_CSWlibldap-r2-3-0 = OpenLDAP library, libldap_r-2.3.so.0
PKGFILES_CSWlibldap-r2-3-0 += $(call pkgfiles_lib,libldap_r-2.3.so.0)
RUNTIME_DEP_PKGS_CSWlibldap-r2-3-0 += CSWliblber2-3-0

# This is old, stick to BerkeleyDB 4.4
EXTRA_LIB = $(prefix)/bdb44/lib 
EXTRA_INC = $(prefix)/bdb44/include

# Not released yet.
# !! OpenLDAP does not use libnet *at all*. This is an artifact from BeOS where libnet
# !! is a completely different library needed for socket operations.
EXTRA_LDFLAGS = -L$(libdir)/libnet-new

# Is this causing this?
#   https://www.opencsw.org/mantis/view.php?id=4555
NOISALIST = 1
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

NODIRPATHS = --docdir

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-crypt
CONFIGURE_ARGS += --enable-lmpasswd
CONFIGURE_ARGS += --enable-modules
CONFIGURE_ARGS += --enable-rlookups
CONFIGURE_ARGS += --enable-slp

# Is the absence of this arg causing https://www.opencsw.org/mantis/view.php?id=4468 ?
CONFIGURE_ARGS += --enable-dynamic

# Disable MySQL Cluster
CONFIGURE_ARGS += --disable-ndb

# Disable Cyrus SASL in 64 bit until the libraries are available
#   <http://opencsw.org/mantis/view.php?id=3749>
CONFIGURE_ARGS_64 += --without-cyrus-sasl

CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MEMORYMODEL))

# Perl backend is built, although it has been told not to.
EXTRA_PAX_ARGS = -s ,.*/opt/csw/libexec/sparcv9/openldap/back_perl.*,,
EXTRA_PAX_ARGS = -s ,.*/opt/csw/libexec/amd64/openldap/back_perl.*,,

TEST_ARGS += MAKEFLAGS=

include gar/category.mk

CFLAGS := $(filter-out -I%,$(CFLAGS))
DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))
