# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = docbook2X
VERSION = 0.8.8
GARTYPE = v2

DESCRIPTION = Converts DocBook documents to man and Texinfo format

MASTER_SITES = $(SF_MIRRORS)
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://docbook2x.sourceforge.net

BUILD_DEP_PKGS += CSWxalan-j
BUILD_DEP_PKGS += CSWxercesj
BUILD_DEP_PKGS += CSWjre8

PACKAGES += CSWdocbook2x
SPKG_DESC_CSWdocbook2x = Converts DocBook documents to man and Texinfo format
# PKGFILES is catchall

# Unconditional -Wall
GARCOMPILER = GNU

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-xalan-jars=/opt/csw/share/java/xalan.jar
CONFIGURE_ARGS += --with-resolver-jars=/opt/csw/share/java/resolver.jar

EXTRA_CONFIGURE_EXPORTS += JAVA
CONFIGURE_ENV_JAVA = /opt/csw/java/jre/jre8/bin/java

# Tests access network and try to load lots of funky DTDs
SKIPTEST ?= 1

include gar/category.mk

