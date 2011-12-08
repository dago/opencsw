# $Id$

NAME = gamin
VERSION = 0.1.10
CATEGORIES = server

DESCRIPTION = GNOME replacement for FAM which watches for file alterations
define BLURB
endef

MASTER_SITES += http://people.gnome.org/~veillard/gamin/sources/
DISTFILES  = $(DISTNAME).tar.gz

# Solaris Nevada FEN support from
#   https://bugzilla.gnome.org/show_bug.cgi?id=491319
# The patch has been reformatted
# PATCHFILES += 0001-Patch-from-bugid-107675.patch

# As taken from
#   http://src.opensolaris.org/source/xref/jds/spec-files/trunk/base-specs/gamin.spec

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

MASTER_SITES += http://src.opensolaris.org/source/raw/jds/spec-files/branches/opensolaris-2010-03/patches/
PATCHDIRLEVEL = 0
PATCHFILES += gamin-01-all.diff
PATCHFILES += gamin-02-gamin.diff

PATCHFILES += 0003-Enable-64-bit-builds.patch

VENDOR_URL = http://people.gnome.org/~veillard/gamin/

PACKAGES += CSWlibfam0
SPKG_DESC_CSWlibfam0 = FAM compatibility library from GAMIN, libfam.so.0
PKGFILES_CSWlibfam0 += $(call pkgfiles_lib,libfam.so.0)
OBSOLETED_BY_CSWlibfam0 += CSWfam

PACKAGES += CSWlibgamin1-0
SPKG_DESC_CSWlibgamin1-0 = GNOME replacement for FAM library, libgamin-1.so.0
PKGFILES_CSWlibgamin1-0 += $(call pkgfiles_lib,libgamin-1.so.0)

PACKAGES += CSWlibgamin-dev
SPKG_DESC_CSWlibgamin-dev = Development files for libgamin-1.so.0 and legacy compat libfam.so.0
PKGFILES_CSWlibgamin-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgamin-dev += CSWlibgamin1-0
# That is a legacy-only library, no need to pull it in unless for legacy CSWfam
CHECKPKG_OVERRIDES_CSWlibgamin-dev += missing-dependency|CSWlibfam0

PACKAGES += CSWpy-gamin
SPKG_DESC_CSWpy-gamin = Python bindings for GAMIN file alteration monitor
PKGFILES_CSWpy-gamin += $(libdir)/site-packages/.*
RUNTIME_DEP_PKGS_CSWpy-gamin += CSWpython
RUNTIME_DEP_PKGS_CSWpy-gamin += CSWlibgamin1-0

PACKAGES += CSWgamin
SPKG_DESC_CSWgamin = GAMIN file alteration monitor daemon (compatible to FAM)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgamin += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgamin += CSWglib2
OBSOLETED_BY_CSWgamin += CSWfam

# For socket, recvmsg, connect
EXTRA_LINKER_FLAGS = -lsocket -lnsl

BUILD64 = 1

# This is not passed to configure, although it is defined (but wrong) in configure.in
EXTRA_CONFIGURE_EXPORTS += ENV_CFLAGS
CONFIGURE_ENV_ENV_CFLAGS = $(CFLAGS)

# No 64 bit Python yet
CONFIGURE_ARGS-64 += --without-python

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

PYCOMPILE = 1
EXTRA_MERGE_EXCLUDE_FILES += .*\.pyo .*\.pyc
EXTRA_PAX_ARGS += -s ,$(libdir)/python2.6/site-packages,$(libdir)/site-packages,

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && libtoolize --copy --force
	cd $(WORKSRC) && aclocal
	cd $(WORKSRC) && autoconf --force
	cd $(WORKSRC) && automake -a -c -f
	@$(MAKECOOKIE)
