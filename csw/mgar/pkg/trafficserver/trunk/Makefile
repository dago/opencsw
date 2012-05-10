# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = trafficserver
VERSION = 3.0.5
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = Apache Traffic Server is fast, scalable and extensible HTTP/1.1 compliant caching proxy server.
define BLURB
  Apache Traffic Server is fast, scalable and extensible HTTP/1.1 compliant caching proxy server
endef

MASTER_SITES = http://people.apache.org/~igalic/releases/
DISTFILES  = $(DISTNAME).tar.bz2

PACKAGING_PLATFORMS = solaris10-i386
BUILD64_ONLY = 1
ISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/$(NAME)
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-tcl=$(libdir)
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-pcre=$(prefix)
CONFIGURE_ARGS += --with-lzma=$(prefix)
CONFIGURE_ARGS += --with-expat=$(prefix)

pkgsysuser  = $(shell /opt/csw/gnu/id -nu)
pkgsysgroup = $(shell /opt/csw/gnu/id -ng)

EXTRA_CONFIGURE_EXPORTS += pkgsysuser
EXTRA_CONFIGURE_ENV_pkgsysuser += $(pkgsysuser)

EXTRA_CONFIGURE_EXPORTS += pkgsysgroup
EXTRA_CONFIGURE_ENV_pkgsysgroup = $(pkgsysgroup)

EXTRA_BUILD_EXPORTS += pkgsysuser
EXTRA_BUILD_ENV_pkgsysuser = $(pkgsysuser)

EXTRA_BUILD_EXPORTS += $(pkgsysgroup)
EXTRA_BUILD_ENV_pkgsysgroup = $(pkgsysgroup)

PROTOTYPE_MODIFIERS += data
PROTOTYPE_FILES_data += $(sysconfdir)/?.*
PROTOTYPE_FILES_data += $(datadir)/?.*
PROTOTYPE_USER_data = nobody
PROTOTYPE_GROUP_data = nobody

include gar/category.mk

