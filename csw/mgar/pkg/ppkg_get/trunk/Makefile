GARNAME = ppkg_get
GARVERSION = 1.0
CATEGORIES = utils

DESCRIPTION = Perl rewrite of origine pkg-get tools
define BLURB
  ppkg-get is tool to automatically download, install or upgrade
  solaris package from a remote repository, taking care of
  retrieving required dependancies.
  ppkg-get is a perl rewrite of original pkg-get tool written
  by Phillip Brown.
endef

MASTER_SITES = 
DISTFILES = $(call admfiles,CSWppkgget,prototype)
DISTFILES += ppkg-get ppkg-get.conf 
DISTFILES += README.CSW

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS =

include gar/category.mk
