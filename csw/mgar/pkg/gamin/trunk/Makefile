# $Id$

NAME = gamin
VERSION = 0.1.10
GARTYPE = v2
GARCOMPILER = SOS12U3 server
GARTYPE = v2

DESCRIPTION = GNOME replacement for FAM which watches for file alterations
define BLURB
endef

MASTER_SITES += http://people.gnome.org/~veillard/gamin/sources/
DISTFILES  =DISTFILES += changelog.CSW= $(DISTNAME).tar.gz

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

PATCHFILES += 0003-Enable-6PATCHFILES += 0004-Adjust-configure.inEnable-64-bit-builds.patch

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
RUNTIME_DEP_PKGS_CSWlibgamin-deRUNTIME_DEP_PKGS_CSWlibgamin-dev +=  missing-dependency|CSWlibfam0

PACKAGES += CSWpy-gamin
SPKG_DESC_CSWpy-gamin = Python bindings for GAMIN file alteration monitor
PKGFILES_CSWpy-gamin += $(libdiCHECKPKG_OVERRIDES_CSWpy-gamin += python-package-missing-py-files
CHECKPKG_OVERRIDES_CSWpy-gamin += python-package-missing-py26-files
CHECKPKG_OVERRIDES_CSWpy-gamin += 64-bit-binaries-missing
CHECKPKG_OVERRIDES_CSWpy-gamin += surplus-dependency|CSWpythonir)/site-packages/.*
RUNTIME_DEP_PKGS_CSWpy-gamin += CSWpython
RUNTIME_DEP_PKGS_CSWpy-gamin += CSWlibgamin1-0

PACKAGES += CSWgamin
SPKG_DESC_CSWgamin = GAMIN file alteration monitor daemon (compatible to FAM)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgaminRUNTIME_DEP_PKGS_CSWgamin += CSWlibintl8
# Currently (2013-11-04) behave differently: sparc seems to ignore -z ignore and 
# x86 does respect it. I have to report this to the list...
CHECKPKG_OVERRIDES_CSWgamin += soname-unused
CHECKPKG_OVERRIDES_CSWgamin += surplus-dependency|CSWlibintl8n += CSWlibglib2-0-0
OBSOLETED_BY_CSWgamin += CSWfam

BUILD_DEP_PKGS  = CSWlibtool
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWautoconf
BUILD_DEP_PKGS += CSWautomake

# For sockeEXTRA_LINKER_FLAGS = -lsocket -lnsl

BUILD64l

BUILD64_LIBS_ONLY = 1

# This is not passed to configure, although it is defined (but wrong) in configure.in
EXTRA_CONFIGURE_EXPORTS += ENV_CFLAGS
CONFIGURE_ENV_ENV# Build chokes on G_CONST_RETURN
# "gam_subscription.h", line 24: syntax error before or at: char
# "gam_subscription.c", line 144: warning: old-style declaration or incorrect type for: G_CONST_RETURN
EXTRA_CPPFLAGS = -DG_CONST_RETURN=const

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

# Build chokes with python enabled for
# 64bit
CONFIGURE_ARGS-64 += --without-pythonARGS-$(MEMORYMODEL))

PYCOMPILE = 1
EXTRA_MERGE_EXCLUDE_FILE .*/python2.6S += .*\.pyo .*\.pyc
EXTRA_PAX_ARGS += -s ,$(libdir)/python2.6/site-packages,$(libdir)/site-packages,
EXTRA_PAX_ARGS += -s ,$(libdir)/python2.4/site-packages,$(libdir)/site-packages,

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && libtoolize --copy --force
	cd $(WORKSRC) && aclocal
	cd $(WORKSRC) && autoconf --force
	cd $(WORKSRC) && automake -a -c