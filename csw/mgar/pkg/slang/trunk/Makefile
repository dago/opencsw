# $Id$

NAME = slang
VERSION = 2.2.4
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Library primarily to provide an alternative to libcurses
define BLURB
endef

MASTER_SITES = ftp://space.mit.edu/pub/davis/slang/v$(shell echo $V | perl -ne 'print /(\d+\.\d+)/')
DISTFILES = $(DISTNAME).tar.bz2

VENDOR_URL = http://www.s-lang.org/

BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWlibonig-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_DEP_PKGS += CSWlibiconv-dev

FOREIGN_PACKAGES += CSWlibslang1
OBSOLETED_BY_CSWlibslang1 += CSWslang

PACKAGES += CSWlibslang2
SPKG_DESC_CSWlibslang2 = Library primarily to provide an alternative to libcurses, libslang.so.2
PKGFILES_CSWlibslang2 += $(call pkgfiles_lib,libslang.so.2)
PKGFILES_CSWlibslang2 += $(call baseisadirs,$(libdir),slang/.*)
RUNTIME_DEP_PKGS_CSWlibslang2 += CSWlibpcre0
RUNTIME_DEP_PKGS_CSWlibslang2 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibslang2 += CSWlibonig2
RUNTIME_DEP_PKGS_CSWlibslang2 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibslang2 += CSWlibz1
OBSOLETED_BY_CSWlibslang2 += CSWslang
# These are locations of fallback terminfo/ directories, /opt/csw/share/terminfo comes first
# due to our reinplacement
CHECKPKG_OVERRIDES_CSWlibslang2 += file-with-bad-content|/usr/local|root/opt/csw/lib/libslang.so.2.2.4
CHECKPKG_OVERRIDES_CSWlibslang2 += file-with-bad-content|/usr/local|root/opt/csw/lib/sparcv9/libslang.so.2.2.4
CHECKPKG_OVERRIDES_CSWlibslang2 += file-with-bad-content|/usr/local|root/opt/csw/lib/amd64/libslang.so.2.2.4
CHECKPKG_OVERRIDES_CSWlibslang2 += file-with-bad-content|/usr/share|root/opt/csw/lib/libslang.so.2.2.4
CHECKPKG_OVERRIDES_CSWlibslang2 += file-with-bad-content|/usr/share|root/opt/csw/lib/sparcv9/libslang.so.2.2.4
CHECKPKG_OVERRIDES_CSWlibslang2 += file-with-bad-content|/usr/share|root/opt/csw/lib/amd64/libslang.so.2.2.4

PACKAGES += CSWlibslang-dev
SPKG_DESC_CSWlibslang-dev = Development for libslang.so.2
PKGFILES_CSWlibslang-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibslang-dev += $(docdir)/slang/.*
RUNTIME_DEP_PKGS_CSWlibslang-dev += CSWlibslang2
# These are docs only
CHECKPKG_OVERRIDES_CSWlibslang-dev += file-with-bad-content

PACKAGES += CSWslsh
SPKG_DESC_CSWslsh = SLANG shell, a shell using slang for terminal control
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWslsh += CSWlibslang2

# These are examples on√ly
CHECKPKG_OVERRIDES_CSWslsh += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/slsh.1
CHECKPKG_OVERRIDES_CSWslsh += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/slsh.1

# This is funny, the slsh.rc is placed in the correct location, but the search path
# is hardwired to something different
REINPLACEMENTS += slshrc
REINPLACE_MATCH_slshrc = define DEFAULT_CONF_PATH.*
REINPLACE_WITH_slshrc = define DEFAULT_CONF_PATH "/etc/opt/csw:/opt/csw/etc"
REINPLACE_FILES_slshrc = slsh/slsh.c

REINPLACEMENTS += slshrc_man
REINPLACE_MATCH_slshrc_man = \$$\(prefix\)/etc
REINPLACE_WITH_slshrc_man = /etc/opt/csw/:/opt/csw/etc/
REINPLACE_FILES_slshrc_man = slsh/doc/man/slsh.1

# Replace all the other default pathes with nothing
REINPLACEMENTS += slshrc_man_skip
REINPLACE_MATCH_slshrc_man_skip = \\fI(/usr/local/etc/|/usr/local/etc/slsh/|/etc/|/etc/slsh/)\\fR
REINPLACE_WITH_slshrc_man_skip = 
REINPLACE_FILES_slshrc_man_skip = slsh/doc/man/slsh.1

# Setting -L$(libdir) before the newly built lib confuses function
# definitions if the installed lib is older than the newly built one.
LINKER_FLAGS =

BUILD64_LIBS_ONLY = 1

include gar/category.mk
