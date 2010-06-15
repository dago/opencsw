# $Id$
GARNAME = x3270
GARVERSION = 3.3.10ga5
CATEGORIES = apps

DESCRIPTION = An IBM 3270 terminal emulator
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = suite3270-$(GARVERSION)-src.tgz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)-src.tar.gz

VENDOR_URL = http://x3270.sourceforge.net/

BASEREL = 3.3
# wc3270 = windows console, we don't need that.
# wpr3270 = MinGW
# ws3270 = MinGW
# SUBSYSTEMS = c3270 pr3287 s3270 tcl3270 wc3270 wpr3287 ws3270 x3270
SUBSYSTEMS = c3270 pr3287 s3270 tcl3270 x3270

WORKSRC = $(WORKDIR)
CONFIGURE_SCRIPTS = $(foreach S,$(SUBSYSTEMS),$(WORKDIR)/$S-$(BASEREL)/configure)
CONFIGURE_ARGS = $(DIRPATHS)

BUILD_SCRIPTS = $(foreach S,$(SUBSYSTEMS),$(WORKDIR)/$S-$(BASEREL)/Makefile)
TEST_SCRIPTS = 
INSTALL_SCRIPTS = $(BUILD_SCRIPTS)



include gar/category.mk
