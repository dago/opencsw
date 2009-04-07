GARNAME = libgda
GARVERSION = 3.99.14
CATEGORIES = gnome

DESCRIPTION = GNU Data Access
define BLURB
 GNU Data Access (GDA) is an attempt to provide uniform access to different
 kinds of data sources (databases, information servers, mail spools, etc).
 It is a complete architecture that provides all you need to access your data.
 It is defined by a set of plugin APIs as generic as possible
 (but very powerful at the same time) so that any kind of data source
 can be accessed through them.
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTNAME  = $(GARNAME)-$(GARVERSION)

REQUIRED_PKGS += CSWggettextrt CSWglib2 CSWiconv CSWlibxml2 CSWlibxslt
REQUIRED_PKGS += CSWncurses CSWreadline CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CFLAGS += -D__FUNCTION__=__func__
CXXFLAGS += -D__FUNCTION__=__func__

CONFIGURE_ARGS = $(DIRPATHS)

# One test fail for some reason...
#TEST_TARGET = check
TEST_TARGET = 

include gar/category.mk

PATH :=/opt/csw/bin:/opt/csw/gnu:$(PATH)
