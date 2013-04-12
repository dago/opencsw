# $Id$
NAME = libicu
VERSION = 4.2.1
CATEGORIES = lib

DESCRIPTION = International Components for Unicode
define BLURB
endef

_V-4.2.1 = 4_2_1
filename = icu4c-$(_V-$(1))-src.tgz

MASTER_SITES = $(addsuffix /,$(addprefix http://download.icu-project.org/files/icu4c/,$(VERSION)))
SOURCEFILES = $(call filename,$(VERSION))
DISTFILES  = $(SOURCEFILES)

# icu-config is broken with ECHO_N/ECHO_C detection:
#   http://bugs.icu-project.org/trac/ticket/7768
PATCHFILES = 0001-Add-workaround-for-echo-n.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:_\d+)*)-src.tgz

PACKAGES += CSWlibicu42
CATALOGNAME_CSWlibicu42 = libicu42
SPKG_DESC_CSWlibicu42 = International Components for Unicode, libicu*.so.42

# These are ok. As they are all used and bundled together they are also
# released together in one soname-specific package.
CHECKPKG_OVERRIDES_CSWlibicu42 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libicudata.so.42.1|soname=libicudata.so.42|pkgname=CSWlibicu42|expected=CSWlibicudata42
CHECKPKG_OVERRIDES_CSWlibicu42 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libicui18n.so.42.1|soname=libicui18n.so.42|pkgname=CSWlibicu42|expected=CSWlibicui18n42
CHECKPKG_OVERRIDES_CSWlibicu42 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libicuio.so.42.1|soname=libicuio.so.42|pkgname=CSWlibicu42|expected=CSWlibicuio42
CHECKPKG_OVERRIDES_CSWlibicu42 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libicule.so.42.1|soname=libicule.so.42|pkgname=CSWlibicu42|expected=CSWlibicule42
CHECKPKG_OVERRIDES_CSWlibicu42 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libiculx.so.42.1|soname=libiculx.so.42|pkgname=CSWlibicu42|expected=CSWlibiculx42
CHECKPKG_OVERRIDES_CSWlibicu42 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libicutu.so.42.1|soname=libicutu.so.42|pkgname=CSWlibicu42|expected=CSWlibicutu42
CHECKPKG_OVERRIDES_CSWlibicu42 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libicuuc.so.42.1|soname=libicuuc.so.42|pkgname=CSWlibicu42|expected=CSWlibicuuc42

# The collisions will be there until CSWlibicu has also been updated.
# This will happen at the same time as the CSWlibicu42 release.
CHECKPKG_OVERRIDES_CSWlibicu42 += file-collision

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

CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibicu42 = $(call baseisadirs,$(libdir),libicu.*\.so\.42(\.\d+)*)

include gar/category.mk
