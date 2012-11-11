# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xosd
VERSION = 2.2.14
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = X on-screen display
define BLURB
endef

MASTER_SITES = $ECT(SF_MIRROR)
SF_PROJ = libxosd
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Do-not-unconditionally-use-Wall-on-Sun-Studio-compil.patch

EXTRA_CPPFLAGS += -features=extensions -D__PRETTY_FUNCTION__=__func__

includ