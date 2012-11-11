# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libupnp
VERSION = 1.6.15
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Portable UPnP SDK
define BLUECTRB
endef

SF_PROJ = pupnp
MASTER_SITES = $(SF_MIRROR)
DISTFILES += $(DISTNAME).tar.bz2

# Add patch from SFE originally to be found at
#   http://pkgbuild.svn.sourceforge.net/svnroot/pkgbuild/spec-files-extra/trunk/patches/libupnp-01-solaris.spec
# PATCHFILES += libupnp-01-solaris.spec

PATCHFILES += 0001-Add-includes-for-Solaris.patch
PATCHFILES += 0002-Use-inttypes.h-if-stdint.h-is-not-available.patch

PACKAGES += CSWmypkg
SPKG_DESC_CSWmypkg = My package
PKGFILES_CSWmypkg += $(call pkgfiles_lib,libabc.so.1)
PKGFILES_CSWmypkg += $(call baseisadirs,$(bindir),myexec)
PKGFILES_CSWmypkg += $(sysconfdir)/myconf

# "VERSION\" | sed " configure
REINPLACEMENTS += gsed
REINPLACE_MATCH_gsed = VERSION\"\ \|\ sed
REINPLACE_WITH_gsed = VERSION\" | gsed
REINPLACE_FILES_gsed += configure


BUILD64_LIBS_ONLY = 1

# From README
EXTRA_CFLAGS += -D__sun

CONFIGURE_ARGS = $(DIRPATHS)

include 