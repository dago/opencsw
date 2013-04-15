# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pubcookie
VERSION = 3.3.4a
GARTYPE = v2

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://www.pubcookie.org/downloads/
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS) --enable-login --enable-ldap --enable-shadow --with-apxs=/opt/csw/apache2/sbin/apxs 

SKIPTEST = 1
include gar/category.mk

