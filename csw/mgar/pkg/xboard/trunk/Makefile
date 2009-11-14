GARNAME = xboard
GARVERSION = 4.4.1
CATEGORIES = apps

DESCRIPTION = X graphical chessboard
define BLURB
  XBoard is a graphical user interface for chess in all its major forms,
  including international chess, xiangqi (Chinese chess) and shogi (Japanese chess),
  in addition to many minor variants such as Losers Chess, Crazyhouse, Chess960 and
  Capabanca Chess. It displays a chessboard on the screen, accepts moves made with
  the mouse, and loads and saves games in Portable Game Notation (PGN).
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

EXTRA_LDFLAGS = -lm /usr/openwin/lib/libXext.so

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
