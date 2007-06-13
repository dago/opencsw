GARNAME = orca
GARVERSION = snapshot-r529
SPKG_VERSION = r529
CATEGORIES = utils

DESCRIPTION = A system performance monitoring tool
define BLURB
  The SE Toolkit is
  * An interpreter for a programming language that is both a subset of C and C++.
    Syntactically, it looks like C, but it contains a limited class mechanism.
  * Include files for use by toolkit scripts.
  * A bunch of example scripts.
  * A set of extensions for writing GUIs and "network aware" scripts.
endef

MASTER_SITES = http://www.orcaware.com/orca/pub/snapshots/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWorca,depend)

CONFIGURE_ARGS = $(DIRPATHS) \
	--with-html-dir=$(prefix)/apache2/share/htdocs/orca \
	--disable-librrdtool

include ../category.mk
