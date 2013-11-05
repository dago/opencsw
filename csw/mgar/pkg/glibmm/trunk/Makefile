NAME = glibmm
VERSION = 2.28.2
GARTYPE = v2

DESCRIPTION = C++ interface to glib2
define BLURB
endef

PATCHFILES += 0001-Fix-disable-tests-1.patch
PATCHFILES += 0003-Disable-Tests-2.patch
PATCHFILES += 0003-Use-etc-hosts-instead-of-etc-fstab-in-test.patch

MASTER_SITES += $(GNOME_MIRROR)
DISTFILES += $(DISTNAME).tar.xz
DISTFILES += changelog.CSW

GARCOMPILER = GNU

PACKAGES = CSWlibgiomm2-4-1
SPKG_DESC_CSWlibgiomm2-4-1 = $(DESCRIPTION), libgiomm-2.4.so.1
PKGFILES_CSWlibgiomm2-4-1  = $(call pkgfiles_lib,libgiomm-2.4.so.1)
RUNTIME_DEP_PKGS_CSWlibgiomm2-4-1 += CSWlibsigc2-0-0
RUNTIME_DEP_PKGS_CSWlibgiomm2-4-1 += CSWlibglibmm2-4-1
RUNTIME_DEP_PKGS_CSWlibgiomm2-4-1 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgiomm2-4-1 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibgiomm2-4-1 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgiomm2-4-1 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgiomm2-4-1 += CSWlibglib2-0-0
CHECKPKG_OVERRIDES_CSWlibgiomm2-4-1 += surplus-dependency|CSWlibgmodule2-0-0
CHECKPKG_OVERRIDES_CSWlibgiomm2-4-1 += surplus-dependency|CSWlibintl8

PACKAGES += CSWlibglibmm2-4-1
SPKG_DESC_CSWlibglibmm2-4-1 = $(DESCRIPTION), libglibmm-2.4.so.1
PKGFILES_CSWlibglibmm2-4-1  = $(call pkgfiles_lib,libglibmm-2.4.so.1)
RUNTIME_DEP_PKGS_CSWlibglibmm2-4-1 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibglibmm2-4-1 += CSWlibsigc2-0-0
RUNTIME_DEP_PKGS_CSWlibglibmm2-4-1 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibglibmm2-4-1 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibglibmm2-4-1 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibglibmm2-4-1 += CSWlibgcc-s1

# Had to shorten package name :/
PACKAGES += CSWlibglibmm-extra-defs2-4-1
SPKG_DESC_CSWlibglibmm-extra-defs2-4-1 = $(DESCRIPTION), libglibmm_generate_extra_defs-2.4.so.1
PKGFILES_CSWlibglibmm-extra-defs2-4-1  = $(call pkgfiles_lib,libglibmm_generate_extra_defs-2.4.so.1)
RUNTIME_DEP_PKGS_CSWlibglibmm-extra-defs2-4-1 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibglibmm-extra-defs2-4-1 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibglibmm-extra-defs2-4-1 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibglibmm-extra-defs2-4-1 += CSWlibglib2-0-0
# Package name would be too long
CHECKPKG_OVERRIDES_CSWlibglibmm-extra-defs2-4-1 += shared-lib-pkgname-mismatch
# Remove once ld -z ignore issue has been resolved on sparc
UNTIME_DEP_PKGS_CSWlibglibmm2-4-1 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgiomm2-4-1 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgiomm2-4-1 += CSWlibgmodule2-0-0

PACKAGES += CSWlibglibmm-dev
SPKG_DESC_CSWlibglibmm-dev = $(DESCRIPTION), development files
PKGFILES_CSWlibglibmm-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibglibmm-dev += .*/lib/(.*/|)giomm-2.4.*
PKGFILES_CSWlibglibmm-dev += .*/lib/(.*/|)glibmm-2.4.*
RUNTIME_DEP_PKGS_CSWlibglibmm-dev  = CSWlibglib2-dev 
RUNTIME_DEP_PKGS_CSWlibglibmm-dev += CSWlibglibmm-extra-defs2-4-1
RUNTIME_DEP_PKGS_CSWlibglibmm-dev += CSWlibgiomm2-4-1
RUNTIME_DEP_PKGS_CSWlibglibmm-dev += CSWlibglibmm2-4-1
RUNTIME_DEP_PKGS_CSWlibglibmm-dev += CSWperl
# Nothing to worry, just in a comment
CHECKPKG_OVERRIDES_CSWlibglibmm-dev += file-with-bad-content|/usr/local|root/opt/csw/include/glibmm-2.4/glibmm/miscutils.h

PACKAGES += CSWglibmm-doc
ARCHALL_CSWglibmm-doc = 1
SPKG_DESC_CSWglibmm-doc = $(DESCRIPTION), documentation
# Catch all


BUILD64_LIBS_ONLY = 1

EXTRA_CONFIGURE_EXPORTS += MAKE
CONFIGURE_ENV_MAKE = gmake

# Some test rely on gthread, but do not pull it in.
EXTRA_LINKER_FLAGS = -lgthread-2.0

include gar/category.mk
