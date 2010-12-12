NAME = R
VERSION = 2.10.1
CATEGORIES = apps

DESCRIPTION = A language and environment for statistical computing and graphics
define BLURB
endef

MASTER_SITES = http://stat.ethz.ch/CRAN/src/base/R-2/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWr
CATALOGNAME = r

RUNTIME_DEP_PKGS = CSWggettextrt CSWiconv CSWlibicu CSWperl CSWreadline CSWsunmath 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.r-project.org/

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check-recommended

include gar/category.mk
