# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = t1lib
VERSION = 5.1.2
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Type1 font renderering library
define BLURB
  t1lib is a library distributed under the GNU General Public Library
  License for generating character- and string-glyphs from Adobe Type 1
  fonts under UNIX. t1lib uses most of the code of the X11 rasterizer
  donated by IBM to the X11-project. But some disadvantages of the
  rasterizer being included in X11 have been eliminated.
endef

MASTER_SITES = ftp://sunsite.unc.edu/pub/Linux/libs/graphics/
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER			=	GNU
# there is no check defined in upstream's Makefile:
SKIPTEST			=	1

include gar/category.mk

