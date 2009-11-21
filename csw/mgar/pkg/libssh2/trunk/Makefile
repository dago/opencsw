GARNAME = libssh2
GARVERSION = 1.2.2
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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS  = CSWosslrt CSWzlib
PREREQUISITE_PKGS = CSWossldevel CSWzlib

BUILD64 = 1
NO_ISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libz
CONFIGURE_ARGS += --with-openssl=/opt/csw

# TEST_SCRIPTS =
TEST_TARGET = check

include gar/category.mk
