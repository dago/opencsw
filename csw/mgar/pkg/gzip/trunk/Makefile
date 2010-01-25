GARNAME = gzip
GARVERSION = 1.4
CATEGORIES = utils

DESCRIPTION = GNU zip
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = 0001-Force-ggrep-as-Solaris-grep-doesn-t-understand-the-f.patch

# From TODO:
# - Add a block size (-b) option to improve error recovery in case of
#   failure of a complete sector. Each block could be extracted
#   independently, but this reduces the compression ratio.
# 
# For one possible approach to this, please see:
#   http://www.samba.org/netfilter/diary/gzip.rsync.patch
#
# Update patch from
#  http://cvs.fedoraproject.org/viewvc/rpms/gzip/F-12/gzip-1.3.9-rsync.patch?revision=1.2&content-type=text%2Fplain&view=co
PATCHFILES += gzip-1.3.9-rsync.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWggrep

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk
