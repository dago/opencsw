GARNAME = less
GARVERSION = 382
CATEGORIES = utils

DESCRIPTION = A terminal based program for viewing text files.
define BLURB
    Less is a program similar to more, i.e. a terminal based program for viewing
    text files and the output from other programs. Less offers many features beyond
    those that more does. For instance, it allows backward movement in the files as
    well as forward.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

LIBDEPS = lib/ncurses

INSTALL_OVERRIDE_DIRS = bindir mandir

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk
