NAME = libassuan
VERSION = 2.0.1
CATEGORIES = lib

DESCRIPTION = IPC library used by some GnuPG related software
define BLURB
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/libassuan/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# Use this patch unless this is fixed:
#   https://bugs.g10code.com/gnupg/issue1282
PATCHFILES = 0001-Add-INADDR_NONE-for-Solaris.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://www.gnupg.org/download/#libassuan

BUILD_DEP_PKGS = CSWgpgerr CSWpth
RUNTIME_DEP_PKGS = CSWgpgerr

BUILD64 = 1
NOISAEXEC = 1

# EXTRA_LDFLAGS = -lrt -lsocket -lnsl

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# Disable tests until this is fixed:
#   https://bugs.g10code.com/gnupg/msg3633
SKIPTEST ?= 1

include gar/category.mk
