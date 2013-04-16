# $Id$
#
NAME = dircproxy
VERSION = 1.2.0-RC1
GARTYPE = v2

DESCRIPTION = IRC proxy
define BLURB
  Software for IRC proxy
endef

MASTER_SITES = http://dircproxy.googlecode.com/files/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Include-string.h-to-mitigate-warnings.patch

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-ssl

RUNTIME_DEP_PKGS += CSWperl

REINPLACE_USRLOCAL += conf/dircproxyrc.sample

include gar/category.mk

