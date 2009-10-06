GARNAME = libssh2
GARVERSION = 1.2.1
CATEGORIES = lib

DESCRIPTION = A Library Implementing the SSH2 Protocol.
define BLURB
	libssh2 is a library implementing the SSH2 protocol as defined by 
	Internet Drafts: SECSH-TRANS, SECSH-USERAUTH, SECSH-CONNECTION, 
	SECSH-ARCH, SECSH-FILEXFER, SECSH-DHGEX, SECSH-NUMBERS, and 
	SECSH-PUBLICKEY. 
endef

MASTER_SITES = http://www.libssh2.org/download/
SPKG_SOURCEURL = http://www.libssh2.org
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWlibssh2
CATALOGNAME_CSWlibssh2 = libssh2
SPKG_DESC_CSWlibssh2 = $(DESCRIPTION)

REQUIRED_PKGS_CSWlibssh2  = CSWosslrt CSWzlib


# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
NO_ISAEXEC = 1
TEST_SCRIPTS =
TEST_TARGET = check

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libz
CONFIGURE_ARGS += --with-openssl=/opt/csw

include gar/category.mk
