# $Id$
#
NAME = yapet
VERSION = 0.8pre2
CATEGORIES = apps

DESCRIPTION = Text-based Password Manager
define BLURB
	YAPET is a text based password manager using the Blowfish encryption
	algorithm. Because of its small footprint and very few library dependencies,
	it is suited for installing on desktop and server systems alike.
endef

MASTER_SITES = http://www.guengel.ch/myapps/yapet/downloads/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += README.CSW

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

RUNTIME_DEP_PKGS  = CSWosslrt
RUNTIME_DEP_PKGS += CSWlibncurses5
RUNTIME_DEP_PKGS += CSWlibintl8

BUILD_DEP_PKGS  = CSWossldevel
BUILD_DEP_PKGS += CSWlibncurses-dev
BUILD_DEP_PKGS += CSWggettext-dev

EXTRA_INC = /opt/csw/include/ncurses
EXTRA_CXXFLAGS += -norunpath

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

