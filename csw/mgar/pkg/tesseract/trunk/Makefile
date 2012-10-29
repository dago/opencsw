# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tesseract
VERSION = 3.02.02
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = An OCR engine

GOOGLE_PROJECT = tesseract-ocr
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz
#DISTFILES  = $(DISTNAME)-dam.tar.gz

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://code.google.com/p/tesseract-ocr/

BUILD_DEP_PKGS += CSWliblept-dev

PACKAGES += CSWlibtesseract3
SPKG_DESC_CSWlibtesseract3 = Tesseract OCR engine library, libtesseract.so.3
PKGFILES_CSWlibtesseract3 += $(call pkgfiles_lib,libtesseract.so.3)
RUNTIME_DEP_PKGS_CSWlibtesseract3 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtesseract3 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibtesseract3 += CSWliblept3

PACKAGES += CSWlibtesseract-dev
SPKG_DESC_CSWlibtesseract-dev = Development files for libtesseract.so.3
PKGFILES_CSWlibtesseract-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibtesseract-dev += CSWlibtesseract3

PACKAGES += CSWtesseract
SPKG_DESC_CSWtesseract = Tesseract OCR engine
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibtesseract += CSWlibtesseract3
RUNTIME_DEP_PKGS_CSWtesseract += CSWlibtesseract3
RUNTIME_DEP_PKGS_CSWtesseract += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWtesseract += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWtesseract += CSWliblept3

GARCOMPILER = GCC4

BUILD64 = 1
ISAEXEC = 1

EXTRA_CONFIGURE_EXPORTS += LIBLEPT_HEADERSDIR
CONFIGURE_ENV_LIBLEPT_HEADERSDIR = $(includedir)

CONFIGURE_ARGS = $(DIRPATHS)

# The tarball does not contain the languages
#INSTALL_ARGS += install-langs

include gar/category.mk

post-extract-modulated:
	@# Yes, the tarball must be bootstrapped
	@#   http://code.google.com/p/tesseract-ocr/issues/detail?id=756
	-cd $(WORKSRC) && ./autogen.sh
	@$(MAKECOOKIE)
