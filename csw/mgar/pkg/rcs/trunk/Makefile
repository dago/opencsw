GARNAME = rcs
GARVERSION = 5.7
CATEGORIES = apps

DESCRIPTION = GNU Revision Control System
define BLURB
endef

MASTER_SITES = http://www.cs.purdue.edu/homes/trinkle/RCS/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.Z

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWdiffutils

man1dir = $(mandir)/man1
man5dir = $(mandir)/man5

DIFF = $(bindir)/gdiff
DIFF3 = $(bindir)/gdiff3

NORUNPATH = 1
CONFIGURE_ARGS = --prefix=$(prefix)
CONFIGURE_ARGS += --with-diffutils

TEST_TARGET =

INSTALL_OVERRIDE_DIRS = prefix man1dir man5dir
BUILD_OVERRIDE_DIRS = DIFF DIFF3

include gar/category.mk
