# $Id$
NAME = Socket-GetAddrInfo
VERSION = 0.22
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PEVANS

DESCRIPTION = Address-family independent name resolving functions
define BLURB
endef

LICENSE_TEXT = This module is licensed under the Perl license

DISTFILES  = $(DISTNAME).tar.gz

PACKAGES = CSWpm-socket-getaddrinfo
CATALOGNAME = pm_socket_getaddrinfo

BUILD_DEP_PKGS += CSWpm-extutils-cchecker

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
