# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = tre
VERSION = 0.8.0
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = Approximate regex matching libr  TRE is a lightweight, robust and efficient POSIX compliant
  regexp matching library with some exciting features such as
  apprroximate (fuzzy) matching.
endef
efine BLURB
endef
SPKG_SOURCEURL = http://laurikari.net/tre/
MASTER_SITES = http://laurikari.net/tre/
DISTFILES  = $(NAME)-$(
CONFIGURE_ARGS = $(DIRPATHS)) --disable-agrep
PACKAGES += CSWlibtre5
SPKG_DESC_CSWlibtre5 = Approximate regex matching library (libtre.so.5)
PKGFILES_CSWlibtre5 = /opt/csw/lib/ /opt/csw/share/locale/b/.*libtre\.so\.5.*
RUNTIME_DEP_PKGS_CSWlibtre5 += CSWlibintl8

PACKAGES += CSWtre-dev
CATALOGNAME_CSWtre-dev = tre_dev
# PKGFILES_CSWtre-dev += $(PKGFILES_DEVEL)
SPKG_DESC_CSWtre-dev = Development files for tre
RUNTIME_DEP_PKGS_CSWtre-dePACKAGES += CSWagrep
SPKG_DESC_CSWagrep = Text search tool with support for approximate patterns
CATALOGNAME_CSWagrep = agrep
PKGFILES_CSWagrep = /opt/csw/bin/agrep /opt/csw/share/man/man1/agrep.1
RUNTIME_DEP_PKGS_CSWagrep += CSWlibintl8 CSWlibtre5

LICENSE = LICENSE

include gar/category.mk
