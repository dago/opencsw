NAME = rdiff-backup
VERSION = 1.2.8
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Remote incremental backup
define BLURB
  Remote incremental backup
endef

MASTER_SITES = http://savannah.nongnu.org/download/rdiff-backup/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWrdiffbackup
CATALOGNAME = rdiffbackup

RUNTIME_DEP_PKGS_CSWrdiffbackup += CSWlibrsync

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SKIPTEST = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
