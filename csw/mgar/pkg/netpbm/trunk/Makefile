NAME = netpbm
VERSION = 10.35.80
CATEGORIES = utils

DESCRIPTION = Netpbm is a toolkit for manipulation of graphic images
define BLURB
  Netpbm is a toolkit for manipulation of graphic images, 
  including conversion of images between a variety of different formats.
endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES += $(DISTNAME).tgz
DISTFILES += Makefile.config

EXPANDVARS += Makefile.config

PATCHFILES += 0001-Reorder-includes-so-that-local-includes-come-before-.patch
PATCHFILES += 0002-Remove-unused-external-references-causing-link-error.patch
PATCHFILES += 0003-Remove-extra-conversion-in-function-call-causing-err.patch
PATCHFILES += 0004-Move-opt-csw-include-to-the-end.patch

VENDOR_URL = http://netpbm.sourceforge.net/

LICENSE = doc/GPL_LICENSE.txt

PACKAGES += CSWnetpbm
SPKG_DESC_CSWnetpbm = A toolkit for manipulation of graphic images
RUNTIME_DEP_PKGS_CSWnetpbm += CSWjpeg
RUNTIME_DEP_PKGS_CSWnetpbm += CSWtiff
RUNTIME_DEP_PKGS_CSWnetpbm += CSWpng
RUNTIME_DEP_PKGS_CSWnetpbm += CSWiconv
RUNTIME_DEP_PKGS_CSWnetpbm += CSWzlib
RUNTIME_DEP_PKGS_CSWnetpbm += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWnetpbm += CSWlibnetpbm10

PACKAGES += CSWlibnetpbm10
SPKG_DESC_CSWlibnetpbm10 = Library for manipulation of graphic images, libnetpbm.so.10
PKGFILES_CSWlibnetpbm10 = $(call pkgfiles_lib,libnetpbm.so.10)

PACKAGES += CSWlibnetpbm-dev
SPKG_DESC_CSWlibnetpbm-dev = Development files for libnetpbm.so.10
PKGFILES_CSWlibnetpbm-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibnetpbm-dev += CSWlibnetpbm10

CONFIGURE_SCRIPTS = custom

EXTRA_CFLAGS += -D__inline=

INSTALL_OVERRIDE_VARS += PKGMANDIR
INSTALL_ARGS = package pkgdir=$(DESTDIR)$(prefix)
INSTALL_OVERRIDE_VAR_PKGMANDIR = share/man

# Package has no testsuite
TEST_SCRIPTS =

EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/README
EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/pkginfo
EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/VERSION
EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/config_template
EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/man/.*
EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/link/.*

EXTRA_PAX_ARGS = -s ",$(prefix)/misc,$(sharedstatedir)/netpbm,"

include gar/category.mk

configure-custom:
	cp $(WORKDIR)/Makefile.config $(WORKSRC)
	perl -pi \
		-e 's,(#define\s+RGB_DB1\s+).*,$$1"/opt/csw/share/netpbm/rgb.txt",;' \
		-e 's,(#define\s+RGB_DB2\s+).*,$$1"/usr/openwin/lib/X11/rgb.txt",;' \
		-e 's,(#define\s+RGB_DB3\s+).*,$$1"/usr/openwin/lib/rgb.txt",;' \
		$(WORKSRC)/pm_config.in.h
	@$(MAKECOOKIE)

pre-install-modulated:
	mkdir -p $(DESTDIR)/opt
