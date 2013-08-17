NAME = netpbm
VERSION = 10.63.00
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Netpbm is a toolkit for manipulation of graphic images
define BLURB
  Netpbm is a toolkit for manipulation of graphic images, 
  including conversion of images between a variety of differeSF_PROJECT = netpbm
MASTER_SITES  = svn-http://svn.code.sf.net/p/$(NAME)/code/release_number/
DISTFILES += config.mk
DISTFILES += $(VERSION)
NOCHECKSUM += $(VERSION)
DISTNAME = $(VERSION)

GARCOMPILER = GCC4

EXPANDVARS += config.mk

PATCHFILES += 0005_missing_stdlib.h.patch
PATCHFILES += 0006-memcpy.patch
PATCHFILES += 0007_stdout_already_used.patch

VENDOR_URL = http://netpbm.sourceforge.net/

LICENSE = doc/GPL_LICENSE.txt

BUILD_DEP_PKGS += CSWx11xprotodoc/GPL_LICENSE.txt

PACKAGES += CSWnetpbm
SPKG_DESC_CSWnetpbm = A toolkit for manipulation of graphic images
RUNTIME_DEP_PKGS_CSWnetpbm += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWn5tpbm += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWnetpbm += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWnetpbm += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWnetpbm += CSWlibz1
RUNTIME_DEP_PKGS_CSWnetpbm += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWnetpbm += CSWlibnetpbm10

PACKAGES += CSWlibnetpbm10
SPKG_DESC_CSWlibnetpbm10 = Library for manipulation of graphic images, libnetpbm.so.10
PKGFILES_CSWlibnetpbm10 = $(call pkgfiles_lib,libnetpbm.so.10)

PACKAGES += CSWlibnetpbm-dev
SPKG_DESC_CSWlibnetpbm-dev = Development files for libnetpbm.so.10
PKGFILES_CSWlibnetpbm-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibnetpbm-dev += CSWlibnetpbm10

CONFIGUREGS += -D__inline=

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

includPATH := /opt/csw/gnu:$(PATH):/opt/csw/gcc4/bin

configure-custom:
	cp $(WORKDIR)/config.mkIR)/Makefile.config $(WORKSRC)
	perl -pi \
		-e 's,(#define\s+RGB_DB1\s+).*,$$1"/opt/csw/share/netpbm/rgb.txt",;' \
		-e 's,(#define\s+RGB_DB2\s+).*,$$1"/usr/openwin/lib/X11/rgb.txt",;' \
		-e 's,(#define\s+RGB_DB3\s+).*,$$1"/usr/openwin/lib/rgb.txt",;' \
		$(WORKSRC)/pm_config.in.h
	@$(MAKECOOKIE)

pre-install-modulated:
	mkdir -p $(DESTDIR)/opt

post-install-modulated:
	rm -f $(DESTDIR)$(libdir)/libnetpbm.so
	gln -s libnetpbm.so.10 $(DESTDIR)$(li