GARNAME = xpdf
GARVERSION = 3.02
CATEGORIES = utils

DESCRIPTION = Open source viewer for Portable Document Format (PDF) files
define BLURB
  Xpdf is an open source viewer for Portable Document Format (PDF) files. 
  (These are also sometimes also called 'Acrobat' files, from the name of 
  Adobe's PDF software.) The Xpdf project also includes a PDF text extractor, 
  PDF-to-PostScript converter, and various other utilities. 
  Xpdf is designed to be small and efficient. It can use Type 1, TrueType, 
  or standard X fonts. 
endef

MASTER_SITES = ftp://ftp.foolabs.com/pub/xpdf/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# we require
REQUIRED_PKGS = CSWftype2 CSWt1lib CSWxpm CSWgsfonts

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-Xpm-library=$(libdir)
CONFIGURE_ARGS += --with-Xpm-includes=$(includedir)
CONFIGURE_ARGS += --with-t1-library=$(libdir)
CONFIGURE_ARGS += --with-t1-includes=$(includedir)
CONFIGURE_ARGS += --with-freetype2-library=$(libdir)
CONFIGURE_ARGS += --with-freetype2-includes=$(includedir)/freetype2

# apply patches
PATCHFILES  = xpdf-3.02pl1.patch
PATCHFILES += xpdf-3.02pl2.patch
PATCHFILES += xpdf-3.02pl3.patch
PATCHFILES += patch-GString.cc
PATCHFILES += patch-XPDFCore.cc

# no test script
TEST_SCRIPTS =

include gar/category.mk

pre-build-modulated:
	@cp files/xpdfrc ${WORKSRC}/doc/sample-xpdfrc
