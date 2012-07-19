# $Id$

NAME = gwrap
VERSION = 1.3.4
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A tool for exporting C libraries into Scheme interpreters
define BLURB
  A tool for exporting C libraries into Scheme interpreters
endef

DISTNAME		=	g-wrap-$(VERSION)
MASTER_SITES	=	http://www.gnucash.org/pub/g-wrap/source/
DISTFILES		=	$(DISTNAME).tar.gz
PATCHFILES		+=	0001-Remove-unused-variable.patch
PATCHFILES		+=	0002-Inhibit-unused-but-set-variable.patch
PATCHFILES		+=	0003-Correct-shell.patch

BUILD_DEP_PKGS	+=	CSWglib
BUILD_DEP_PKGS	+=	CSWgtk
BUILD_DEP_PKGS	+=	CSWslib

GARCOMPILER		=	GNU

CONFIGURE_ARGS	=	$(DIRPATHS)

include gar/category.mk

