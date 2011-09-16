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

RUNTIME_DEP_PKGS  = CSWggettextrt
RUNTIME_DEP_PKGS += CSWiconv
RUNTIME_DEP_PKGS += CSWlibicu
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWreadline
RUNTIME_DEP_PKGS += CSWsunmath 

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check-recommended

include gar/category.mk
