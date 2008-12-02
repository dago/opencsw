GARNAME = mktemp
GARVERSION = 1.5
CATEGORIES = utils

DESCRIPTION = A small program to allow safe temporary file creation from shell scripts.
define BLURB
    The mktemp utility takes the given filename template and overwrites a
    portion of it to create a unique filename.	 The template may be any file-
    name with some number of `Xs' appended to it, for example
    /tmp/tfile.XXXXXXXXXX.
endef

MASTER_SITES = ftp://ftp.mktemp.org/pub/$(GARNAME)/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += $(call admfiles,CSWmktemp)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES = makefile-destdir.patch

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
