# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = inkscape
VERSION = 0.48.4
GARTYPE = v2

DESCRIPTION = Open source scalable vector graphics editor

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2

GARCOMPILER = GNU

BUILD_DEP_PKGS += CSWlibwpg-dev

CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_CONFIGURE_EXPORTS += XGETTEXT MSGMERGE MSGFMT
CONFIGURE_ENV_XGETTEXT = $(bindir)/gxgettext
CONFIGURE_ENV_MSGMERGE = $(bindir)/gmsgmerge
CONFIGURE_ENV_MSGFMT = $(bindir)/gmsgfmt

#EXTRA_CONFIGURE_EXPORTS += PROTOC
#CONFIGURE_ENV_PROTOC = $(prefix)/gxx/bin/protoc

# Use this until GCC boost is moved to /opt/csw
EXTRA_INC += $(prefix)/gxx/include
EXTRA_LIB += $(prefix)/gxx/lib


include gar/category.mk

