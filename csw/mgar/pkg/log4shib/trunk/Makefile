# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = log4shib
VERSION = 1.0.8
GARTYPE = v2

DESCRIPTION = Fork of log4cpp for the Shibboleth project

MASTER_SITES += http://shibboleth.net/downloads/log4shib/latest/
DISTFILES += $(DISTNAME).tar.gz

GARCOMPILER = GCC4
#CONFIGURE_ARGS = $(DIRPATHS)
RUNTIME_DEP_PKGS_CSWlog4shib += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlog4shib += CSWlibstdc++6
CONFIGURE_ARGS = --disable-static --disable-doxygen --prefix=/opt/csw

include gar/category.mk

