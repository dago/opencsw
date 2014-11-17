# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gnome-doc-utils
VERSION = 0.4.4
SUBDIR = $(basename $(VERSION))
GARTYPE = v2

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES =  http://ftp.gnome.org/pub/gnome/sources/$(NAME)/$(SUBDIR)/
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER = GCC4

BUILD_DEP_PKGS += CSWpm-xml-parser
BUILD_DEP_PKGS += CSWlibxml2-dev
BUILD_DEP_PKGS += CSWlibxslt-dev

EXTRA_MERGE_EXCLUDE_FILES = /var/lib.*
SKIPTEST = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

