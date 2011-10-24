# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = wdiff
VERSION = 1.0.1
CATEGORIES = utils

DESCRIPTION = A front end to diff for comparing files on a word per word basis
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# Use patch until this is fixed:
#   http://lists.gnu.org/archive/html/wdiff-bugs/2011-09/msg00006.html
PATCHFILES += wdiff-1.0.1-testsuite.patch

VENDOR_URL = http://www.gnu.org/software/wdiff/

RUNTIME_DEP_PKGS_CSWwdiff += CSWlibintl8

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk
