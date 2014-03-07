NAME = silc-toolkit
VERSION = 1.1.10

DESCRIPTION = S

DESCRIPTION = secure internet live conferencing toolkit
define BLURB
  SILC Project develops the Secure Internet Live Conferencing protocol, which provides secure conferencing s###
# client.h collides with Samba and has to be somehow dealt with
### services. 
endef

MASTER_SITES = http://silcnet.org/download/toolkit/so+= $(DISTNAME).tar.bz2
PATCHFILES += function.patch
PATCHFILES += 0002-linking-lacks-LDFLAGS.patch

PATCHFILES += 0001-xargs-splits-into-multiple-invocations-make-sure-to-.patch

VENDOR_URL = http://silcnet.org/software/download/toolkit/

# This is the same as what Debian used to do:
# http://packages.debian.org/squeeze/libsilc-1.1-2
# http://packages.debian.org/squeeze/libsilcclient-1.1-3
# It seems they now have dropped SILC altogether
PACKAGES += CSWlibsilc1-1-2
SPKG_DESC_CSWlibsilc1-1-2 = Secure internet live conferencing toolkit, libsilc-1.1.so.2
PKGFILES_CSWlibsilc1-1-2 += $(call pkgfiles_lib,libsilc-1.1.so.2)
PKGFILES_CSWlibsilc1-1-2 += $(call baseisadirs,$(libdir),silc/.*)
RUNTIME_DEP_PKGS_CSWlibsilc1-1-2 += CSWlibiconv2

OBSOLETED_BY_CSWlibsilc1-1-2 += CSWsilctoolkit

PACKAGES += CSWlibsilcclient1-1-3
SPKG_DESC_CSWlibsilcclient1-1-3 += Secure internet live conferencing toolkit, libsilcclient-1.1.so.3
PKGFILES_CSWlibsilcclient1-1-3 += $(call pkgfiles_lib,libsilcclient-1.1.so.3)

OBSOLETED_BY_CSWlibsilcclient1-1-3 += CSWsilctoolkit

# This is because of the modules in lib/silc/*.so
CHECKPKG_OVERRIDES_CSWlibsilc1-1-2 += soname-not-part-of-filename

# Just a comment
CHECKPKG_OVERRIDES_CSWlibsilc-dev += discouraged-path-in-pkgmap|/opt/csw/share/doc/silc-toolkit/README.CVS

PACKAGES += CSWlibsilc-dev
SPKG_DESC_CSWlibsilc-dev = Development files for libsilc-1.1.so.2
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibsilc-dev += CSWlibsilc1-1-2
RUNTIME_DEP_PKGS_CSWlibsilc-dev += CSWlibsilcclient1-1-3

BUILD64 = 1

# These are at least needed for libsilc.so
EXTRA_LINKER_FLAGS += -lsocket -lnsl -liconv

# Avoid a collision between its client.h and Samba's
includedir = $(prefix)/include/silc

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-simdir=$(libdir)/silc

include gar/category.mk
