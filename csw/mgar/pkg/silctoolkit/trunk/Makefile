NAME = silc-toolkit
VERSION = 1.1.10

DESCRIPTION = S

DESCRIPTION = secure internet live conferencing toolkit
define BLURB
  SILC Project develops the Secure Internet Live Conferencing protocol, which provides secure conferencing services. 
endef

MASTER_SITES = http://silcnet.org/download/toolkit/so+= $(DISTNAME).tar.bz2
PATCHFILES += function.patch

VENDOR_URL = http://silcnet.org/software/download/toolkit/

PACKAGES += CSWlibsilc1-1-2
SPKG_DESC_CSWlibsilc1-1-2 = Secure internet live conferencing toolkit, libsilc-1.1.so.2
# This is the same as Debian:
#   http://packages.debian.org/sid/m68k/libsilc-1.1-2/filelist
PKGFILES_CSWlibsilc1-1-2 += $(call pkgfiles_lib,libsilc-1.1.so.2)
PKGFILES_CSWlibsilc1-1-2 += $(call pkgfiles_lib,libsilcclient-1.1.so.2)
PKGFILES_CSWlibsilc1-1-2 += $(call baseisadirs,$(libdir)/silc,.*)

OBSOLETED_BY_CSWlibsilc1-1-2 += CSWsilctoolkit

# This is because of the modules in lib/silc/*.so
CHECKPKG_OVERRIDES_CSWlibsilc1-1-2 += soname-not-part-of-filename

# Just a comment
CHECKPKG_OVERRIDES_CSWlibsilc-dev += discouraged-path-in-pkgmap|/opt/csw/share/doc/silc-toolkit/README.CVS

PACKAGES += CSWlibsilc-dev
SPKG_DESC_CSWlibsilc-dev = Development files for libsilc-1.1.so.2
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibsilc-dev += CSWlibsilc1-1-2

# False positives
CHECKPKG_OVERRIDES_CSWlibsilc-dev += shared-lib-package-contains-so-symlink
CHECKPKG_OVERRIDES_CSWlibsilc-dev += shared-lib-pkgname-mismatch

BUILD64 = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-simdir=$(libdir)/silc

include gar/category.mk
