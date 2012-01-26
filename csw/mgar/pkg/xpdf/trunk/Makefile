NAME = xpdf
VERSION = 3.02
CATEGORIES = utils
GARTYPE = v2
RELEASE = p4

DESCRIPTION = Open source viewer for Portable Document Format (PDF) files
define BLURB
  Xpdf is an open source viewer for Portable Document Format (PDF) files. 
  (These are also sometimes also called 'Acrobat' files, from the name of 
  Adobe's PDF software.) The Xpdf project also includes a PDF text extractor, 
  PDF-to-PostScript converter, and various other utilities. 
  Xpdf is designed to be small and efficient. It can use Type 1, TrueType, 
  or standard X fonts. 
endef

VENDOR_URL = http://www.foolabs.com/xpdf
MASTER_SITES = ftp://ftp.foolabs.com/pub/xpdf/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWxpdf CSWxpdfutils
CATALOGNAME_CSWxpdf = xpdf
CATALOGNAME_CSWxpdfutils = xpdf_utils
SPKG_DESC_CSWxpdf = $(DESCRIPTION)
SPKG_DESC_CSWxpdfutils = $(DESCRIPTION) - utils

# we require
RUNTIME_DEP_PKGS = CSWftype2 CSWt1lib CSWgsfonts

# poppler also has pdffonts, pdfimages et al.
INCOMPATIBLE_PKGS_CSWxpdfutils = CSWpoppler

PKGFILES_CSWxpdf += $(call baseisadirs,$(bindir),[^/]*xpdf)
PKGFILES_CSWxpdf += $(sysconfdir)/.*
PKGFILES_CSWxpdf += $(mandir)/man.*/xpdf.*

# Yes, we need gsfonts
CHECKPKG_OVERRIDES_CSWxpdfutils += surplus-dependency|CSWgsfonts
CHECKPKG_OVERRIDES_CSWxpdf += surplus-dependency|CSWgsfonts

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-t1-library=$(libdir)
CONFIGURE_ARGS += --with-t1-includes=$(includedir)
CONFIGURE_ARGS += --with-freetype2-library=$(libdir)
CONFIGURE_ARGS += --with-freetype2-includes=$(includedir)/freetype2
CONFIGURE_ARGS += --with-Xpm-library=/usr/openwin/lib
CONFIGURE_ARGS += --with-Xpm-includes=/usr/openwin/include

EXTRA_SOS_LD_FLAGS = -L/usr/openwin/lib
EXTRA_SOS_LD_OPTIONS = -R/usr/openwin/lib

# apply patches
PATCHFILES  = xpdf-3.02pl1.patch
PATCHFILES += xpdf-3.02pl2.patch
PATCHFILES += xpdf-3.02pl3.patch
PATCHFILES += xpdf-3.02pl4.patch
PATCHFILES += patch-GString.cc
PATCHFILES += patch-XPDFCore.cc

# no test script
TEST_SCRIPTS =

include gar/category.mk
SPKG_VERSION := $(SPKG_VERSION)$(RELEASE)

pre-build-modulated:
	@cp files/xpdfrc ${WORKSRC}/doc/sample-xpdfrc
