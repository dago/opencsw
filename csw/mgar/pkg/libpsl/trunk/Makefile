# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libpsl
VERSION = 0.6.2
GARTYPE = v2

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = https://github.com/rockdaboot/libpsl/archive/
DISTFILES += $(VERSION).tar.gz

# Use patch until this is fixed:
#   https://github.com/rockdaboot/libpsl/issues/19
#PATCHFILES += 0001-Use-GTK_DOC_USE_LIBTOOL.patch

PATCHFILES += 0001-Solaris-needs-lsocket-lnsl-for-inet_ntop.patch

PACKAGES += CSWlibpsl0
SPKG_DESC_CSWlibpsl0 = Public Suffix List library, libpsl.so.0
# PKGFILES is catchall

PACKAGES += CSWlibpsl-dev
SPKG_DESC_CSWlibpsl-dev = Development files for libpsl.so.0
PKGFILES_CSWlibpsl-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibpsl-dev += $(bindir)/.*
RUNTIME_DEP_PKGS_CSWlibpsl-dev += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSWlibpsl-dev += CSWlibpsl0

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)

# This is needed for sha1sum
BUILD_ENV_PATH = /opt/csw/gnu:$(PATH)

include gar/category.mk

post-patch:
	cd $(WORKSRC) &&  ./autogen.sh
	@$(MAKECOOKIE)

post-install:
	@# Remove directory until this is fixed:
	@#   https://github.com/rockdaboot/libpsl/issues/21
	rmdir $(DESTDIR)/libpsl
	@$(MAKECOOKIE)
