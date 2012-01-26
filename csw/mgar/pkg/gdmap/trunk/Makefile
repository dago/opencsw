NAME = gdmap
VERSION = 0.8.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = GdMap is a tool which allows to visualize disk space
define BLURB
  GdMap is a tool which allows to visualize disk space. Ever wondered why your
  hard disk is full or what directory and files take up most of the space?
  With GdMap these questions can be answered quickly. To display directory
  structures cushion treemaps are used which visualize a complete folder or
  even the whole hard drive with one picture.
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWgtk2 CSWlibatk CSWlibcairo CSWlibxml2 CSWpango
BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWglib2devel CSWgtk2devel CSWlibcairodevel CSWlibxml2devel CSWpangodevel

EXTRA_INC = $(prefix)X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

# Needed for sqrt(3m)
EXTRA_LDFLAGS = -lm

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# For GNU gettext
PATH := /opt/csw/gnu:$(PATH)
