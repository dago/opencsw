NAME = libssh2
VERSION = 1.4.2
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A library for impementing the SSH2 protocol
define BLURB
	libssh2 is a library implementing the SSH2 protocol as defined by 
	Internet Drafts: SECSH-TRANS, SECSH-USERAUTH, SECSH-CONNECTION, 
	SECSH-ARCH, SECSH-FILEXFER, SECSH-DHGEX, SECSH-NUMBERS, and 
	SECSH-PUBLICKEY. 
endef

MASTER_SITES = http://www.libssh2.org/download/
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-Force-bash-and-GNU-grep.patch

VENDOR_URL = http://www.libssh2.org

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibz-dev

PACKAGES += CSWlibssh2-1
SPKG_DESC_CSWlibssh2-1 = A library for impementing the SSH2 protocol, libssh2.so.1
PKGFILES_CSWlibssh2-1 += $(call pkgfiles_lib,libssh2.so.1)
RUNTIME_DEP_PKGS_CSWlibssh2-1 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlibssh2-1 += CSWlibz1
OBSOLETED_BY_CSWlibssh2-1 += CSWlibssh2

PACKAGES += CSWlibssh2-dev
SPKG_DESC_CSWlibssh2-dev = Development files for libssh2.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibssh2-dev += CSWlibssh2-1
OBSOLETED_BY_CSWlibssh2-dev += CSWlibssh2devel
CATALOGNAME_CSWlibssh2devel = libssh2_devel_stub

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libz
CONFIGURE_ARGS += --with-openssl=/opt/csw

# Disable for now until this is fixed:
#   http://libssh2.stuge.se/ticket/170
# GARFLAVOR = DBG
# EXTRA_CPPFLAGS = -DLIBSSH2DEBUG
SKIPTEST ?= 1

include gar/category.mk
