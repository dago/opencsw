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

ARCHALL	=	1

REINPLACE_WHEN_USRLOCAL	=	postinstall
REINPLACE_USRLOCAL		+=	/opt/csw/bin/xdg-mime
REINPLACE_USRLOCAL		+=	/opt/csw/bin/xdg-desktop-menu
REINPLACE_USRLOCAL		+=	/opt/csw/bin/xdg-icon-resource
REINPLACE_WHEN_USRSHARE	=	postinstall
REINPLACE_USRSHARE		+=	/opt/csw/bin/xdg-mime
REINPLACE_USRSHARE		+=	/opt/csw/bin/xdg-desktop-menu
REINPLACE_USRSHARE		+=	/opt/csw/bin/xdg-icon-resource

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

# TODO there is work remaining on specific tests; most of them fail as
# they cannot acces to the X server
test-custom:
	-(cd $(WORKSRC)/tests && \
	 	/usr/bin/env -i \
		  $(CONFIGURE_ENV) \
			./testrun -R -C -I)
	@$(MAKECOOKIE)

# replace all shebangs sh to bash as that is expected:
post-install:
	cd $(DESTDIR)$(bindir) && \
		gsed -i 's;^#!/bin/sh$$;#!/usr/bin/env bash;' *
	@$(MAKECOOKIE)
