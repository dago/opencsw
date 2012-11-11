NAME = xmlstarlet
VERSION = 1.3.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = XML transformation utility
define BLURB
  XMLStarlet is a set of command line utilities (tools)
  to transform, query, validate, and edit XML documents
  and files using simple set of shell commands in similar
  way it is done for text files with UNIX grep, sed, awk,
  diff, patch, join, etc utilitECTies.
endef

SF_PROJ = xmlstar
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(DISTNAME).tar.gz

VENDOR_URL = http://xmlstar.sourceforge.net/

BUILD_DEP_PKGS += CSWlibxml2-dev
BUILD_DEP_PKGS += CSWlibxslt-dev

RUNTIME_DEP_PKGS_CSWxmlstarlet += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWxmlstarlet += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWxmlstarlet += CSWlibexslt0

BUILD64 = 1
ISAEXEC = 1

EXTRA_CONFIGURE_ENV += LIBXML_CONFIG=$(bindir)/xml2-config
EXTRA_CONFIGURE_ENV += LIBXSLT_CONFIG=$(bindir)/xslt-config

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-static-libs
CONFIGURE_ARGS += --with-libxml-include-prefix=$(includedir)/libxml2
CONFIGURE_ARGS += --with-libxml-libs-prefix=$(libdir)

BUILD_OVERRIDE_VARS = CFLAGS CPPFLAGS LDFLAGS
BUILD_OVERRIDE_VAR_CFLAGS = $(CFLAGS)
BUILD_OVERRIDE_VAR_CPPFLAGS = $(CPPFLAGS)
BUILD_OVERRIDE_VAR_LDFLAGS = $(LDFLAGS)

EXTRA_PAX_ARGS = -s ,$(bindir)/xml,$(bindir)/xmlstarlet,

inclu