GARNAME = libassuan
GARVERSION = 1.0.5
CATEGORIES = lib

DESCRIPTION = IPC library used by some GnuPG related software
define BLURB
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/libassuan/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWlibassuan,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.bz2

PREREQUISITE_PKGS = CSWcommon
PREREQUISITE_PKGS += CSWpth

BUILD64 = 1
NO_ISAEXEC = 1

EXTRA_LDFLAGS = -lrt -lsocket -lnsl

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-pth-prefix=/opt/csw

# We must include static libs here as libassuan contains *only*
# static libs
MERGE_EXCLUDE_STATICLIBS =

TEST_TARGET = check

include gar/category.mk
