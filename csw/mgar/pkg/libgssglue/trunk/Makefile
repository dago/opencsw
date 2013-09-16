# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libgssglue
VERSION = 0.4
GARTYPE = v2

DESCRIPTION = Brief description

MASTER_SITES = http://www.citi.umich.edu/projects/nfsv4/linux/libgssglue/
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-Fix-gcc-issues.patch

VENDOR_URL = http://www.citi.umich.edu/projects/nfsv4/linux/libgssglue/

PACKAGES += CSWlibgssglue0
SPKG_DESC_CSWlibgssglue0 = A GSSAPI interface
PKGFILES_CSWlibgssglue0 += $(call pkgfiles_lib,libgssglue.so.0)

# We must link against the kerberos libraries although they are not directly pulled in or it will not work
RUNTIME_DEP_PKGS_CSWlibgssglue0 += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibgssglue0 += CSWlibkrb5support0
RUNTIME_DEP_PKGS_CSWlibgssglue0 += CSWlibgssapi-krb5-2
CHECKPKG_OVERRIDES_CSWlibgssglue0 += soname-unused

PACKAGES += CSWlibgssglue-dev
SPKG_DESC_CSWlibgssglue-dev = Development files for libgssglue.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibgssglue-dev += CSWlibgssglue0

EXTRA_CPPFLAGS += -DUSE_SOLARIS_SHARED_LIBRARIES=1

# We must link against the kerberos libraries although they are not directly pulled in or it will not work
LINKER_IGNORE =
EXTRA_LINKER_FLAGS += -lkrb5 -lkrb5support -lgssapi_krb5

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

