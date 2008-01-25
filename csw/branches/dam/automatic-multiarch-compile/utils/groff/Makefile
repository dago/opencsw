GARNAME = groff
GARVERSION = 1.19
CATEGORIES = utils

DESCRIPTION = front end for the groff document formatting system
define BLURB
    groff is the front end to a ducument formatting system.  Included with GNUs
    version of groff are the utilities: troff, pic, eqn, tbl, grn, refer, -man,
    -mdoc, and -ms; drivers for the PostScript, TeX dvi format, HP LaserJet 4
    printers, Canon CAPSL printers, HTML format (still alpha), and typewriter-
    like devices.  Also included is a modified version fo the Berkeley -me 
    macros, an enhanced version of the X11 xditview previewer, and an 
    implimentation of the -mm macros contributed by Joergen Haegg (jg@axis.se).
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_OVERRIDE_DIRS = bindir datadir

TEST_TARGET = check

include ../category.mk
