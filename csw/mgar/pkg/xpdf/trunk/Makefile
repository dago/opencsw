NAME = xpdf
VERSION = 3.03
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
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER = SOS12U3
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES = CSWxpdf CSWxpdfutils
CATALOGNAME_CSWxpdf = xpdf
CATALOGNAME_CSWxpdf-utils = xpdf_utils
SPKG_DESC_CSWxpdf = $(DESCRIPTION)
SPKG_DESC_CSWxpdfutils = $(DESCRIPTION) - utils

# we require
RUNTIME_DEP_PKGS = CSWgsfonts
RUNTIME_DEP_PKGS_CSWxpdf += CSWxpm
RUNTIME_DEP_PKGS_CSWxpdf += CSWlibfreetype6


# poppler also has pdffonts, pdfimages et al.
# INCOMPATIBLE_PKGS_CSWxpdfutils = CSWpoppler

PKGFILES_CSWxpdf += $(call baseisadirs,$(bindir),[^/]*xpdf)
PKGFILES_CSWxpdf += $(sysconfdir)/.*
PKGFILES_CSWxpdf += $(mandir)/man.*/xpdf.*

#content moved to package CSWpoppler
EXTRA_MERGE_EXCLUDE_FILES += $(call baseisadirs,$(bindir),[^/]*pdffonts)
EXTRA_MERGE_EXCLUDE_FILES += $(call baseisadirs,$(bindir),[^/]*pdfimages)
EXTRA_MERGE_EXCLUDE_FILES += $(call baseisadirs,$(bindir),[^/]*pdfinfo)
EXTRA_MERGE_EXCLUDE_FILES += $(call baseisadirs,$(bindir),[^/]*pdftoabw)
EXTRA_MERGE_EXCLUDE_FILES += $(call baseisadirs,$(bindir),[^/]*pdftohtml)
EXTRA_MERGE_EXCLUDE_FILES += $(call baseisadirs,$(bindir),[^/]*pdftoppm)
EXTRA_MERGE_EXCLUDE_FILES += $(call baseisadirs,$(bindir),[^/]*pdftops)
EXTRA_MERGE_EXCLUDE_FILES += $(call baseisadirs,$(bindir),[^/]*pdftotext)
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/.*/pdffonts.*
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/.*/pdfimages.1
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/.*/pdfinfo.1
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/.*/pdftoabw.1
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/.*/pdftohtml.1
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/.*/pdftoppm.1
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/.*/pdftops.1
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/.*/pdftotext.1

# Yes, we need gsfonts
CHECKPKG_OVERRIDES_CSWxpdfutils += surplus-dependency|CSWgsfonts
CHECKPKG_OVERRIDES_CSWxpdf += surplus-dependency|CSWgsfonts
CHECKPKG_OVERRIDES_CSWxpdf += file-with-bad-content|/usr/local|root/opt/csw/bin/xpdf
CHECKPKG_OVERRIDES_CSWxpdf += file-with-bad-content|/usr/local|root/opt/csw/share/man/man5/xpdfrc.5
CHECKPKG_OVERRIDES_CSWxpdf += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/xpdf.1
CHECKPKG_OVERRIDES_CSWxpdf += file-with-bad-content|/usr/local|root/etc/opt/csw/xpdfrc
CHECKPKG_OVERRIDES_CSWxpdf += file-with-bad-content|/usr/share|root/opt/csw/bin/xpdf
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/pdfdetach.1
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/local|root/opt/csw/bin/pdfdetach
CHECKPKG_OVERRIDES_CSWxpdfutils += file-with-bad-content|/usr/share|root/opt/csw/bin/pdfdetach


CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-t1-library=$(libdir)
CONFIGURE_ARGS += --with-t1-includes=$(includedir)
CONFIGURE_ARGS += --with-freetype2-library=$(libdir)
CONFIGURE_ARGS += --with-freetype2-includes=$(includedir)/freetype2
CONFIGURE_ARGS += --with-Xpm-library=/usr/openwin/lib
CONFIGURE_ARGS += --with-Xpm-includes=/usr/openwin/include

EXTRA_SOS_LD_FLAGS = -L/usr/openwin/lib
EXTRA_SOS_LD_OPTIONS = -R/usr/openwin/lib
EXTRA_CXXFLAGS = -I/opt/csw/include
EXTRA_LINKER_FLAGS = -norunpath

# apply patches
# PATCHFILES  = xpdf-3.02pl1.patch
# PATCHFILES += xpdf-3.02pl2.patch
# PATCHFILES += xpdf-3.02pl3.patch
# PATCHFILES += xpdf-3.02pl4.patch
# PATCHFILES += patch-GString.cc
# PATCHFILES += patch-XPDFCore.cc

# no test script
TEST_SCRIPTS =

include gar/category.mk
SPKG_VERSION := $(SPKG_VERSION)$(RELEASE)

pre-build-modulated:
	@cp files/xpdfrc ${WORKSRC}/doc/sample-xpdfrc
