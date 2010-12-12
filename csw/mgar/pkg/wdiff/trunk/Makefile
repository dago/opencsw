# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = wdiff
VERSION = 0.6.2
CATEGORIES = utils

DESCRIPTION = A front end to diff for comparing files on a word per word basis
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.gnu.org/software/wdiff/

DEP_PKGS = CSWggettextrt

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk
