# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = zabbix
VERSION = 1.8.10
GARTYPE = v2-build64only
CATEGORIES = server

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

BUILD64_ONLY = 1

RUNTIME_DEP_PKGS_CSWzabbix += CSWlibmysqlclient15
RUNTIME_DEP_PKGS_CSWzabbix += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWzabbix += CSWlibz1
RUNTIME_DEP_PKGS_CSWzabbix += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWzabbix += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWzabbix += CSWlibidn11

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-mysql
CONFIGURE_ARGS += --with-libcurl
CONFIGURE_ARGS += --enable-server
CONFIGURE_ARGS += --enable-agent
CONFIGURE_ARGS += --enable-ipv6

include gar/category.mk

