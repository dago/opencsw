NAME = PDF-Reuse-Barcode
VERSION = 0.06
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = LARSLUND

DESCRIPTION = Reuse and mass produce PDF documents
define BLURB
endef

DISTFILES += COPYING

PACKAGES = CSWpm-pdf-reuse-barcode
CATALOGNAME = pm_pdf_reuse_barcode
SPKG_DESC_CSWpm-pdf-reuse-barcode = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-pdf-reuse-barcode = CSWpmpdfreusebarcode
CATALOGNAME_CSWpmpdfreusebarcode = pm_pdfreusebarcode

ARCHALL = 1

BUILD_DEP_PKGS += CSWpm-gd-barcode
BUILD_DEP_PKGS += CSWpm-pdf-reuse
BUILD_DEP_PKGS += CSWpm-barcode-code128

RUNTIME_DEP_PKGS += CSWpm-gd-barcode
RUNTIME_DEP_PKGS += CSWpm-pdf-reuse
RUNTIME_DEP_PKGS += CSWpm-barcode-code128

include gar/category.mk
