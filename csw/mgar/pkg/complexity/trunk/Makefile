# $Id$

NAME	=	complexity
VERSION	=	1.1
GARTYPE	=	v2

DESCRIPTION	=	Measure complexity of C source
define BLURB
  A tool designed for analyzing the complexity of "C" program
  functions.  It is very similar to the McCabe scoring, but addresses
  several issues not considered in that scoring scheme.
endef

MASTER_SITES	=	$(GNU_MIRROR)
DISTFILES		=	$(DISTNAME).tar.gz
PATCHFILES		+=	0001-test-driver-uses-bash.patch

GARCOMPILER		=	GNU
CONFIGURE_ARGS	=	$(DIRPATHS)

BUILD_DEP_PKGS	=	CSWautogen-dev

RUNTIME_DEP_PKGS_CSWcomplexity	+=	CSWlibopts25

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

