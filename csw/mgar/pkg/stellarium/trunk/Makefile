# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = stellarium
VERSION = 0.10.4
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Planetarium with a realistic 3D sky just like seeing with naked eye
define BLURB
  Stellarium is a free open source planetarium for your computer. It shows a realistic
  sky in 3D, just like what you see with the naked eye, binoculars or a telescope. 
  It is being used in planetarium projectors. Just set your coordinates and go.
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
