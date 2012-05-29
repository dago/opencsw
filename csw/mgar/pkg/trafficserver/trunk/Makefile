# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = trafficserver
VERSION = 3.1.4-unstable
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = Apache Traffic Server is fast, scalable and extensible HTTP/1.1 compliant caching proxy server.
define BLURB
  Apache Traffic Server is fast, scalable and extensible HTTP/1.1 compliant caching proxy server
endef

MASTER_SITES = http://people.apache.org/~zwoop/rel-candidates/
DISTFILES  = $(DISTNAME).tar.bz2

PACKAGING_PLATFORMS = solaris10-i386
BUILD64_ONLY = 1
ISAEXEC = 1

pkgsysuser  = $(shell /opt/csw/gnu/id -nu)
pkgsysgroup = $(shell /opt/csw/gnu/id -ng)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/$(NAME)
CONFIGURE_ARGS += --libexecdir=$(libexecdir)/$(NAME)
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-tcl=$(libdir)
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-pcre=$(prefix)
CONFIGURE_ARGS += --with-lzma=$(prefix)
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --enable-hwloc
CONFIGURE_ARGS += --with-user=$(pkgsysuser)
CONFIGURE_ARGS += --with-group=$(pkgsysgroup)

PROTOTYPE_MODIFIERS += data
PROTOTYPE_FILES_data += $(sysconfdir)/?.*
PROTOTYPE_FILES_data += $(datadir)/?.*
PROTOTYPE_USER_data = nobody
PROTOTYPE_GROUP_data = nobody

REINPLACE_MATCH = $(pkgsysuser)
REINPLACE_WITH = nobody
REINPLACE_FILES += $(sysconfidir)/$(NAME)/records.config
REINPLACE_WHEN = postinstall

STRIP_LIBTOOL = 1

include gar/category.mk

