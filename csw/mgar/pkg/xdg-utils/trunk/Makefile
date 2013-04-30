# $Id$

NAME	=	xdg-utils
# TODO: try 1.1.0 rc1 + git, same as Debian
VERSION	=	1.0.2
GARTYPE	=	v2

DESCRIPTION	=	Basic desktop integration functions
define BLURB
  A set of simple scripts that provide basic desktop integration functions
  for any Free Desktop.
endef

MASTER_SITES =	http://portland.freedesktop.org/download/
DISTFILES 	=	$(DISTNAME).tgz
PATCHFILES	+=	0001-adapt-to-available-utilities-set.patch

BUILD_DEP_PKGS	+=	CSWxmlto

GARCOMPILER		=	GNU
CONFIGURE_ARGS	=	$(DIRPATHS)

TEST_SCRIPTS	=	custom

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

# TODO there is work remaining on specific tests
test-custom:
	-(cd $(WORKSRC)/tests && \
	 	/usr/bin/env -i \
		  $(CONFIGURE_ENV) \
			./testrun -R -C -I)
	@$(MAKECOOKIE)
