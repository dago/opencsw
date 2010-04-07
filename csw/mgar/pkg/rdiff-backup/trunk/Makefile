GARNAME = rdiff-backup
GARVERSION = 1.2.8
CATEGORIES = python

DESCRIPTION = Remote incremental backup
define BLURB
  Remote incremental backup
endef

MASTER_SITES = http://savannah.nongnu.org/download/rdiff-backup/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWrdiffbackup
CATALOGNAME = rdiffbackup

RUNTIME_DEP_PKGS_CSWrdiffbackup += CSWlibrsync

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SKIPTEST = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
