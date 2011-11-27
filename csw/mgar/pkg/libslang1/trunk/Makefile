# $Id$

NAME = slang
VERSION = 1.4.9
CATEGORIES = lib

DESCRIPTION = Library primarily to provide an alternative to libcurses
define BLURB
endef

MASTER_SITES = ftp://space.mit.edu/pub/davis/slang/v$(shell echo $(VERSION) | perl -ne 'print /(\d+\.\d+)/')
DISTFILES += $(DISTNAME).tar.bz2

VENDOR_URL = http://www.s-lang.org/

PACKAGES += CSWlibslang1
SPKG_DESC_CSWlibslang = Library primarily to provide an alternative to libcurses, libslang.so.1
PKGFILES_CSWlibslang1 += $(call pkgfiles_lib,libslang.so.1)

# These are locations of fallback terminfo/ directories, /opt/csw/share/terminfo comes first
# due to our reinplacement
CHECKPKG_OVERRIDES_CSWlibslang1 += file-with-bad-content|/usr/local|root/opt/csw/lib/libslang.so.1.4.9
CHECKPKG_OVERRIDES_CSWlibslang1 += file-with-bad-content|/usr/share|root/opt/csw/lib/libslang.so.1.4.9

# Setting -L$(libdir) before the newly built lib confuses function
# definitions if the installed lib is older than the newly built one.
LINKER_FLAGS =

# No testsuite available
TEST_TARGET = 

# Make sure to find just the right terminfo files
REINPLACEMENTS += usr_share_terminfo
REINPLACE_MATCH_usr_share_terminfo = /usr/share/terminfo
REINPLACE_WITH_usr_share_terminfo = /opt/csw/share/terminfo
REINPLACE_FILES_usr_share_terminfo = src/sltermin.c

INSTALL_ARGS = install-elf install-links

BUILD_ARGS = elf

BUILD_OVERRIDE_VARS = ELF_CFLAGS
BUILD_OVERRIDE_VAR_ELF_CFLAGS = -K pic $(CFLAGS)

include gar/category.mk
