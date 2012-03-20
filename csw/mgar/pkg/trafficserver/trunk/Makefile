# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = trafficserver
VERSION = 3.0.4
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = Apache Traffic Server is fast, scalable and extensible HTTP/1.1 compliant caching proxy server.
define BLURB
  Apache Traffic Server is fast, scalable and extensible HTTP/1.1 compliant caching proxy server
endef

MASTER_SITES = http://people.apache.org/~zwoop/rel-candidates/
DISTFILES  = $(DISTNAME).tar.bz2

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-tcl=$(libdir)
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-pcre=$(prefix)
CONFIGURE_ARGS += --with-lzma=$(prefix)
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --with-user=$(shell /opt/csw/gnu/id -nu)
CONFIGURE_ARGS += --with-group=$(shell /opt/csw/gnu/id -ng)

PROTOTYPE_MODIFIERS = config data
PROTOTYPE_FILES_config = $(sysconfdir)
PROTOTYPE_CLASS_config = cswconffile
PROTOTYPE_USER_config = nobody
PROTOTYPE_GROUP_config = $(shell id -ng nobody)
PROTOTYPE_FILES_data = $(datadir)
PROTOTYPE_FILES_data = $(datadir)

PACKAGING_PLATFORMS = solaris10-i386
SKIP_MODULATIONS = isa-i386 isa-pentium_pro
BUILD64 = 1

include gar/category.mk

