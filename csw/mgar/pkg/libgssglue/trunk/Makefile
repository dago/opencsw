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
PKGFILES_CSWlibgssglue0 += $(sysconfdir)/.*

# We must link against the kerberos libraries although they are not directly pulled in or it will not work
RUNTIME_DEP_PKGS_CSWlibgssglue0 += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibgssglue0 += CSWlibkrb5support0
RUNTIME_DEP_PKGS_CSWlibgssglue0 += CSWlibgssapi-krb5-2
CHECKPKG_OVERRIDES_CSWlibgssglue0 += soname-unused

# These are really comments
CHECKPKG_OVERRIDES_CSWlibgssglue0 += file-with-bad-content|/usr/local|root/etc/opt/csw/gssapi_mech.conf.CSW
CHECKPKG_OVERRIDES_CSWlibgssglue0 += file-with-bad-content|/usr/local|root/etc/opt/csw/64/gssapi_mech.conf.CSW

PACKAGES += CSWlibgssglue-dev
SPKG_DESC_CSWlibgssglue-dev = Development files for libgssglue.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibgssglue-dev += CSWlibgssglue0

REINPLACEMENTS += mech
REINPLACE_MATCH_mech = /etc/mech.conf
REINPLACE_WITH_mech = $(abspath $(sysconfdir)/$(MM_LIBDIR))/gssapi_mech.conf
REINPLACE_FILES_mech += src/g_initialize.c

PRESERVECONF += $(sysconfdir)/gssapi_mech.conf
PRESERVECONF += $(sysconfdir)/64/gssapi_mech.conf

REINPLACEMENTS += krb5
REINPLACE_MATCH_krb5 = /usr/lib/libgssapi_krb5.so
REINPLACE_WITH_krb5 = $(libdir)/libgssapi_krb5.so.2
REINPLACE_FILES_krb5 += doc/gssapi_mech.conf

EXTRA_CPPFLAGS += -DUSE_SOLARIS_SHARED_LIBRARIES=1

# We must link against the kerberos libraries although they are not directly pulled in or it will not work
LINKER_IGNORE =
EXTRA_LINKER_FLAGS += -lkrb5 -lkrb5support -lgssapi_krb5

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

#DEVEL_EXECUTABLES += $(sysconfdir)/.*
#EXTRA_MERGE_SCRIPTS_isa-extra += merge-copy-config-only

include gar/category.mk

post-install:
	ginstall -D -m 0644 $(WORKSRC)/doc/gssapi_mech.conf $(DESTDIR)$(sysconfdir)/$(MM_LIBDIR)/gssapi_mech.conf
	$(MAKECOOKIE)
