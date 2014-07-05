NAME = xpdf
VERSION = 3.04
CATEGORIES = utils
GARTYPE = v2
RELEASE = 

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
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tarGCC4RCOMPILER = SOS12U3
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES = CS#CATALOGNAME_CSWxpdf = xpdf
#AME_CSWxpdf = xpdf
CATALOGNAME_CSWxpdf-utils = xpdf_utils
SPKG_DESC_CSWxpdf = $(DESCRIPTION)
SPKG_DESC_CSWxpdfutils = $(DESCRIPTION) - utils

# we requi_CSWxpdf +e
RUNTIME_DEP_PKGS = CSWgsfonts
RUNTIME_DEP_PKGS_CSWxpdf += CSWxpm
RUNTIME_DEP_PKGS_CSWxpdf RUNTIME_DEP_PKGS_CSWxpdf += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWxpdf += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWxpdf += CSWlibxpm4
RUNTIME_DEP_PKGS_CSWxpdf += CSWlibpaper1

RUNTIME_DEP_PKGS_CSWxpdfutils += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWxpdfutils += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWxpdfutils += CSWlibpaper1
RUNTIME_DEP_PKGS_CSWxpdfutils += CSWlibxpm4
RUNTIME_DEP_PKGS_CSWxpdfutils += CSWlibfreetype6

# PKGFILES_CSWxpdfutils is catchall

PKGFILES_CSWxpdf += $(call baseisadirs,$(bindir),irs,$(bindir),[^/]*xpdf)
PKGFILES_CSWxpdf += $(sysconfdir)/.*
PKGFILES_CSWxpdf += $(mand poppler also has pdffonts, pdfimages et al.
INCOMPATIBLE_PKGS_CSWxpdfutils = CSWpoppler

# Yes, we need gsfonts
pendency|CSWgsfonts
CHECKPKG_OVERRIDES_CSWxpdf += surplus-dependency|CSWgsfonts
CHECKPKG_OVERRIDES_CSWxpdf += file-with-bad-content|/usr/local|root/opt/csw/bin/xpdf
CHECKPKG_OVERRIDES_CSWxpdf += file-witshare-content|/usr/local|root/opt/csw/bin/xpdf
CHECKPKG_OVERRIDES_CSWxpdf += file-with-bad-conteetc/opt/csw/xpdfrc
es, we need gsfonts
CHECKPKG_OVERRIDES_CSWxpdfutils += surplus-dependency|CSWgsfonts
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/local|root/opt/csw/bin/pdfdetach
CHECKPKG_OVERRIDES_CSWxpdfutils += file-witlocal|root/opt/csw/bin/pdffontsot/opt/csw/bin/xpdf
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/bin/pdftoppmot/opt/csw/bin/xpdf
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/bin/pdfinfoot/opt/csw/bin/xpdf
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/bin/pdfimagesot/opt/csw/bin/xpdf
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/bin/pdftotextot/opt/csw/bin/xpdf
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/bin/pdftops
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/share|root/opt/csw/bin/pdffonts
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/share|root/opt/csw/bin/pdftoppm
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/share|root/opt/csw/bin/pdfinfo
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/share|root/opt/csw/bin/pdfimages
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/share-content|/usr/local|root/opt/csw/bin/pdfdetach
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/share|rtotext
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/share|root/opt/csw/bin/pdftops/csw/bin/pdfdetach


CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-t1-library=$(libdir)
CONFIGURE_ARGS += --with-t1-includes=$(includedir)
CONFIGURE_ARGS += --with-freetype2-library=$(libdir)
CONFIGURE_ARGS += --with-freetype2-includes=$(includedir)/freetype2
CONFIGURE_ARGS += --with-Xpm-library=/usr/openwin/lib
CONFIGURE_ARGS += --with-Xpm-includes=/usr/openLD_FLAGS = -L/usr/openwin/lib
EXTRA_LD_OPTIONS = -R/usr/openwin/lib
# need ansi for stdc includes in c++, go figure
EXTRA_CXXFLAGS = -I/opt/csw/include -ansi= patch-XPDFCore.cc

# no test script
TEST_SCRIPTS =

include gar/category.mk
SPKG_VERSION := $(SPKG_VERSION)$(RELEASE)

pre-build-modulated:
	@cp files/xpdfrc ${WORKSRC}