# $Id$
NAME = libicu
VERSION = 4.6.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = International Components for Unicode
define BLURB
endef

MASTER_SITES = http://download.icu-project.org/files/icu4c/$(VERSION)/
SOURCEFILES = icu4c-$(subst .,_,$(VERSION))-src.tgz
DISTFILES = $(SOURCEFILES)

# icu-config is broken with ECHO_N/ECHO_C detection:
#   http://bugs.icu-project.org/trac/ticket/7768
#PATCHFILES = 0001-Add-workaround-for-echo-n.patch

PACKAGES += CSWlibicu46
CATALOGNAME_CSWlibicu46 = libicu46
SPKG_DESC_CSWlibicu46 = International Components for Unicode, libicu*.so.46
PKGFILES_CSWlibicu46 = $(call baseisadirs,$(libdir),libicu.*\.so\.46(\.\d+)*)
# These are ok. As they are all used and bundled together they are also
# released together in one soname-specific package.
CHECKPKG_OVERRIDES_CSWlibicu46 += shared-lib-pkgname-mismatch

PACKAGES += CSWlibicu-devel
CATALOGNAME_CSWlibicu-devel = libicu_devel
SPKG_DESC_CSWlibicu-devel = Development Files for libicu
# This package is PKGFILES catchall
RUNTIME_DEP_PKGS_CSWlibicu-devel = CSWlibicu46

# This is just a comment for --prefix
CHECKPKG_OVERRIDES_CSWlibicu-devel += file-with-bad-content|/usr/local|root/opt/csw/bin/icu-config
CHECKPKG_OVERRIDES_CSWlibicu-devel += file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv9/icu-config

PACKAGES += CSWlibicu
CATALOGNAME_CSWlibicu = libicu
SPKG_DESC_CSWlibicu = $(DESCRIPTION)
PKGFILES_CSWlibicu = NOFILES
ARCHALL_CSWlibicu = 1
# There are still legacy packages depending on CSWlibicu and expecting .so.42 in it.
# Also depend on legacy soname-package until all these have been resolved.
RUNTIME_DEP_PKGS_CSWlibicu += CSWlibicu42
CHECKPKG_OVERRIDES_CSWlibicu += surplus-dependency|CSWlibicu42
# This package is generated in a branch and cannot be found in this build.
CHECKPKG_OVERRIDES_CSWlibicu += unidentified-dependency|CSWlibicu42

# The collisions will be there until CSWlibicu has also been updated.
# This will happen at the same time as the CSWlibicu42 release.
CHECKPKG_OVERRIDES_CSWlibicu46 += file-collision
CHECKPKG_OVERRIDES_CSWlibicu-devel += file-collision
CHECKPKG_OVERRIDES_CSWlibicu += file-collision

LICENSE = license.html

VENDOR_URL = http://icu-project.org/

DISTNAME = icu
WORKSRC = $(WORKDIR)/$(DISTNAME)/source

# Using -I/opt/csw/include here puts it before the include of the newly built
# software which breaks definitions, so make sure it is empty.
CPPFLAGS = 

# libCrun is needed for all libs, libCstd for libicui18n.so only
# Not having these does not cause errors during build of libicu, but the
# packages using the libs will bail out as they assume the libs are self-contained.
LINKER_FLAGS = -lCrun -lCstd

EXTRA_CXXFLAGS = -norunpath

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

include gar/category.mk
