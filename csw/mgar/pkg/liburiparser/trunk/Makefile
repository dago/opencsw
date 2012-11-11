# $Id$
NAME = liburiparser
VERSION = 0.7.7
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = RFC 3986 Compliant URI Parsing Library
define BLUECTRB
endef

SF_PROJ = uriparser
MASTER_SITES = $(SF_MIRROR)
DISTNAME = $(SF_PROJ)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD_DEP_PKGS = CSWlibcpptest-dev

PACKAGES += CSWliburiparser1
SPKG_DESC_CSWliburiparser1 = RFC 3986 compliant URI parsing library, liburiparser.so.1
PKGFILES_CSWliburiparser1 += $(call pkgfiles_lib,liburiparser.so.1)

PACKAGES += CSWliburiparser-dev
SPKG_DESC_CSWliburiparser-dev = Development files for liburiparser.so.1
RUNTIME_DEP_PKGS_CSWliburiparser-dev += CSWliburiparser1
OBSOLETED_BY_CSWliburiparser-dev += CSWliburiparserdevel
CATALOGNAME_CSWliburiparserdevel = liburiparser_devel_stub

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --docdir=$(docdir)/$(NAME)

include