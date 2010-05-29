GARNAME = gnuplot
GARVERSION = 4.4.0
CATEGORIES = utils

DESCRIPTION = The Gnuplot Plotting Utility
define BLURB
	The Gnuplot Plotting Utility.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

include gar/category.mk
