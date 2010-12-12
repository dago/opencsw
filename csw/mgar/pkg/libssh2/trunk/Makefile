NAME = libssh2
VERSION = 1.2.7
CATEGORIES = lib

DESCRIPTION = A Library Implementing the SSH2 Protocol
define BLURB
	libssh2 is a library implementing the SSH2 protocol as defined by 
	Internet Drafts: SECSH-TRANS, SECSH-USERAUTH, SECSH-CONNECTION, 
	SECSH-ARCH, SECSH-FILEXFER, SECSH-DHGEX, SECSH-NUMBERS, and 
	SECSH-PUBLICKEY. 
endef

MASTER_SITES = http://www.libssh2.org/download/
SPKG_SOURCEURL = http://www.libssh2.org
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_CSWlibssh2  = CSWosslrt CSWzlib
RUNTIME_DEP_PKGS_CSWlibssh2devel = CSWlibssh2
BUILD_DEP_PKGS = CSWossldevel CSWzlib

PACKAGES = CSWlibssh2 CSWlibssh2devel

CATALOGNAME_CSWlibssh2 = libssh2
CATALOGNAME_CSWlibssh2devel = libssh2_devel

SPKG_DESC_CSWlibssh2 = $(DESCRIPTION)
SPKG_DESC_CSWlibssh2devel = Developer files for libssh2

BUILD64 = 1
NOISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libz
CONFIGURE_ARGS += --with-openssl=/opt/csw

TEST_TARGET = check

# Disable for now until this is fixed:
#   http://libssh2.stuge.se/ticket/170
SKIPTEST ?= 1

PKGFILES_CSWlibssh2devel = $(PKGFILES_DEVEL)

CHECKPKG_OVERRIDES_CSWlibssh2devel += surplus-dependency|CSWlibssh2

include gar/category.mk
