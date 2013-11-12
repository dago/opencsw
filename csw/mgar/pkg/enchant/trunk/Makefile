NAME = enchant
VERSION = 1.6.0
GARTYPE = v2
GARCOMPILER = GNU apps
GARTYPE = v2

DESCRIPTION = A wrapper library for various spell checking engines
define BLURB
endef

MASTER_SITES =  http://www.abisource.com/downloads/$(NAME)/$(VERSION)/
DISTFILES  = $(NAME)-$(VEFILES += changelog.CSW
DISTFILES += CSWlibenchant1.postmsg
SPKG_SOURCEURL = http://www.abisource.com/projects/enchant/

PACKAGES = CSWenchant
SPKG_DESC_CSWenchant += $(DESCRIPTION), meta package
ARCHALL_CSWenchant = 1
RUNTIME_DEP_PKGS_CSWenchant += CSWenchant-bin
RUNTIME_DEP_PKGS_CSWenchant += CSWlibenchant1
RUNTIME_DEP_PKGS_CSWenchant += CSWlibenchant-aspell
RUNTIME_DEP_PKGS_CSWenchant += CSWlibenchant-ispell
RUNTIME_DEP_PKGS_CSWenchant += CSWlibenchant-myspell
CHECKPKG_OVERRIDES_CSWenchant += surplus-dependency|CSWenchant-bin
CHECKPKG_OVERRIDES_CSWenchant += surplus-dependency|CSWlibenchant-aspell
CHECKPKG_OVERRIDES_CSWenchant += surplus-dependency|CSWlibenchant-ispell
CHECKPKG_OVERRIDES_CSWenchant += surplus-dependency|CSWlibenchant-myspell
CHECKPKG_OVERRIDES_CSWenchant += surplus-dependency|CSWlibenchant1

PACKAGES +=  CSWenchant-bin
SPKG_DESC_CSWenchant-bin += $(DESCRIPTION), runtime package
PKGFILES_CSWenchant-bin  = $(bindir).*
PKGFILES_CSWenchant-bin += $(mandir)/man1.*
PKGFILES_CSWenchant-bin += $(docdir)/enchant_bin.*
RUNTIME_DEP_PKGS_CSWenchant-bin += CSWlibenchant1
RUNTIME_DEP_PKGS_CSWenchant-bin += CSWlibglib2-0-0
# This is due to `ld -z ignore` issue on sparc, once resolved, deps can be removed
RUNTIME_DEP_PKGS_CSWenchant-bin += CSWlibintl8
CHECKPKG_OVERRIDES_CSWenchant-bin += surplus-dependency|CSWlibintl8

PACKAGES += CSWlibenchant1
SPKG_DESC_CSWlibenchant1 = $(DESCRIPTION), libenchant.so.1
PKGFILES_CSWlibenchant1 += $(call pkgfiles_lib,libenchant.so.1)
PKGFILES_CSWlibenchant1 += $(sharedstatedir)/enchant.*
PKGFILES_CSWlibenchant1 += $(docdir)/libenchant1.*
POSTMSG_CSWlibenchant1 = /opt/csw/share/doc/libenchant1/CSWenchant.postmsg
RUNTIME_DEP_PKGS_CSWlibenchant1 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibenchant1 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibenchant1 += CSWlibgcc-s1
# This is due to `ld -z ignore` issue on sparc, once resolved, deps can be removed
RUNTIME_DEP_PKGS_CSWlibenchant1 += CSWlibintl8
CHECKPKG_OVERRIDES_CSWlibenchant1 += surplus-dependency|CSWlibintl8

PACKAGES += CSWlibenchant-aspell
SPKG_DESC_CSWlibenchant-aspell = $(DESCRIPTION), aspell backend
PKGFILES_CSWlibenchant-aspell  = .*enchant/libenchant_aspell.so
PKGFILES_CSWlibenchant-aspell += $(docdir)/libenchant_aspell.*
# Apparently, there is no aspell 64bit
CHECKPKG_OVERRIDES_CSWlibenchant-aspell += 64-bit-binaries-missing
RUNTIME_DEP_PKGS_CSWlibenchant-aspell += CSWlibaspell15
RUNTIME_DEP_PKGS_CSWlibenchant-aspell += CSWlibenchant1
RUNTIME_DEP_PKGS_CSWlibenchant-aspell += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibenchant-aspell += CSWlibgcc-s1
# This is due to `ld -z ignore` issue on sparc, once resolved, deps can be removed
RUNTIME_DEP_PKGS_CSWlibenchant-aspell += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibenchant-aspell += CSWlibgmodule2-0-0
CHECKPKG_OVERRIDES_CSWlibenchant-aspell += surplus-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWlibenchant-aspell += surplus-dependency|CSWlibgmodule2-0-0

PACKAGES += CSWlibenchant-ispell
SPKG_DESC_CSWlibenchant-ispell = $(DESCRIPTION), ispell backend
PKGFILES_CSWlibenchant-ispell  = .*enchant/libenchant_ispell.so
PKGFILES_CSWlibenchant-ispell += $(docdir)/libenchant_ispell.*
RUNTIME_DEP_PKGS_CSWlibenchant-ispell += CSWlibenchant1
RUNTIME_DEP_PKGS_CSWlibenchant-ispell += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibenchant-ispell += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibenchant-ispell += CSWlibstdc++6
# This is due to `ld -z ignore` issue on sparc, once resolved, deps can be removed
RUNTIME_DEP_PKGS_CSWlibenchant-ispell += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibenchant-ispell += CSWlibgmodule2-0-0
CHECKPKG_OVERRIDES_CSWlibenchant-ispell += surplus-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWlibenchant-ispell += surplus-dependency|CSWlibgmodule2-0-0

PACKAGES += CSWlibenchant-myspell
SPKG_DESC_CSWlibenchant-myspell = $(DESCRIPTION), myspell backend
PKGFILES_CSWlibenchant-myspell  = .*enchant/libenchant_myspell.so
PKGFILES_CSWlibenchant-myspell += $(docdir)/libenchant_myspell.*
RUNTIME_DEP_PKGS_CSWlibenchant-myspell += CSWlibenchant1
RUNTIME_DEP_PKGS_CSWlibenchant-myspell += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibenchant-myspell += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibenchant-myspell += CSWlibstdc++6
# This is due to `ld -z ignore` issue on sparc, once resolved, deps can be removed
RUNTIME_DEP_PKGS_CSWlibenchant-myspell += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibenchant-myspell += CSWlibgmodule2-0-0
CHECKPKG_OVERRIDES_CSWlibenchant-myspell += surplus-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWlibenchant-myspell += surplus-dependency|CSWlibgmodule2-0-0

PACKAGES += CSWlibenchant-dev
SPKG_DESC_CSWlibenchant-dev += $(DESCRIPTION) - developer package
PKGFILES_CSWlibenchant-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibenchant-dev += $(docdir)/libenchant_dev.*
RUNTIME_DEP_PKGS_CSWlibenchant-dev += CSWlibenchant1

BUILD_DEP_PKGS += CSWlibdbus-glib-dev
BUILD_DEP_PKGS += CSWlibglib2-dev

LICENSE = COPYING.LIB

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64#BUILD64_LIBS_ONLY = 1

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no

include gar/category.mk

PATH := /op
post-merge:
	[ -d $(PKGROOT)$(docdir)/libenchant1/ ] || mkdir -p $(PKGROOT)$(docdir)/libenchant1/
	ginstall $(FILEDIR)/CSWlibenchant1.postmsg $(PKGROOT)$(docdir)/libenchant1/
	@$(MAKECOOKIE)
