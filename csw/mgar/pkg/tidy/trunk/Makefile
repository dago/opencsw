# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tidy
VERSION = 20090325cvs
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = An HTML Syntax Checker and Reformatter
define BLURB
An HTML Syntax Checker and Reformatter
endef

MASTER_SITES = http://tidy.sourceforge.net
DISTFILES  = $(DISTNAME).tar.gz

LICENSE = LICENSE

include gar/category.mk

pre-configure-modulated:
	@(cd $(WORKSRC); bash build/gnuauto/setup.sh; \
		lynx --dump htmldoc/license.html > LICENSE )
	@$(MAKECOOKIE)
