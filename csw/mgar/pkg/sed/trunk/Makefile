GARNAME = sed
GARVERSION = 4.0.9
CATEGORIES = utils

DESCRIPTION = GNU Stream Editor
define BLURB
    Sed, the GNU Stream Editor, copies the named files (standard input default) to
    the standard output, edited according to a script of commands.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
