# Only builds on Solaris 10

NAME = R
VERSION = 2.13.1
CATEGORIES = apps

DESCRIPTION = A language and environment for statistical computing and graphics
define BLURB
endef

MASTER_SITES = http://stat.ethz.ch/CRAN/src/base/R-2/
DISTFILES    = $(NAME)-$(VERSION).tar.gz

PACKAGES       = CSWr
CATALOGNAME    = r
SPKG_SOURCEURL = http://www.r-project.org/

RUNTIME_DEP_PKGS_CSWr += CSWsunmath 
RUNTIME_DEP_PKGS_CSWr += CSWjpeg
RUNTIME_DEP_PKGS_CSWr += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWr += CSWtcl
RUNTIME_DEP_PKGS_CSWr += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWr += CSWlibz1
RUNTIME_DEP_PKGS_CSWr += CSWlibintl8
RUNTIME_DEP_PKGS_CSWr += CSWtiff
RUNTIME_DEP_PKGS_CSWr += CSWliblzma5
RUNTIME_DEP_PKGS_CSWr += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWr += CSWlibicu46
RUNTIME_DEP_PKGS_CSWr += CSWtk
RUNTIME_DEP_PKGS_CSWr += CSWpango
RUNTIME_DEP_PKGS_CSWr += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWr += CSWss12f95rt
RUNTIME_DEP_PKGS_CSWr += CSWglib2

# Temporary overrides
CHECKPKG_OVERRIDES_CSWr += file-with-bad-content
CHECKPKG_OVERRIDES_CSWr += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWr += soname-not-found

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check-recommended

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

include gar/category.mk
