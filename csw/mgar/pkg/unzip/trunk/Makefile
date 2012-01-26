NAME = unzip
VERSION = 6.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Info-Zip UnZip extraction utility for archives compressed in .zip format
define BLURB
endef

SF_PROJ = infozip
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = unzip60
DISTFILES  = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.info-zip.org/

LICENSE = LICENSE

CONFIGURE_SCRIPTS = $(WORKSRC)/unix/configure
# CONFIGURE_ARGS = $(DIRPATHS)

BUILD_SCRIPTS     = $(WORKSRC)/unix/Makefile
BUILD_ARGS = sunos

TEST_SCRIPTS      = $(WORKSRC)/unix/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/unix/Makefile

include gar/category.mk
